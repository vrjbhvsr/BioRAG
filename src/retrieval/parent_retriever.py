from config.logging import log
from config.exception import CustomException
import sys
from lanchain_classic.storage import LocalFileStore, create_kv_docstore
from langchain_classic.retrievers import ParentDocumentRetriever
from vectorstore.chroma_client import chroma_client
from langchain_community.docstore import InMemoryDocstore
from langchain_core.stores import InMemoryByteStore
from ingestion.splitting.chunking import chunking
from langchain_core.documents import Document
from typing import List
from constants import *

logger = log()
log = logger.get_logger(__name__)

class retirever:
    """
    A retriever that fetches parent documents from the Chroma vector store.
    """
    def __init__(self):
        try:
            log.info("Initializing Chroma client for retriever...")
            self.chroma = chroma_client()
            self.store = self.chroma.store()
            file_store = LocalFileStore(PARENT_DOCSTORE_PATH)
            self.docstore = create_kv_docstore(file_store,
                                              byte_store=InMemoryByteStore(),
                                              in_memory_docstore=InMemoryDocstore())
            self.parent_splitter = chunking().parent_splitter()
            self.child_splitter = chunking().child_splitter()
            log.info("Chroma client initialized successfully for retriever.")
        except Exception as e:
            log.error("Error initializing Chroma client for retriever.")
            raise CustomException(e, sys)

    def create_retriever(self) -> ParentDocumentRetriever:
        """
        Create and return a ParentDocumentRetriever instance.

        Returns:
            ParentDocumentRetriever: The retriever instance.
        """
        try:
            log.info("Creating ParentDocumentRetriever...")
            retriever = ParentDocumentRetriever(vectorstore=self.store,
                                                docstore=self.docstore,
                                                parent_splitter=self.parent_splitter,
                                                child_splitter=self.child_splitter,
                                                search_kwargs={"k": 3})
            log.info("ParentDocumentRetriever created successfully.")
            return retriever
        except Exception as e:
            log.error("Error creating ParentDocumentRetriever.")
            raise CustomException(e, sys)
        
    def sync_docs(self, documents: List[Document]) -> None:
        """
        Sync documents to the vector store.

        Args:
            documents (List[Document]): The list of documents to sync.
        """
        try:
            log.info("Syncing documents to the vector store...")
            retirever = self.create_retriever()
            retirever.add_documents(documents)
            log.info("Documents synced successfully.")
        except Exception as e:
            log.error("Error syncing documents to the vector store.")
            raise CustomException(e, sys)

    def get_retriever(self,  documents: List[Document]) -> ParentDocumentRetriever:
        """
        Get the ParentDocumentRetriever instance.

        Returns:
            ParentDocumentRetriever: The retriever instance.
        """
        try:
            log.info("Creating ParentDocumentRetriever...")
            retriever = self.create_retriever()
            log.info("ParentDocumentRetriever created successfully.")
            return retriever
        except Exception as e:
            log.error("Error creating ParentDocumentRetriever.")
            raise CustomException(e, sys)