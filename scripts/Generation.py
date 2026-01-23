from generation.query_rewrite import QueryRewriter
from generation.mapping import Mapper
#from generation.reduce import Reducer
from generation.deduplication import Deduplication
from config.logging import log
from config.exception import CustomException
import sys
from constants import *
from typing import Optional, Literal
from generation.generation_pipeline import GenerationPipeline

logger = log()
log = logger.get_logger(__name__)

rewriter = QueryRewriter()
deduplicator = Deduplication()
mapper = Mapper()
#reducer = Reducer()

try:
    log.info(
    "\n"
    "=====================================================\n"
    "        🚀Generation PIPELINE STARTED\n"
    "====================================================="
)

    pipeline = GenerationPipeline(rewriter = rewriter,
                                deduplicator = deduplicator,
                                mapper = mapper,
                                #reducer = reducer
                                )
    
    dedup = pipeline.run("In the Materials and Methods section, how is the IonOptix electrical stimulation chamber described, including electrode material, geometry, and well configuration?")
    print(dedup)
    log.info(
    "\n"
    "=====================================================\n"
    "         Generation PIPELINE Finished 🚀\n"
    "====================================================="
)
    
except Exception as e:
    log.error(e)
    raise CustomException(e, sys)
