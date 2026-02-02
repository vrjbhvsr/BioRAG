from chains.map_chain import map_chain
from config.logging import log
from config.exception import CustomException
import sys
from constants import *
from typing import List
from langchain_core.documents import Document

logger = log()
log = logger.get_logger(__name__)

class Mapper:
    """
    A class to handle the mapping process using the map chain.
    """
    def __init__(self, model):
        self.map_chain = map_chain(model).chain()
        

    def map(self, queries: List[str], documents: List[Document]) -> str:
        """
        Maps the input queries using the map chain.

        Args:
            queries (list): A list of queries to be mapped.

        Returns:
            list: A list of mapped responses.
        """
        inputs = [
                    {
                        "user_query": q,
                        "text_chunk": [doc.page_content for doc in documents]
                    }
                    for q in queries
]
        try:
            log.info("Starting mapping process...")
            mapped_responses = self.map_chain.batch(inputs, config = {"max_concurrency": MAX_CONCURRENCY})
            log.info("Mapping process completed successfully.")
            return mapped_responses
        except Exception as e:
            log.error("Error during mapping process.")
            raise CustomException(e, sys)