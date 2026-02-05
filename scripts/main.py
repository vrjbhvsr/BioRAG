from generation.query_rewrite import QueryRewriter
from generation.mapping import Mapper
from generation.reduce import Reducer
from generation.deduplication import Deduplication
from config.logging import log
from config.exception import CustomException
import sys
from constants import *
from typing import Optional, Literal
from generation.generation_pipeline import GenerationPipeline
from models.Llama import model
import uuid
from generation.graph import create_graph
from generation.state import State

model = model().load()

rewriter = QueryRewriter(model)
deduplicator = Deduplication()
mapper = Mapper(model)
reducer = Reducer(model)


pipeline = GenerationPipeline(rewriter, deduplicator, mapper, reducer)
app = create_graph(pipeline)

# Create a unique session ID for this chat
session_config = {"configurable": {"thread_id": str(uuid.uuid4())}}

print("Chatbot initialized. Type 'exit' to quit.")
while True:
    user_input = input("\nUser: ")
    if user_input.lower() in ["exit", "quit"]:
        break

    # We only send the NEW message. 
    # LangGraph pulls the PREVIOUS messages from the checkpointer using the thread_id.
    output = app.invoke(
        {"messages": [("user", user_input)]}, 
        config=session_config
    )

    # Get the last message in the state (the AI's response)
    ai_response = output["messages"][-1].content
    print(f"\nAI: {ai_response}")