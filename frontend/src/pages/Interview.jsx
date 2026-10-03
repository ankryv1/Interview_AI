import React, { useState, useEffect } from "react";
import { useParams, useNavigate } from "react-router-dom";
import api from "../services/api";
import Button from "../components/ui/Button";

const Interview = () => {
  const { sessionId } = useParams();
  const navigate = useNavigate();

  const [currentQuestionNo, setCurrentQuestionNo] = useState(1);
  const [currentQuestion, setCurrentQuestion] = useState("");
  const [userAnswer, setUserAnswer] = useState("");
  const [conversation, setConversation] = useState([]);
  const [answerLoading, setAnswerLoading] = useState(false);
  const [interviewData, setInterviewData] = useState(null);

  const getInterview = async (sessionId) => {
    const response = await api.get(`/interview/${sessionId}`);

    const history = response.data?.conversation || [];
    setInterviewData(response?.data)

    setConversation(history);

    if (history.length > 0) {
      const latest = history[history.length - 1];
      setCurrentQuestion(latest.question);
      setCurrentQuestionNo(latest.question_number);
    }
  };

  const handleSubmitAnswer = async () => {
    if (userAnswer.trim() == "") return;

    setAnswerLoading(true);

    const response = await api.post("/interview/answer", {
      session_id: sessionId,
      answer: userAnswer
    });

    setAnswerLoading(false);

    const updatedHistory = response.data?.conversation || [];
    setConversation(updatedHistory);

    if (updatedHistory.length > 0) {
      const latest = updatedHistory[updatedHistory.length - 1];
      setCurrentQuestion(latest.question);
      setCurrentQuestionNo(latest.question_number);
    }

    setUserAnswer("");

    const stage = response?.data?.stage;
    if(stage === "COMPLETED"){
      navigate(`/report/${sessionId}`,{ state: { interviewData: response?.data }});
    }
    console.log(response);
  };

  useEffect(() => {
    getInterview(sessionId);
  }, [sessionId]);

  const previousQAs = conversation.slice(0, conversation.length - 1);

  return (
    <div className="min-h-screen bg-[#0b0e14] text-white">
      <div className="max-w-4xl mx-auto px-4 py-10 md:px-6">

        {/* Header */}
        <div className="mb-8">
          <span className="inline-block text-xs font-semibold tracking-wide text-orange-400 bg-orange-400/10 px-2.5 py-1 rounded-md mb-3">
            InterviewAI
          </span>

          <div className="flex flex-wrap items-center gap-6">
            <h1 className="text-2xl md:text-3xl font-bold text-white">
              {interviewData?.role || "Interview"}
            </h1>
            {interviewData?.interview_type && (
              <span className="text-s font-medium text-sky-300 bg-sky-700/10 border border-sky-500/20 px-3 py-3 rounded-full">
                {interviewData.interview_type} round
              </span>
            )}
          </div>

          <p className="text-gray-400 mt-2 text-sm">
            Answer each question carefully — your responses are evaluated by the AI interviewer.
          </p>
        </div>

        {/* Previous Questions */}
        {previousQAs.length > 0 && (
          <div className="space-y-4 mb-10">
            <h2 className="text-sm font-semibold text-gray-400 uppercase tracking-wide">
              Previous questions
            </h2>

            {previousQAs.map((item, index) => (
              <div key={index} className="rounded-xl border border-gray-800 bg-[#131722] p-5">
                <div className="flex items-center justify-between mb-3">
                  <span className="inline-flex items-center gap-1.5 text-xs font-medium text-orange-300 bg-orange-400/10 px-2.5 py-1 rounded-full">
                    Q{item.question_number || index + 1}
                  </span>

                  {item.is_follow_up && (
                    <span className="text-xs font-medium text-violet-300 bg-violet-500/10 px-2.5 py-1 rounded-full">
                      Follow-up
                    </span>
                  )}
                </div>

                <p className="text-base text-white leading-relaxed mb-4">
                  {item.question}
                </p>

                <div className="rounded-lg bg-[#0b0e14] border-l-2 border-emerald-500/40 p-3.5">
                  <p className="text-[11px] uppercase tracking-wide text-emerald-400/80 font-semibold mb-1.5">
                    Your answer
                  </p>
                  <p className="text-sm text-gray-300 leading-relaxed whitespace-pre-wrap">
                    {item.answer}
                  </p>
                </div>
              </div>
            ))}
          </div>
        )}

        {/* Current Question */}
        <div className="rounded-xl border border-orange-400/30 bg-[#131722] shadow-lg shadow-orange-500/5">
          <div className="flex items-center gap-3 px-5 py-4 border-b border-gray-800">
            <div className="flex h-9 w-9 shrink-0 items-center justify-center rounded-full bg-orange-400 text-black font-bold text-sm">
              {currentQuestionNo}
            </div>
            <div>
              <p className="text-sm font-semibold text-white">Current question</p>
              <p className="text-xs text-gray-500">Take your time to answer</p>
            </div>
          </div>

          <div className="px-5 py-6">
            <h2 className="text-xl md:text-2xl font-semibold leading-relaxed text-white">
              {currentQuestion}
            </h2>

            <div className="mt-7">
              <label htmlFor="answer" className="block text-sm font-medium text-gray-300 mb-2">
                Your answer
              </label>
              <input
                name="answer"
                type="text"
                value={userAnswer}
                onChange={(e) => {
                  setUserAnswer(e.target.value);
                }}
                placeholder="Type your answer here..."
                className="w-full rounded-lg border border-gray-700 bg-[#0b0e14] px-4 py-3 text-white placeholder:text-gray-600 focus:outline-none focus:border-sky-400 focus:ring-1 focus:ring-sky-400"
              />
            </div>

            <div className="mt-5 flex justify-end">
              <Button
                disabled={answerLoading || !userAnswer.trim()}
                onClick={() => {
                  handleSubmitAnswer();
                }}
              >
                {answerLoading ? "Submitting..." : "Submit Answer"}
              </Button>
            </div>
          </div>
        </div>

        <p className="mt-5 text-center text-xs text-gray-600">
          Make your answer specific and explain your reasoning where possible.
        </p>
      </div>
    </div>
  );
};

export default Interview;