from chains.query_rewrite_chain import QueryRewriteChain
from config.logging import log
from config.exception import CustomException
import sys

logger = log()
log = logger.get_logger(__name__)

class QueryRewriter:
    """
    A class to handle query rewriting.
    """
    def __init__(self):
        self.chain = QueryRewriteChain().chain()

    def rewrite(self, query: str) -> list[str]:
        """
        Rewrite the given query.

        Args:
            query: The input query string.

        Returns:
            A list of rewritten queries.
        """
        try:
            log.info("Rewriting query...")
            response = self.chain.invoke({"query": query})
            rewritten_queries = response.queries
            log.info("Query rewritten successfully.")
            return rewritten_queries
        except Exception as e:
            log.error("Error rewriting query.")
            raise CustomException(e, sys)