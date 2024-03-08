"""Registry of functions for use by ChatCompletions.

Example usage:

    from chatlab import FunctionRegistry
    from pydantic import BaseModel

    registry = FunctionRegistry()

    class Parameters(BaseModel):
        name: str

    from datetime import datetime
    from pytz import timezone, all_timezones, utc
    from typing import Optional
    from pydantic import BaseModel

    def what_time(tz: Optional[str] = None):
        '''Current time, defaulting to the user's current timezone'''
        if tz is None:
            pass
        elif tz in all_timezones:
            tz = timezone(tz)
        else:
            return 'Invalid timezone'
        return datetime.now(tz).strftime('%I:%M %p')

    class WhatTime(BaseModel):
        timezone: Optional[str]

    import chatlab
    registry = chatlab.FunctionRegistry()

    chat = chatlab.Chat(
        function_registry=registry,
    )

    await chat("What time is it?")

"""

import asyncio
import inspect
import json
from typing import (
    Any,
    Callable,
    Dict,
    Iterable,
    List,
    Optional,
    Type,
    TypedDict,
    Union,
    cast,
    get_args,
    get_origin,
    overload,
)

from openai.types import FunctionDefinition, FunctionParameters
from openai.types.chat.completion_create_params import Function, FunctionCall
from pydantic import BaseModel, Field, create_model

from openai.types.chat import ChatCompletionToolParam

from .decorators import ChatlabMetadata
from .errors import ChatLabError


class APIManifest(TypedDict, total=False):
    """The schema for the API."""

    functions: List[Function]
    """A list of functions that the model can call during the conversation."""

    function_call: FunctionCall
    """The policy for when to call functions.

    One of "auto", "none", or a dictionary with a "name" key.
    """


class FunctionArgumentError(ChatLabError):
    """Exception raised when a function is called with invalid arguments."""

    pass


class UnknownFunctionError(ChatLabError):
    """Exception raised when a function is called that is not registered."""

    pass


# Allowed types for auto-inferred schemas
ALLOWED_TYPES = [int, str, bool, float, list, dict, List, Dict]

JSON_SCHEMA_TYPES = {
    int: "integer",
    float: "number",
    str: "string",
    bool: "boolean",
    list: "array",
    dict: "object",
    List: "array",
    Dict: "object",
}


def is_optional_type(t):
    """Check if a type is Optional."""
    return get_origin(t) is Union and len(get_args(t)) == 2 and type(None) in get_args(t)


def is_union_type(t):
    """Check if a type is a Union."""
    return get_origin(t) is Union


class FunctionSchemaConfig:
    """Config used for model generation during function schema creation."""

    arbitrary_types_allowed = True


def extract_model_from_function(func_name: str, function: Callable) -> Type[BaseModel]:
    # extract function parameters and their type annotations
    sig = inspect.signature(function)

    fields = {}
    required_fields = []
    for name, param in sig.parameters.items():
        # skip 'self' for class methods
        if name == "self":
            continue

        # determine type annotation
        if param.annotation == inspect.Parameter.empty:
            # no annotation, raise instead of falling back to Any
            raise Exception(f"`{name}` parameter of {func_name} must have a JSON-serializable type annotation")
        type_annotation = param.annotation

        default_value: Any = ...

        # determine if there is a default value
        if param.default != inspect.Parameter.empty:
            default_value = param.default
        else:
            required_fields.append(name)

        # Check if the annotation is Union that includes None, indicating an optional parameter
        if get_origin(type_annotation) is Union:
            args = get_args(type_annotation)
            if len(args) == 2 and type(None) in args:
                type_annotation = next(arg for arg in args if arg is not type(None))
                default_value = None

        fields[name] = (type_annotation, Field(default=default_value) if default_value is not ... else ...)

    model = create_model(
        function.__name__,
        __config__=FunctionSchemaConfig,  # type: ignore
        **fields,  # type: ignore
    )
    return model


def generate_function_schema(
    function: Callable,
    parameter_schema: Optional[Union[Type["BaseModel"], dict]] = None,
) -> FunctionDefinition:
    """Generate a function schema for sending to OpenAI."""
    doc = function.__doc__
    func_name = function.__name__

    if not func_name:
        raise Exception("Function must have a name")
    if func_name == "<lambda>":
        raise Exception("Lambdas cannot be registered. Use `def` instead.")
    if not doc:
        raise Exception("Only functions with docstrings can be registered")

    schema = FunctionDefinition(
        name=func_name,
        description=doc,
        parameters={},
    )

    if isinstance(parameter_schema, dict):
        parameters = parameter_schema
    elif parameter_schema is not None:
        parameters = parameter_schema.model_json_schema()  # type: ignore
    else:
        model = extract_model_from_function(func_name, function)
        parameters: dict = model.model_json_schema()  # type: ignore

    if "properties" not in parameters:
        parameters["properties"] = {}

    # remove "title" since it's unused by OpenAI
    parameters.pop("title", None)
    for field_name in parameters["properties"].keys():
        parameters["properties"][field_name].pop("title", None)

    if "required" not in parameters:
        parameters["required"] = []

    schema.parameters = parameters
    return schema


