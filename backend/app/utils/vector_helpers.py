from app.rag.vector_store import vector_store

def get_resume_context(resume_id: str, question: str,k: int =3):
    retriever = vector_store.as_retriever(
        search_kwargs= {"k": k, "filter": {"resume_id": resume_id}}
    )

    docs = retriever.invoke(question)

    context = "\n\n".join(doc.page_content for doc in docs)

    return context

#  ye fn us question ke according database se chunks fetch krke return marta hai