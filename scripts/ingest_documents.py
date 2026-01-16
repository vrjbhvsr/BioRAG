from ingestion.loader.pdfloader import PDFLoader
from ingestion.pipeline import IngestionPipeline
from config.logging import log
from config.exception import CustomException
from constants import *
import sys


logger = log()
log = logger.get_logger(__name__)

loader = PDFLoader(FILE_PATH)
try:
    log.info(
    "\n"
    "=====================================================\n"
    "        🚀 DATA INGESTION PIPELINE STARTED\n"
    "====================================================="
)

    pipeline = IngestionPipeline(loader = loader,)
    pipeline.run()
    
except Exception as e:
    log.error(e)
    raise CustomException(e, sys)
