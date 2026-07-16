from langchain_core.prompts import ChatPromptTemplate

resume_qa_prompt = ChatPromptTemplate.from_template("""
You are an AI assistant.

Answer ONLY from the resume context.

If the answer is not present in the context, say:
"I could not find this information in the resume."

Resume Context:
{context}

Question:
{question}
""")

# Why this file exists
#  This file verifies that the LLM is followintg the resume insted of halluccinating, 
# it is also helping to ddo guadrails , means not answering to questions which are no relevance in resume

# PURPOSE
# User asks a question
#         ↓
# Answer using the resume

# we used ChatPromptTemplate because it turns raw string into structured reusable message template for the chat model

# we will have multiple prompts for different uses like reseume answering prompt ,we cant use this 
# as this will only say llm to answer using the prompt ,but the user has no question9