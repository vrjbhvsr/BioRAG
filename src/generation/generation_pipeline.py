from generation.query_rewrite import QueryRewriter
from generation.mapping import Mapper
from generation.reduce import Reducer
from retrieval.parent_retriever import retirever
from config.logging import log
from config.exception import CustomException
import sys
from constants import *
from typing import Optional, Literal

logger = log()
log = logger.get_logger(__name__)

class GenerationPipeline:
    def __init__(self, 
                rewriter,
                 mapper,
                 reducer):
        self.rewriter = rewriter
        self.mapper = mapper
        self.reducer = reducer  

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
            rewritten_query_list = self.rewriter.rewrite(query)
            log.info("Query rewritten successfully.")

            log.info(
                "\n"
                "================ Mapping started ================\n"
            )
            mapped_responses = self.mapper.map(rewritten_query_list
                                               )
            log.info("Mapping completed successfully.")

            log.info(
                "\n"
                "================ Reducing started ================\n"
            )
            final_response = self.reducer.reduce(mapped_responses)
            log.info("Reduction completed successfully.")

            return final_response

        except Exception as e:
            log.error(e)
            raise CustomException(e, sys)
