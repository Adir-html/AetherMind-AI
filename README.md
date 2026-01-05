AetherMind — A Modular, Extensible RAG Framework
AetherMind is a fully modular Retrieval‑Augmented Generation (RAG) backend built from scratch.
It’s designed for clarity, extensibility, and real‑world engineering practices — with pluggable vectorstores, interchangeable embedding backends, clean retrieval orchestration, and a memory system supporting both short‑term and long‑term context.

This project demonstrates how to build a production‑grade RAG pipeline without relying on monolithic frameworks.

🚀 Features
Core Pipeline
Ingestion pipeline: preprocessing, chunking, embedding, vectorstore upsert

Retriever with vector search, scoring, and optional reranking

Memory system with short‑term FIFO memory and long‑term persistent memory

Embedding backends including SentenceTransformers and an OpenAI‑compatible interface

Vectorstores including an in‑memory Chroma‑like store, Pinecone adapter, and Qdrant adapter

FastAPI server with clean routing and shared state

CI pipeline using GitHub Actions

Full test suite for embeddings, vectorstore, and retriever

🧩 Architecture Overview
Ingest flow:
Preprocess → Chunking → Embeddings → Vectorstore → Long‑term Memory

Query flow:
Embeddings → Retriever → Memory Context → Response Assembly

The retriever merges vectorstore hits with both short‑term and long‑term memory to produce a final context set.

📦 Installation
Clone the repository, install dependencies, and ensure SentenceTransformers is available.
No external API keys are required unless you choose to enable OpenAI embeddings.

🏃 Running the API
Start the FastAPI server using Uvicorn.
The API root is available at localhost:8000, and interactive documentation is available at /docs.

📥 Ingesting Text
Send a POST request to the /ingest endpoint with text or a file path.
You can configure chunk size, overlap, and whether to persist long‑term memory.

🔍 Querying
Send a POST request to /query with a natural‑language question.
The response includes:

Retrieved chunks

Similarity scores

Short‑term memory context

Long‑term memory context

🧪 Tests
A full pytest suite validates:

Embedding backend behavior

Vectorstore operations

Retriever orchestration

🔄 CI Pipeline
GitHub Actions automatically runs tests on every push and pull request.
The workflow installs dependencies, runs pytest, and caches packages for faster builds.

🧠 Project Goals
AetherMind is built to be:

Readable — small, focused modules

Extensible — pluggable components at every layer

Tested — reliable behavior across the pipeline

Practical — real embeddings, real retrieval, real memory

Ideal for:

Chatbots

Document QA

Personal knowledge bases

Research assistants

RAG experimentation

📌 Roadmap
Evaluation module (retrieval quality, hallucination checks)

Optional frontend (chat UI + file upload)

Vectorstore persistence layer

Reranking improvements (cross‑encoder)

LLM synthesis layer (answer generation)
