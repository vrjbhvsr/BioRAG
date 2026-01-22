from generation.query_rewrite import QueryRewriter
#from generation.mapping import Mapper
#from generation.reduce import Reducer
from retrieval.parent_retriever import retirever
from config.logging import log
from config.exception import CustomException
import sys
from constants import *
from typing import Optional, Literal
from scripts.Generation import GenerationPipeline

logger = log()
log = logger.get_logger(__name__)

rewriter = QueryRewriter()
#mapper = Mapper()
#reducer = Reducer()

try:
    log.info(
    "\n"
    "=====================================================\n"
    "        🚀Generation PIPELINE STARTED\n"
    "====================================================="
)

    pipeline = GenerationPipeline(rewriter = rewriter,
                                #mapper = mapper,
                                #reducer = reducer
                                )
    
    pipeline.run("Why is electrical stimulation considered relevant for bone regeneration and osteoblast activity?")
    log.info(
    "\n"
    "=====================================================\n"
    "         Generation PIPELINE Finished 🚀\n"
    "====================================================="
)
    
except Exception as e:
    log.error(e)
    raise CustomException(e, sys)
