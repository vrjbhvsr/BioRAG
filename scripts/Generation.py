from generation.query_rewrite import QueryRewriter
from generation.mapping import Mapper
from generation.reduce import Reducer
from generation.deduplication import Deduplication
from config.logging import log
from config.exception import CustomException
import sys
from constants import *
from typing import Optional, Literal
from generation.generation_pipeline import GenerationPipeline
from models.Llama import model

logger = log()
log = logger.get_logger(__name__)

model = model().load()

rewriter = QueryRewriter(model)
deduplicator = Deduplication()
mapper = Mapper(model)
reducer = Reducer(model)

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
                                reducer = reducer
                                )
    
    dedup = pipeline.run(input("Enter Question related to Paper 'Pulsed Electrical Stimulation Affects Osteoblast Adhesion and Calcium Ion Signaling' /n"))
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
