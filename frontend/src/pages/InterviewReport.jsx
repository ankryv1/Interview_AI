import { useState, useEffect } from "react";
import { useLocation, useParams } from "react-router-dom";
import api from "../services/api";

const InterviewReport = () => {
  const { sessionId } = useParams();

  const [report, setReport] = useState(null);

  const location = useLocation();
  const interviewData = location.state?.interviewData;

  const callFullInterview = async () => {
    try {
      const response = await api.get(`/interview/${sessionId}`);
      setReport(response.data.final_report);
    } catch (err) {
      console.error("Error fetching interview data:", err);
    }
  };

  useEffect(() => {
    if (interviewData) {
      setReport(interviewData.final_report);
    } else {
      callFullInterview();
    }
  }, [sessionId, interviewData]);

  if (!report) {
    return (
      <div className="min-h-screen bg-[#0b0e14] text-white flex items-center justify-center">
        <p className="text-gray-400">Loading interview report...</p>
      </div>
    );
  }
return (
  <div className="min-h-screen bg-[#080B12] text-white">
    <div className="max-w-6xl mx-auto px-4 py-10">

      {/* Header */}
      <div className="mb-10">
        <p className="text-sm font-medium text-orange-400 mb-2">
          InterviewAI • Interview Report
        </p>

        <h1 className="text-3xl md:text-4xl font-bold">
          Interview Performance
        </h1>

        <p className="text-slate-400 mt-2">
          Here is a detailed analysis of your interview performance.
        </p>
      </div>


      {/* Overall Score */}
      <div className="grid md:grid-cols-3 gap-6 mb-8">

        <div className="md:col-span-1 rounded-2xl border border-slate-800 bg-[#0E131D] p-6">
          <p className="text-sm text-slate-400 mb-4">
            Overall Rating
          </p>

          <div className="flex items-end gap-2">
            <span className="text-6xl font-bold text-orange-400">
              {report?.overall_rating}
            </span>

            <span className="text-slate-500 mb-2">
              / 100
            </span>
          </div>

          <div className="mt-5 h-2 bg-slate-800 rounded-full overflow-hidden">
            <div
              className="h-full bg-gradient-to-r from-orange-500 to-amber-400 rounded-full"
              style={{
                width: `${report?.overall_rating || 0}%`
              }}
            />
          </div>

          <p className="text-sm text-slate-500 mt-3">
            Overall interview performance
          </p>
        </div>


        {/* Summary */}
        <div className="md:col-span-2 rounded-2xl border border-slate-800 bg-[#0E131D] p-6">
          <p className="text-sm font-semibold text-orange-400 mb-3">
            Overall Summary
          </p>

          <p className="text-slate-300 leading-7">
            {report?.overall_summary}
          </p>
        </div>

      </div>


      {/* Feedback */}
      <div className="grid md:grid-cols-2 gap-6 mb-8">

        {/* Technical */}
        <div className="rounded-2xl border border-slate-800 bg-[#0E131D] p-6">
          <div className="flex items-center gap-3 mb-5">
            <div className="w-10 h-10 rounded-xl bg-blue-500/10 flex items-center justify-center">
              💻
            </div>

            <div>
              <h2 className="font-semibold text-lg">
                Technical Feedback
              </h2>

              <p className="text-xs text-slate-500">
                Technical knowledge & depth
              </p>
            </div>
          </div>

          <p className="text-slate-300 leading-7">
            {report?.technical_feedback}
          </p>
        </div>


        {/* Communication */}
        <div className="rounded-2xl border border-slate-800 bg-[#0E131D] p-6">
          <div className="flex items-center gap-3 mb-5">
            <div className="w-10 h-10 rounded-xl bg-purple-500/10 flex items-center justify-center">
              💬
            </div>

            <div>
              <h2 className="font-semibold text-lg">
                Communication Feedback
              </h2>

              <p className="text-xs text-slate-500">
                Clarity & articulation
              </p>
            </div>
          </div>

          <p className="text-slate-300 leading-7">
            {report?.communication_feedback}
          </p>
        </div>

      </div>


      {/* Strengths + Improvements */}
      <div className="grid md:grid-cols-2 gap-6 mb-8">

        {/* Strengths */}
        <div className="rounded-2xl border border-slate-800 bg-[#0E131D] p-6">

          <h2 className="text-xl font-semibold mb-5">
            Your Strengths
          </h2>

          <div className="space-y-3">
            {report?.strengths?.map((strength, index) => (
              <div
                key={index}
                className="flex items-start gap-3 p-4 rounded-xl bg-emerald-500/5 border border-emerald-500/10"
              >
                <span className="text-emerald-400 text-lg">
                  ✓
                </span>

                <p className="text-slate-300">
                  {strength}
                </p>
              </div>
            ))}
          </div>

        </div>


        {/* Improvements */}
        <div className="rounded-2xl border border-slate-800 bg-[#0E131D] p-6">

          <h2 className="text-xl font-semibold mb-5">
            Areas to Improve
          </h2>

          <div className="space-y-3">
            {report?.improvements?.map((improvement, index) => (
              <div
                key={index}
                className="flex items-start gap-3 p-4 rounded-xl bg-orange-500/5 border border-orange-500/10"
              >
                <span className="text-orange-400 font-semibold">
                  {index + 1}
                </span>

                <p className="text-slate-300">
                  {improvement}
                </p>
              </div>
            ))}
          </div>

        </div>

      </div>


      {/* General Feedback */}
      <div className="rounded-2xl border border-slate-800 bg-[#0E131D] p-6 mb-8">

        <h2 className="text-xl font-semibold mb-4">
          Interviewer Feedback
        </h2>

        <p className="text-slate-300 leading-7">
          {report?.feedback}
        </p>

      </div>


      {/* Final CTA */}
      <div className="rounded-2xl border border-orange-500/20 bg-gradient-to-r from-orange-500/10 to-transparent p-6">

        <h2 className="text-xl font-semibold mb-2">
          Keep Improving 🚀
        </h2>

        <p className="text-white">
          Focus on the improvement areas above and practice explaining
          your technical decisions with concrete examples and metrics.
        </p>

      </div>

    </div>
  </div>
);
};

export default InterviewReport;

