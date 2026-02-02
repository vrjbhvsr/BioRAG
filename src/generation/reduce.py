from chains.reduce_chain import reduce_chain
from config.logging import log
from config.exception import CustomException
import sys
from constants import *
from typing import List

logger = log()
log = logger.get_logger(__name__)

class Reducer:
    """
    A class to handle the reducing process using the reduce chain.
    """
    def __init__(self, model):
        self.reduce_chain = reduce_chain(model).chain()
        

    def reduce(self,query: str, mapped_responses: List[str]) -> str:
        """
        Reduces the mapped responses using the reduce chain.

        Args:
            mapped_responses (list): A list of mapped responses to be reduced.

        Returns:
            str: The reduced response.
        """
        inputs = {"user_query": query, "map_summaries": mapped_responses}
        
        try:
            log.info("Starting reducing process...")
            reduced_response = self.reduce_chain.invoke(inputs, config = {"max_concurrency": MAX_CONCURRENCY})
            log.info("Reducing process completed successfully.")
            return reduced_response
        except Exception as e:
            log.error("Error during reducing process.")
            raise CustomException(e, sys)