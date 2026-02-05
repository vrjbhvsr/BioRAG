from generation.query_rewrite import QueryRewriter
from generation.mapping import Mapper
#from generation.reduce import Reducer
from retrieval.parent_retriever import retriever
from generation.deduplication import Deduplication
from config.logging import log
from config.exception import CustomException
import sys
from constants import *
from typing import Optional, Literal
from generation.state import State
from langchain_core.messages import AIMessage

logger = log()
log = logger.get_logger(__name__)

class GenerationPipeline:
    def __init__(self, 
                rewriter,
                deduplicator,
                mapper,
                reducer):
        self.QueryRewriter = rewriter
        self.deduplicator = deduplicator
        self.Mapper = mapper
        self.Reducer = reducer

    def run(self, query: str) -> Optional[str]:
        """This Function run the complete generation pipeline to generate the final answer.
        Args:
        query: str = The input query from the user.
        """    
        try:
            log.info(
                "\n"
                "================ Query Rewriting started ================\n"
            )
            rewritten_query_list = self.QueryRewriter.rewrite(query)
            log.info("Query rewritten successfully.")
            log.info(
                "\n"
                "================ Deduplication started ================\n"
            )
            deduplicated_docs = self.deduplicator.deduplicate(rewritten_query_list)

            log.info(
                "\n"
                "================ Mapping started ================\n"
            )
            mapped_responses = self.Mapper.map(rewritten_query_list, deduplicated_docs)
            log.info("Mapping completed successfully.")

            log.info(
                "\n"
                "================ Reducing started ================\n"
            )
            final_response = self.Reducer.reduce(query,mapped_responses)
            log.info("Reduction completed successfully.")

            return final_response
    
        except Exception as e:
            log.error(e)
            raise CustomException(e, sys)
    
    '''def rewrite_node(self, state: State):

        # Once the user ask the query it will be loaded in the sate as a last message
        query = state["messages"][-1].content
        rewritten_queries = self.QueryRewriter.rewrite(query)
        return {"rewritten_queries": rewritten_queries}

    def deduplicate_node(self, state: State):
        # state also stories the list of queries
        docs = self.deduplicator.deduplicate(state["rewritten_queries"])
        return {"docs": docs}

    def map_node(self, state: State):

        responses = self.Mapper.map(state["rewritten_queries"], state["docs"])
        return {"mapped_responses": responses}

    def reduce_node(self, state: State):
       
        original_query = state["messages"][-1].content
        final_answer = self.Reducer.reduce(original_query, state["mapped_responses"])
        
        
        return {"messages": [AIMessage(content=final_narrative)],
        "key_metrics": parsed_output.key_metrics}'''

