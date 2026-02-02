from typing import Annotated, TypedDict, List
from langgraph.graph.message import add_messages

class GraphState(TypedDict):
    # This 'add_messages' is the secret sauce for continuous chat
    messages: Annotated[list, add_messages] 
    sub_queries: List[str]
    retrieved_docs: List[dict]
    summaries: List[str]
    final_answer: str