from langchain_groq import ChatGroq
from app.config import GROQ_API_KEY

llm = ChatGroq(
        groq_api_key=GROQ_API_KEY,
        model="openai/gpt-oss-20b",
        temperature=0.5
        )

# using different LLMs for different tasks is exactly how many production AI applications ,0.5 in lm as we want a little variation in question
# are built. It makes your project more reliable, faster, and cheaper because you choose 
# the right model for each job instead of forcing one model to do everything

evaluate_llm = ChatGroq(
    groq_api_key=GROQ_API_KEY,
    model="openai/gpt-oss-20b",
    temperature=0
)

report_llm = ChatGroq(
    groq_api_key=GROQ_API_KEY,
    model="openai/gpt-oss-20b",
    temperature=0
)