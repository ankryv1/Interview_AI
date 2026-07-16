from langchain_chroma import Chroma
from app.rag.embeddings import embedding_model
from app.rag.splitter import text_splitter



vector_store =  Chroma(
        collection_name="resume_collection",
        embedding_function=embedding_model,
        persist_directory="chroma_db"
    )

def add_resume_to_vector_store(resume_id: str, chunks:list[str], user_id: str):
    vector_store.add_texts(texts=chunks, ids=[f"{resume_id}_{i}" for i in range(len(chunks))],
                           metadatas=[{"resume_id": resume_id, "user_id": user_id} for _ in chunks]
                           )

    