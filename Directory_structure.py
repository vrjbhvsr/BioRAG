import os
from pathlib import Path
from typing import List


directories = [
    "src/api",
    "src/ingestion",
    "src/ingestion/loader",
    "src/ingestion/preprocess",
    "src/ingestion/splitting",
    "src/ingestion/enrichment",
    "src/retrieval",
    "src/chains",
    "src/embeddings",
    "src/vectorstore",
    "src/prompts",
    "src/config",
    "evaluation",
    "tests/ingestion",
    "tests/retrieval",
    "notebooks",
    "scripts"
]

files = [
    # API
    "src/api/__init__.py",
    "src/api/main.py",
    "src/api/schemas.py",

    # Ingestion
    "src/ingestion/__init__.py",
    "src/ingestion/pipeline.py",
    "src/ingestion/loader/__init__.py",
    "src/ingestion/loader/base.py",
    "src/ingestion/preprocess/__init__.py",
    "src/ingestion/preprocess/cleaner.py",
    "src/ingestion/splitting/__init__.py",
    "src/ingestion/splitting/semantic.py",
    "src/ingestion/enrichment/__init__.py",
    "src/ingestion/enrichment/table_summary.py",

    # Retrieval
    "src/retrieval/__init__.py",
    "src/retrieval/parent_retriever.py",

    # Chains
    "src/chains/__init__.py",
    "src/chains/map_chain.py",
    "src/chains/reduce_chain.py",
    "src/chains/rag_chain.py",

    # Embeddings
    "src/embeddings/__init__.py",
    "src/embeddings/embedder.py",

    # Vectorstore
    "src/vectorstore/__init__.py",
    "src/vectorstore/chroma_client.py",
    "src/vectorstore/collections.py",

    # Prompts
    "src/prompts/__init__.py",
    "src/prompts/map_prompt.py",
    "src/prompts/reduce_prompt.py",

    # Config
    "src/config/__init__.py",
    "src/config/settings.py",
    "src/config/logging.py",

    # Evaluation
    "evaluation/rag_metrics.py",

    # Tests
    "tests/test_parity.py",

    # Scripts
    "scripts/ingest_documents.py",


    # Root files
    "pyproject.toml"
]

# Create directories
for dir_path in directories:
    os.makedirs(dir_path, exist_ok=True)

# Create files
for file_path in files:
    open(file_path, 'a').close()
