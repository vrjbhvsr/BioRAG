from ingestion.loader.base import BaseLoader
from langchain_community.document_loaders import UnstructuredPDFLoader
from config.logging import log
from config.exception import CustomException
from pathlib import Path
from constants import *
import sys
import os 

logger = log()
log = logger.get_logger(__name__)

class PDFLoader(BaseLoader):
    os.environ["TESSDATA_PREFIX"] = "/opt/conda/share/tessdata"
    def __init__(self, path: str | Path):
        self.path = path

    def load(self):
        """This function will load the Langchain's UnstructuredPDFLoader.
        """
        try:
        
            if isinstance(self.path, str):
                self.path = Path(self.path)
            loader = UnstructuredPDFLoader(self.path,
                                          ocr_languages = OCR_LANGUAGES,
                                          mode = MODE,
                                          strategy = STRATEGY,
                                          infer_table_structure = INFER_TABLE_STRUCTURE)
            return loader.load()
        except Exception as e:
            log.error(e)
            raise CustomException(e,sys)



    
    