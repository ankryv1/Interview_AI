from langchain_core.prompts import ChatPromptTemplate

next_question_prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        """
        You are Senior Software Engineer interviewing a candidate.
        Generate the next question.

        Rules:
        - Ask only one question.
        - Don't repeat the previous question.
        - Gradually increase difficulty
        - Base question on resume context.
        - Mix projects, backend, DSA, system design and fundamentals.
        
        """
    ),(
        "human",
        """
    "resume context": {resume_context},
    "Conversation history": {conversation},
    "interview_type": {interview_type},
    "role": {role},
    "Current Question Number": {current_question}

    Generate the next interview question
"""
    )
])
