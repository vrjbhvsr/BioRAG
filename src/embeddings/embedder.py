from langchain_huggingface import HuggingFaceEmbeddings
from config.logging import log
from config.exception import CustomException
from constants import *
import sys  

logger = log()
log = logger.get_logger(__name__)

class embedder:
    """
    A class to create embeddings using HuggingFace models.
    """
    def __init__(self):
        """
        Initialize the embedder with the specified model.

        Args:
            model_name (str): The name of the HuggingFace model to use for embeddings.
        """
        self.model_name = EMBEDDING_MODEL_NAME

    def get_embeddings(self) -> HuggingFaceEmbeddings:
        """
        Create and return the HuggingFace embeddings.

        Returns:
            HuggingFaceEmbeddings: The embeddings object.
        """
        try:
            log.info(f"Creating embeddings using model: {self.model_name}")
            embeddings = HuggingFaceEmbeddings(model_name=self.model_name,
                                                model_kwargs={"device": EMBEDDING_DEVICE, "trust_remote_code": TRUST_REMOTE_CODE})
            log.info("Embeddings created successfully.")
            return embeddings
        except Exception as e:
            log.error("Error creating embeddings.")
            raise CustomException(e, sys)