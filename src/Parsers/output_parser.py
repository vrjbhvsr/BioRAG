from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
from config.logging import log
from config.exception import CustomException
from typing import List, Optional, Union
import sys      

logger = log()
log = logger.get_logger(__name__)

class query_parser(BaseModel):
    queries: List[str] = Field(description="A list of exactly 3 rewritten technical queries.")


class Map_parser(BaseModel):
    relevant: bool = Field(description="Whether the text contains info about the physicochemical properties or biological effects of the stimulation.")
    summary: str = Field(
        description="A single-paragraph summary of 500-700 words containing only the information from the text that directly addresses the user query."
    )

class Metric(BaseModel):
    parameter: Optional[str] = Field(
        default=None,
        description="What was measured, if explicitly stated"
    )
    value: Optional[Union[str, List[str]]] = Field(
        default=None,
        description="Measured value with unit, if available"
    )

class ReduceParser(BaseModel):
    '''is_sufficient: Optional[bool] = Field(
        default=None,
        description="True if data was found."
    )'''

    key_metrics: Optional[List[Metric]] = Field(
        default=None,
        description="Optional list of extracted measurements."
    )

    analysis: str = Field(
        description="The seamless narrative report (no headers) as multiple paragraphs."
    )