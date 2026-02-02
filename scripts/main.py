from langgraph.graph import StateGraph, END
from langgraph.checkpoint.memory import MemorySaver
from state import GraphState
from  import decompose_query
from map import generate_summaries
from reduce import synthesize_answer

# 1. Initialize the Graph
workflow = StateGraph(GraphState)

# 2. Add your existing logic as "Nodes"
workflow.add_node("decomposer", decompose_query)
workflow.add_node("map_summaries", generate_summaries)
workflow.add_node("reduce_synthesis", synthesize_answer)

# 3. Define the Flow (Edges)
workflow.set_entry_point("decomposer")
workflow.add_edge("decomposer", "map_summaries")
workflow.add_edge("map_summaries", "reduce_synthesis")
workflow.add_edge("reduce_synthesis", END)

# 4. Add the Checkpointer (This enables the "Continuous" part)
memory = MemorySaver()
app = workflow.compile(checkpointer=memory)