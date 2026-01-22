from retrieval.parent_retriever import retriever
from config.logging import log
from config.exception import CustomException
import sys
from constants import *
from typing import Optional, Literal

logger = log()
log = logger.get_logger(__name__)

class Deduplication:
    """A class to handle deduplication of retrieved documents."""
    def __init__(self):
        self.retriever = retriever().get_retriever()
        self.retrieved_chunks = []
        self.deduplicated_chunks = {}

    def deduplicate(self, list_of_queries: list[str]) -> list[str]:
        """Deduplicate the given list of documents.

        Args:
            documents: A list of document strings.

        Returns:
            A list of deduplicated document strings.
        """
        try:
            log.info("Starting deduplication process...")
            for query in list_of_queries:
                log.info(f"Retrieving documents for query: {query}")
                relevent_docs = self.retriever.invoke(query)
                self.retrieved_chunks.extend(relevent_docs)
            
            for chunk in self.retrieved_chunks:
                doc_id = chunk.metadata.get('document_id')
                self.deduplicated_chunks[doc_id] = chunk
            log.info(f"Deduplication completed. Reduced from {len(self.retrieved_chunks)} to {len(self.deduplicated_chunks)} documents.")
            return list(self.deduplicated_chunks.values())
        except Exception as e:
            log.error("Error during deduplication process.")
            raise CustomException(e, sys)
