from models.base import BaseModelLoader
from config.logging import log
from langchain_core.runnables.base import RunnableBinding
from config.exception import CustomException
from langchain_huggingface.llms import HuggingFacePipeline
from transformers import AutoTokenizer, pipeline
from constants import *
from dotenv import load_dotenv
import sys

logger = log()
log = logger.get_logger(__name__)
# defining environment variable
load_dotenv()


class model(BaseModelLoader):
    """
    A model loader for table summarization tasks.
    """
    def __init__(self):
        self.model_name = MODEL_NAME
        self.tokenizer = AutoTokenizer.from_pretrained(self.model_name)
        

    def load(self) -> HuggingFacePipeline:
        """
        Load the table summarization model.

        Returns:
            HuggingFacePipeline: A runnable binding for the table summarization model.
        """
        try:
            # Placeholder for actual model loading logic
            log.info("Loading model...")
            pipe = pipeline("text-generation",
                    tokenizer=self.tokenizer,
                   model= self.model_name,

                   )
            model_pipe = HuggingFacePipeline(pipeline=pipe)
            #model = model_pipe.bind(skip_prompt = SKIP_PROMPT)
            log.info("model loaded successfully.")
            return model_pipe
        except Exception as e:
            log.error("Error loading table summarization model.")
            raise CustomException(e, sys)

