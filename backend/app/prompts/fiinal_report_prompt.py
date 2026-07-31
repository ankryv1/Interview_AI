from langchain_core.prompts import ChatPromptTemplate

final_report_prompt = ChatPromptTemplate.from_template(
        """You are an expert technical interviewer.

Your task is to analyze the complete interview.

Candidate Resume:
{resume_context}

Role:
{role}

Interview Type:
{interview_type}

Interview Conversation:
{conversation}

Evaluate the candidate on:

- Technical correctness
- Depth of knowledge
- Communication skills
- Confidence
- Overall performance

Return ONLY the structured report.

Do NOT include markdown.
Do NOT explain your reasoning.
Do NOT write any text outside the schema.

          """
    
)
