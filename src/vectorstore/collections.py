BIORAG_COLLECTION = "biorag_documents"

BIORAG_COLLECTION_METADATA = {
    "description": "Biomedical documents with table summaries and semantic chunks",
    "domain": "biomedical",
    "chunking": "semantic",
    "enrichment": ["table_summary"],
    "embedding_model": "llama-embeddings",
}
