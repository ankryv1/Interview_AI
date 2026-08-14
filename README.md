 the interview flow itself instead of hardcoading in python  we will use langgraph like , langgraph will control the interview

  React
      │
   FastAPI
      │
  Interview Graph
      │
 ┌──────────────┐
 │Generate Ques │
 └──────────────┘
        │
        ▼
 ┌──────────────┐
 │Wait Answer   │
 └──────────────┘
        │
        ▼
 ┌──────────────┐
 │Evaluate      │
 └──────────────┘
        │
        ▼
 Is Followup?
    /      \
  Yes      No
   │        │
   ▼        ▼
Followup  Next Question
             │
             ▼
     Interview Finished?
         │
      Yes ▼
    Final Report


##   The Overall Architecture ,how the rerquest Flows in the Backend Part is

                MongoDB
                    │
                    ▼
            InterviewSession
                    │
                    ▼
      answer_interview_service
                    │
          Build InterviewState
                    │
                    ▼
            LangGraph Workflow
                    │
                    ▼
            Updated InterviewState
                    │
                    ▼
      Copy values back to Session
                    │
                    ▼
              await session.save()
                    │
                    ▼
                API Response

   
