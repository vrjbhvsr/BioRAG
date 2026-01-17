from langchain_chroma import Chroma
from langgraph.store.memory import InMemoryStore
from langchain_classic.retrievers import ParentDocumentRetriever
from config.logging import log
from config.exception import CustomException
from constants import *
import sys
from vectorstore.collections import BIORAG_COLLECTION, BIORAG_COLLECTION_METADATA
from embeddings.embedder import embedder

logger = log()  
log = logger.get_logger(__name__)

class chroma_client:
    """
    A client for interacting with the Chroma vector store.
    """

    def __init__(self):
        self.embedder = embedder().get_embeddings()
        
    def store(self):
        """
        Initialize the Chroma client with the specified settings.
        """
        try:
            log.info("Initializing Chroma client...")
            self.client = Chroma(
                persist_directory=CHROMA_PERSIST_DIR,
                embedding_function=self.embedder,
                collection_name=BIORAG_COLLECTION,
                metadata=BIORAG_COLLECTION_METADATA,
                in_memory_store=InMemoryStore()
            )
            log.info("Chroma client initialized successfully.")
        except Exception as e:
            log.error("Error initializing Chroma client.")
            raise CustomException(e, sys)