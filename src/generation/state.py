from typing import Annotated, TypedDict, List
from langgraph.graph.message import add_messages

class State(TypedDict):
    # This 'add_messages' is the secret sauce for continuous chat
    messages: Annotated[list, add_messages] 
    rewritten_queries: List[str]  
    docs: List[dict]
    mapped_responses: List[str]
    final_answer: str