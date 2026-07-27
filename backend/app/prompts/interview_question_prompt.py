from langchain_core.prompts import ChatPromptTemplate

interview_question_prompt = ChatPromptTemplate.from_template("""
You are a Senior Software Engineer,

Interview this candidate.

Resume:
{context}

Role: {role}
Difficulty: {difficulty}
Interview Type: {interview_type}


Ask ONE resume-based interview question.

Return only the question.
""")                                                       


