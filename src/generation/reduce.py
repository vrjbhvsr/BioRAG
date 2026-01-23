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
    def __init__(self):
        self.reduce_chain = reduce_chain().chain()
        

    def reduce(self, mapped_responses: List[str]) -> str:
        """
        Reduces the mapped responses using the reduce chain.

        Args:
            mapped_responses (list): A list of mapped responses to be reduced.

        Returns:
            str: The reduced response.
        """
        inputs = {"mapped_responses": mapped_responses}
        try:
            log.info("Starting reducing process...")
            reduced_response = self.reduce_chain.batche(inputs, config = {"max_concurrency": MAX_CONCURRENCY})
            log.info("Reducing process completed successfully.")
            return reduced_response
        except Exception as e:
            log.error("Error during reducing process.")
            raise CustomException(e, sys)