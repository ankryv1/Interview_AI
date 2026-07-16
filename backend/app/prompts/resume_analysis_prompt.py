from langchain_core.prompts import ChatPromptTemplate

resume_analysis_prompt = ChatPromptTemplate.from_template("""
You are a experienced technical recruiter,
Analyse the candidate's resume.

Resume Context:
 {context}

Return your answer in following format:

```json
{{
    "experience": [list of experience],
    "education": [list of education],
    "Resume Score": 0-100,
    "Technical Skills": [list of skills]  ,
    "Missing Skills": [list of skills],
    "Strengths": [list of strengths],
    "Weaknesses": [List of weaknesses],
    Suggestions for Improvement: [list of suggestions]                                                                                                                                                                                                                                                                                                                       
}}
```                                                                                                                                                                                                                              
""")
