from models.base import BaseModelLoader
from config.logging import log
from langchain_core.runnables.base import RunnableBinding
from config.exception import CustomException
from langchain_huggingface.llms import HuggingFacePipeline
from transformers import AutoTokenizer, pipeline, AutoModelForCausalLM
from constants import *
from dotenv import load_dotenv
import sys

logger = log()
log = logger.get_logger(__name__)
# defining environment variable
load_dotenv()


class table_summarizer(BaseModelLoader):
    """
    A model loader for table summarization tasks.
    """
    def __init__(self):
        self.model_name = MODEL_NAME
        self.tokenizer = AutoTokenizer.from_pretrained(self.model_name)
        

    def load(self) -> RunnableBinding:
        """
        Load the table summarization model.

        Returns:
            RunnableBinding: A runnable binding for the table summarization model.
        """
        try:
            # Placeholder for actual model loading logic
            log.info("Loading table summarization model...")
            pipe = pipeline("text-generation",
                    tokenizer=self.tokenizer,
                   model= self.model_name,
                    device_map = DEVICE_MAP,
                    dtype = DTYPE,
                    max_new_tokens=MAX_NEW_TOKENS,   
                    do_sample=DO_SAMPLE,
                   )
            model_pipe = HuggingFacePipeline(pipeline=pipe)
            model = model_pipe.bind(skip_prompt = SKIP_PROMPT)
            log.info("Table summarization model loaded successfully.")
            return model
        except Exception as e:
            log.error("Error loading table summarization model.")
            raise CustomException(e, sys)

