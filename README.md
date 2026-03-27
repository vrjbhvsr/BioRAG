# BioRAG

**BioRAG** is a Retrieval-Augmented Generation (RAG) system designed for scientific literature understanding, with a focus on biomedical and cell biology research. It ingests PDF documents, indexes them into a vector store, and answers user queries using a map-reduce generation pipeline powered by Llama 3.1.

## Features

- PDF ingestion with OCR support via `unstructured`
- Section-based document splitting and parent-child chunking
- ChromaDB vector store with NVIDIA embedding model
- Query rewriting for improved retrieval
- Map-reduce generation pipeline with deduplication
- Built with LangChain and LangGraph
- Docker support for containerized deployment

## Project Structure

```
BioRAG/
├── Data/pdfs/                  # Input PDF documents
├── scripts/
│   ├── ingest_documents.py     # Run the ingestion pipeline
│   └── Generation.py           # Run the generation/QA pipeline
├── src/
│   ├── api/                    # API layer (FastAPI schemas)
│   ├── chains/                 # LangChain chains (map, reduce, query rewrite)
│   ├── config/                 # Logging, exception handling, settings
│   ├── constants/              # All configurable constants
│   ├── embeddings/             # Embedding model wrapper
│   ├── generation/             # Generation pipeline (rewrite, map, reduce)
│   ├── ingestion/              # PDF loading, cleaning, splitting pipeline
│   ├── models/                 # Llama model loader and table summariser
│   ├── prompts/                # Prompt templates
│   ├── retrieval/              # Parent-child retriever
│   └── vectorstore/            # ChromaDB client and collections
├── notebooks/                  # Experiment notebooks
├── evaluation/                 # RAG evaluation metrics
├── tests/                      # Unit tests
├── environment.yml             # Conda environment specification
├── Dockerfile                  # Docker image definition
└── pyproject.toml              # Project metadata and build config
```

## Requirements

- Python >= 3.10
- [Conda](https://docs.conda.io/en/latest/) or [Mamba](https://mamba.readthedocs.io/) (recommended)
- Docker (optional, for containerized setup)
- A GPU is recommended for running the Llama 3.1 8B model

## Installation

### Option 1 — Conda/Mamba (Local)

**1. Clone the repository**

```bash
git clone https://github.com/vrjbhvsr/BioRAG.git
cd BioRAG
```

**2. Create and activate the conda environment**

```bash
mamba env create -f environment.yml
conda activate BioRAG
```

**3. Install the package in editable mode**

```bash
pip install -e .
```

### Option 2 — Docker

**1. Build the Docker image**

```bash
docker build -t biorag .
```

**2. Run the container**

```bash
docker run -it --gpus all biorag
```

Inside the container, the conda environment `BioRAG` is automatically activated.

## Configuration

All constants (model names, file paths, chunk sizes, prompts, etc.) are defined in `src/constants/__init__.py`. Update the following before running:

| Constant | Description | Default |
|---|---|---|
| `FILE_PATH` | Path to the input PDF | `Data/pdfs/cells-11-02650-v2.pdf` |
| `MODEL_NAME` | Hugging Face model for generation | `meta-llama/Llama-3.1-8B-Instruct` |
| `EMBEDDING_MODEL_NAME` | Embedding model | `nvidia/llama-embed-nemotron-8b` |
| `CHROMA_PERSIST_DIR` | ChromaDB persistence directory | `chroma_biorag_db` |
| `PARENT_DOCSTORE_PATH` | Parent document store path | `./parent_docstore_biorag` |

> **Note:** The Llama 3.1 model requires a Hugging Face account with access granted. Set your token:
> ```bash
> huggingface-cli login
> ```

## Running the Project

### Step 1 — Ingest Documents

Place your PDF(s) in the `Data/pdfs/` directory, update `FILE_PATH` in `src/constants/__init__.py`, then run:

```bash
cd BioRAG
python scripts/ingest_documents.py
```

This will load, clean, split, embed, and store the document chunks in ChromaDB.

### Step 2 — Run the Generation Pipeline

```bash
python scripts/Generation.py
```

You will be prompted to enter a query:

```
User: What is the effect of electrical stimulation on cell proliferation?
```

The system will rewrite the query, retrieve relevant chunks, run a map-reduce summarisation, and print the final answer.

## Running Tests

```bash
pytest tests/
```

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.

## Author

**Vraj Bhavsar** — [vrajbhavsar377@gmail.com](mailto:vrajbhavsar377@gmail.com)
