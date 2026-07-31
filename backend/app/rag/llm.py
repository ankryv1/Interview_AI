from langchain_groq import ChatGroq
from app.config import GROQ_API_KEY

llm = ChatGroq(
        groq_api_key=GROQ_API_KEY,
        model="llama-3.1-8b-instant",
        temperature=0
        )

# using different LLMs for different tasks is exactly how many production AI applications 
# are built. It makes your project more reliable, faster, and cheaper because you choose 
# the right model for each job instead of forcing one model to do everything

evaluate_llm = ChatGroq(
    groq_api_key=GROQ_API_KEY,
    model="llama-3.3-70b-versatile"
)

report_llm = ChatGroq(
    groq_api_key=GROQ_API_KEY,
    model="llama-3.3-70b-versatile",
    temperature=0
)