# Declare the type for the python hallucination
PythonHallucinationFunction = Callable[[str], Any]


def adapt_function_definition(fd: FunctionDefinition) -> Function:
    """Adapt a FunctionDefinition to a Function for working with the OpenAI API."""
    return {
        "name": fd.name,
        "parameters": cast(FunctionParameters, fd.parameters),
        "description": fd.description if fd.description is not None else "",
    }


class FunctionRegistry:
    """Registry of functions and their schemas for calling them.

    Example usage:

        from chatlab import FunctionRegistry

        from datetime import datetime
        from pytz import timezone, all_timezones, utc
        from typing import Optional
        from pydantic import BaseModel

        def what_time(tz: Optional[str] = None):
            '''Current time, defaulting to the user's current timezone'''
            if tz is None:
                pass
            elif tz in all_timezones:
                tz = timezone(tz)
                else:
                    return 'Invalid timezone'
            return datetime.now(tz).strftime('%I:%M %p')

        class WhatTime(BaseModel):
            timezone: Optional[str]

        import chatlab
        registry = chatlab.FunctionRegistry()
        registry.register(what_time, WhatTime)

        chat = chatlab.Chat(
            function_registry=registry,
        )

        await chat("What time is it?")
    """

    __functions: dict[str, Callable]
    __schemas: dict[str, FunctionDefinition]

    # Allow passing in a callable that accepts a single string for the python
    # hallucination function. This is useful for testing.
    def __init__(
        self,
        python_hallucination_function: Optional[PythonHallucinationFunction] = None,
    ):
        """Initialize a FunctionRegistry object."""
        self.__functions = {}
        self.__schemas = {}

        self.python_hallucination_function = python_hallucination_function

    def decorator(self, parameter_schema: Optional[Union[Type["BaseModel"], dict]] = None) -> Callable:
        """Create a decorator for registering functions with a schema."""

        def decorator(function):
            self.register_function(function, parameter_schema)
            return function

        return decorator

    @overload
    def register(
        self,
        function: None = None,
        parameter_schema: Optional[Union[Type["BaseModel"], dict]] = None,
    ) -> Callable:
        ...

    @overload
    def register(
        self,
        function: Callable,
        parameter_schema: Optional[Union[Type["BaseModel"], dict]] = None,
    ) -> FunctionDefinition:
        ...

    def register(
        self,
        function: Optional[Callable] = None,
        parameter_schema: Optional[Union[Type["BaseModel"], dict]] = None,
    ) -> Union[Callable, FunctionDefinition]:
        """Register a function for use in `Chat`s. Can be used as a decorator or directly to register a function.

        >>> registry = FunctionRegistry()
        >>> @registry.register
        ... def what_time(tz: Optional[str] = None):
        ...     '''Current time, defaulting to the user's current timezone'''
        ...     if tz is None:
        ...         pass
        ...     elif tz in all_timezones:
        ...         tz = timezone(tz)
        ...     else:
        ...         return 'Invalid timezone'
        ...     return datetime.now(tz).strftime('%I:%M %p')
        >>> registry.get("what_time")
        <function __main__.what_time(tz: Optional[str] = None)>
        >>> await registry.call("what_time", '{"tz": "America/New_York"}')
        '10:57 AM'

        """
        # If the function is None, assume this is a decorator call
        if function is None:
            return self.decorator(parameter_schema)

        # Otherwise, directly register the function
        return self.register_function(function, parameter_schema)

    def register_function(
        self,
        function: Callable,
        parameter_schema: Optional[Union[Type["BaseModel"], dict]] = None,
    ) -> FunctionDefinition:
        """Register a single function."""
        final_schema = generate_function_schema(function, parameter_schema)

        self.__functions[function.__name__] = function
        self.__schemas[function.__name__] = final_schema

        return final_schema

    def register_functions(self, functions: Union[Iterable[Callable], dict[str, Callable]]):
        """Register a dictionary of functions."""
        if isinstance(functions, dict):
            functions = functions.values()

        for function in functions:
            self.register(function)

    def get(self, function_name) -> Optional[Callable]:
        """Get a function by name."""
        if function_name == "python" and self.python_hallucination_function is not None:
            return self.python_hallucination_function

        return self.__functions.get(function_name)

    def get_schema(self, function_name) -> Optional[FunctionDefinition]:
        """Get a function schema by name."""
        return self.__schemas.get(function_name)

    def get_chatlab_metadata(self, function_name) -> ChatlabMetadata:
        """Get the chatlab metadata for a function by name."""
        function = self.get(function_name)

        if function is None:
            raise UnknownFunctionError(f"Function {function_name} is not registered")

        chatlab_metadata = getattr(function, "chatlab_metadata", ChatlabMetadata())
        return chatlab_metadata

    def api_manifest(self, function_call_option: FunctionCall = "auto") -> APIManifest:
        """Get a dictionary containing function definitions and calling options.

        This is designed to be used with OpenAI's Chat Completion API, where the
        dictionary can be passed as keyword arguments to set the `functions` and
        `function_call` parameters.

        The `functions` parameter is a list of dictionaries, each representing a
        function that the model can call during the conversation. Each dictionary
        has a `name`, `description`, and `parameters` key.

        The `function_call` parameter sets the policy of when to call these functions:
            - "auto": The model decides when to call a function (default).
            - "none": The model generates a user-facing message without calling a function.
            - {"name": "<insert-function-name>"}: Forces the model to call a specific function.

        Args:
            function_call_option (str or dict, optional): The policy for function calls.
            Defaults to "auto".

        Returns:
            dict: A dictionary with keys "functions" and "function_call", which
            can be passed as keyword arguments to `openai.ChatCompletion.create`.

        Example usage:
            >>> registry = FunctionRegistry()
            >>> # Register functions here...
            >>> manifest = registry.api_manifest()
            >>> resp = openai.ChatCompletion.create(
                    model="gpt-4.0-turbo",
                    messages=[...],
                    **manifest,
                    stream=True,
                )

            >>> # To force a specific function to be called:
            >>> manifest = registry.api_manifest({"name": "what_time"})
            >>> resp = openai.ChatCompletion.create(
                    model="gpt-4.0-turbo",
                    messages=[...],
                    **manifest,
                    stream=True,
                )

            >>> # To generate a user-facing message without calling a function:
            >>> manifest = registry.api_manifest("none")
            >>> resp = openai.ChatCompletion.create(
                    model="gpt-4.0-turbo",
                    messages=[...],
                    **manifest,
                    stream=True,
                )
        """
        function_definitions = [adapt_function_definition(f) for f in self.__schemas.values()]

        if len(function_definitions) == 0:
            # When there are no functions, we can't send an empty functions array to OpenAI
            return {}

        return {
            "functions": function_definitions,
            "function_call": function_call_option,
        }

    @property
    def tools(self) -> Iterable[ChatCompletionToolParam]:
        return [{"type": "function", "function": adapt_function_definition(f)} for f in self.__schemas.values()]

    async def call(self, name: str, arguments: Optional[str] = None) -> Any:
        """Call a function by name with the given parameters."""
        if name is None:
            raise UnknownFunctionError("Function name must be provided")

        # Handle the code interpreter hallucination
        if name == "python" and self.python_hallucination_function is not None:
            function = self.python_hallucination_function
            if arguments is None:
                arguments = ""

            # The "hallucinated" python function takes raw plaintext
            # instead of a JSON object. We can just pass it through.
            if asyncio.iscoroutinefunction(function):
                return await function(arguments)
            return function(arguments)

        possible_function = self.get(name)

        if possible_function is None:
            raise UnknownFunctionError(f"Function {name} is not registered")

        function = possible_function

        # TODO: Use the model extractor here
        prepared_arguments = extract_arguments(name, function, arguments)

        if asyncio.iscoroutinefunction(function):
            result = await function(**prepared_arguments)
        else:
            result = function(**prepared_arguments)
        return result

    def __contains__(self, name) -> bool:
        """Check if a function is registered by name."""
        if name == "python" and self.python_hallucination_function:
            return True
        return name in self.__functions

    @property
    def function_definitions(self) -> list[FunctionDefinition]:
        """Get a list of function definitions."""
        return list(self.__schemas.values())


def extract_arguments(name: str, function: Callable, arguments: Optional[str]) -> dict:
    dict_arguments = {}
    if arguments is not None and arguments != "":
        try:
            dict_arguments = json.loads(arguments)
        except json.JSONDecodeError:
            raise FunctionArgumentError(f"Invalid Function call on {name}. Arguments must be a valid JSON object")

    prepared_arguments = {}

    for param_name, param in inspect.signature(function).parameters.items():
        param_type = param.annotation
        arg_value = dict_arguments.get(param_name)

        # Check if parameter type is a subclass of BaseModel and deserialize JSON into Pydantic model
        if inspect.isclass(param_type) and issubclass(param_type, BaseModel):
            prepared_arguments[param_name] = param_type.model_validate(arg_value)
        else:
            prepared_arguments[param_name] = cast(Any, arg_value)

    return prepared_arguments
