"""
A vectro stre is a system designed to store and retireve data represented as numerical vectors.

Key Features
1. Storage - Ensures that vectors and their associated metadta are retained whether in 
memory for quick lookups or on-disk for durability and large scale use.

2. Similarity Search - Helps retieve the vectors most similar to a query vector

3. Indexing - Provides a data structure or method that enables fast similarity searches on 
high-dimensional vectors(e.g. approximate nearest neighbor looking).

4. CRUD Operations - manage the lifecycyle of data- adding new vectors, reading them, updating 
existing entries, removing outdated vectors.

Use-Cases
1. Semantic Search
2. RAG
3. Recommender Systems
4. Image/Multimedia Search

Vectore store vs Vector Database

Vector Store
- Typically refers to a lightweight library or service that foucses on storing vectors (embeddings) and performing similarity search.
- May not include many traditional database features like transactions, rich query languages, or role based acecess control.
- Ideal for prototyping, smaller scale applications.
- Examples: FAISS (where you store vectors and can query them by similarity but handle persisitence and sclaing separately).

Vector Database.
- A full-fledged database system designed to store and query vectors.

Offers additional "database-like" features..
    - Destributed architecture for horizonatal scaling.
    -Durability and persistence (replication, backup/restore)
    - Metadata Handling(schemas, filters)
    - Pontential for ACID or near-ACID guarantees.
    - Authentiication/authorization and more advance security.
"""

"""
Vector Stores in LangChain 

Supported stores : langchain integrates with multiple vector stores(FAISS, Phinecone, Chroma, Quadrand, Weaviate, etc.),
giving you flexibility in scale, features, and deployment.

Common Interfaces: A uniform Vector store API lets you swap out one backent (e.g. FAISS) for another.

Metadata Handling: Most vector stores in Langchain allow yo to attach metadata.
"""

"""
Chroma Vector Store
Chorma is a lightweight, open source vector database that is especially friendly for local development and 
small to medium scale production needs.
"""

