from app.rag.vector_store import vector_store

retriever = vector_store.as_retriever( search_kwargs ={"k":3, "filter":{"resume_id": resume_id}})

docs = retriever.invoke("What is name of programs does the candidate have experience in?")

for doc in docs:
    print(doc.page_content)
