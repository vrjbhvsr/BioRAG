from langgraph.graph import StateGraph, END
from langgraph.checkpoint.memory import MemorySaver
from generation.state import State


def create_graph(pipeline_instance):
    workflow = StateGraph(State)

    # Register the methods as nodes
    workflow.add_node("rewrite", pipeline_instance.rewrite_node)
    workflow.add_node("deduplicate", pipeline_instance.deduplicate_node)
    workflow.add_node("map", pipeline_instance.map_node)
    workflow.add_node("reduce", pipeline_instance.reduce_node)

    # Set the flow
    workflow.set_entry_point("rewrite")
    workflow.add_edge("rewrite", "deduplicate")
    workflow.add_edge("deduplicate", "map")
    workflow.add_edge("map", "reduce")
    workflow.add_edge("reduce", END)

    # Add memory for continuous chat
    memory = MemorySaver()
    return workflow.compile(checkpointer=memory)