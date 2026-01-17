from config.logging import log
from config.exception import CustomException
from transformers import AutoTokenizer
import sys
from constants import *
from langchain_text_splitters import RecursiveCharacterTextSplitter


logger = log()
log = logger.get_logger(__name__)

class chunking:
    """
    A class for chunking documents into smaller parts.
    """
    def __init__(self):
        self.tokenizer = AutoTokenizer.from_pretrained(EMBEDDING_MODEL_NAME)

    def _token_length(self, text: str) -> int:
        """
        Calculate the token length of the input text.

        Args:
            text (str): The input text.

        Returns:
            int: The token length of the text.
        """
        try:
            log.info("Calculating token length...")
            
            token_length = len(self.tokenizer.encode(text, add_special_tokens=False))
            log.info(f"Token length calculated: {token_length}")
            return token_length
        except Exception as e:
            log.error("Error calculating token length.")
            raise CustomException(e, sys)

    def parent_splitter(self, text: str,) -> list:
        """
        Chunk the input text into smaller parts.

        Returns:
            list: A list of text chunks.
        """
        try:
            log.info("Starting Parent chunking...")
            Parent_text_splitter = RecursiveCharacterTextSplitter(
                chunk_size= PARENT_CHUNK_SIZE,
                chunk_overlap= PARENT_CHUNK_OVERLAP,
                length_function=self._token_length,
                separators=SEPARATORS,
                add_start_index= ADD_START_INDEX,
            )

            log.info("Parent chunking completed successfully.")
            return Parent_text_splitter
        except Exception as e:
            log.error("Error during text chunking.")
            raise CustomException(e, sys)
        
    def child_splitter(self) -> list:
        """
        Chunk the input text into smaller parts.

        Returns:
            list: A list of text chunks.
        """
        try:
            log.info("Starting Child chunking...")
            Child_text_splitter = RecursiveCharacterTextSplitter(
                chunk_size= CHILD_CHUNK_SIZE,
                chunk_overlap= CHILD_CHUNK_OVERLAP,
                length_function=self._token_length,
                add_start_index= ADD_START_INDEX,
            )

            log.info("Child chunking completed successfully.")
            return Child_text_splitter
        
        except Exception as e:
            log.error("Error during text chunking.")
            raise CustomException(e, sys)