from langchain_core.prompts import ChatPromptTemplate

evaluation_prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        """
Evaluate the candidate's answer.

Give:
- score
- feedback
- one improvement
- whether a follow-up is needed
"""
    ),
    (
        "human",
        """
Question:
{question}

Answer:
{answer}
"""
    )
])