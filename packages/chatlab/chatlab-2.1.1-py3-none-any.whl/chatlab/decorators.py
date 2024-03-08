"""ChatLab decorators.

This module lets you augment your functions before you register them with a ChatLab chat.

Examples:
    >>> from chatlab import Chat
    >>> from chatlab.decorators import expose_exception_to_llm

    >>> class PokemonFetchError(Exception):
    ...   def __init__(self, pokemon_name):
    ...     self.pokemon_name = pokemon_name
    ...     self.message = f"Failed to fetch information for Pokemon '{self.pokemon_name}'."
    ...     super().__init__(self.message)

    >>> @expose_exception_to_llm
    ... def fetch_pokemon(name: str):
    ...     '''Fetch information about a pokemon by name'''
    ...     url = f"https://pokeapi.co/api/v2/pokemon/{name}"
    ...     try:
    ...         response = requests.get(url)
    ...         response.raise_for_status()
    ...         return response.json()
    ...     except requests.HTTPError:
    ...         raise PokemonFetchError(name)

    >>> chat = Chat()
    >>> await chat("Get pikachu")
    Failed to fetch information for Pokemon 'pikachu'.

"""


from typing import Callable, Optional

from pydantic import BaseModel

class ChatlabMetadata(BaseModel):
    """ChatLab metadata for a function."""
    expose_exception_to_llm: bool = False
    render: Optional[Callable] = None

def expose_exception_to_llm(func):
    """Expose exceptions from calling the function to the LLM.

    Args:
        func (Callable): The function to annotate.

    Examples:
        >>> import chatlab
        >>> from chatlab.decorators import expose_exception_to_llm

        >>> @expose_exception_to_llm
        ... def roll_die():
        ...     roll = random.randint(1, 6)
        ...     if roll == 1:
        ...         raise Exception("The die rolled a 1!")
        ...     return roll
        >>> chat = chatlab.Chat()
        >>> await chat("Roll the dice!")
        The die rolled a 1!

    """
    if not hasattr(func, "chatlab_metadata"):
        func.chatlab_metadata = ChatlabMetadata()

    # Make sure that chatlab_metadata is an instance of ChatlabMetadata
    if not isinstance(func.chatlab_metadata, ChatlabMetadata):
        raise Exception("func.chatlab_metadata must be an instance of ChatlabMetadata")

    func.chatlab_metadata.expose_exception_to_llm = True
    return func


'''
The `incremental_display` decorator lets you render a function while the model is streaming in arguments.

def visualize_knowledge_graph(kg: KnowledgeGraph, comment: str = "Knowledge Graph"):
    """Visualizes a knowledge graph using graphviz."""
    dot = Digraph(comment=comment)

    for node in kg.nodes:
        dot.node(str(node.id), node.label, color=node.color)

    for edge in kg.edges:
        dot.edge(str(edge.source), str(edge.target), label=edge.label, color=edge.color)
    
    return dot


@incremental_display(visualize_knowledge_graph)
def store_knowledge_graph(kg: KnowledgeGraph, comment: str = "Knowledge Graph"):
    """Databases a knowledge graph"""
    ...

chat.register(store_knowledge_graph)
'''

def incremental_display(render_func: Callable):
    def decorator(func):
        if not hasattr(func, "chatlab_metadata"):
            func.chatlab_metadata = ChatlabMetadata()

        # Make sure that chatlab_metadata is an instance of ChatlabMetadata
        if not isinstance(func.chatlab_metadata, ChatlabMetadata):
            raise Exception("func.chatlab_metadata must be an instance of ChatlabMetadata")

        func.chatlab_metadata.render = render_func
        return func
    return decorator

