from langchain_core.prompts import ChatPromptTemplate

followup_prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        """"
        You are senior Software Engineer,
        You are interviewing a candidate.
        Ask a concise follow-up question that helps the candidates improve or clarify the previous question.

        Rules:
        - Ask only one follow-up on the same topic.
        - Keep it under 40 words.
        - return only the interview question
        """
    ),
    (
        "human",
        """
        Previous Question:
        {question}
        Candidate answer:
        {answer}
        Feedback:
        {feedback}

        Generate only one follow-up question
        """)
])
