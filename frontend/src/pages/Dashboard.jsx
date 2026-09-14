
import React from "react";
import { useAuth } from "../context/AuthContext";
import Button from "../components/ui/Button";
import Card from "../components/ui/Card";
import { useNavigate } from "react-router-dom";
import {
  FaCode,
  FaChartLine,
  FaArrowRight,
} from "react-icons/fa";

const Dashboard = () => {
  const { user } = useAuth();
  const navigate = useNavigate();

  const getGreeting = () => {
    const hour = new Date().getHours();

    if (hour < 12) return "Good Morning";
    else if (hour < 18) return "Good Afternoon";

    return "Good Night";
  };

  // Dummy data for now
  const stats = [
    {
      title: "Interviews",
      value: "8",
      icon: <FaCode />,
    },
    {
      title: "Average Score",
      value: "76%",
      icon: <FaChartLine />,
    },
   
  ];

  const recentInterviews = [
    {
      role: "Backend Developer",
      type: "Technical",
      difficulty: "Medium",
      score: 82,
      date: "Sep 12, 2026",
    },
    {
      role: "React Developer",
      type: "Technical",
      difficulty: "Easy",
      score: 74,
      date: "Sep 10, 2026",
    },
    {
      role: "Software Engineer",
      type: "Behavioral",
      difficulty: "Hard",
      score: 68,
      date: "Sep 7, 2026",
    },
  ];

  return (
    <div className="min-h-screen bg-[#080B12] py-12">
      <div className="max-w-6xl mx-auto px-6">

        {/* Header */}
        <div className="flex flex-col md:flex-row md:items-center md:justify-between gap-6">

          <div>
            <h2 className="text-3xl md:text-4xl font-bold text-[#F5F7FA]">
              {`${getGreeting()}, ${user?.username}`}
            </h2>

            <p className="mt-2 text-[#98A2B3] text-2xl">
              Ready for the next interview?
            </p>
          </div>

          <Button
            onClick={() => navigate("/interview/setup")}
          >
            Start New Interview
          </Button>

        </div>


        {/* Stats */}
        <div className="grid grid-cols-1 sm:grid-cols-3 gap-14 mt-10">

          {stats.map((stat) => (
            <Card key={stat.title}>

              <div className="flex items-center justify-between">

                <div>
                  <p className="text-sm text-[#98A2B3]">
                    {stat.title}
                  </p>

                  <p className="text-3xl font-bold text-[#F5F7FA] mt-2">
                    {stat.value}
                  </p>
                </div>

                <div className="w-11 h-11 rounded-lg bg-[#171D2B] text-[#6366F1] flex items-center justify-center text-lg">
                  {stat.icon}
                </div>

              </div>

            </Card>
          ))}

        </div>


        {/* Recent Interviews */}
        <div className="mt-14">

          <div className="flex items-center justify-between mb-6">

            <div>
              <h3 className="text-2xl font-bold text-[#F5F7FA]">
                Recent Interviews
              </h3>

              <p className="text-sm text-[#98A2B3] mt-1">
                Review your previous interview sessions.
              </p>
            </div>

            <button
              className="hidden sm:flex items-center gap-2 text-sm
                         text-[#8B5CF6] hover:text-[#A78BFA] transition"
            >
              View All
              <FaArrowRight className="text-xs" />
            </button>

          </div>


          <div className="space-y-4">

            {recentInterviews.map((interview, index) => (

              <Card key={index}>

                <div className="flex flex-col md:flex-row md:items-center md:justify-between gap-5">

                  {/* Interview info */}
                  <div className="flex items-center gap-4">

                    <div className="w-11 h-11 rounded-lg bg-[#171D2B]
                                    flex items-center justify-center
                                    text-[#6366F1]">
                      <FaCode />
                    </div>

                    <div>
                      <h4 className="font-semibold text-[#F5F7FA]">
                        {interview.role}
                      </h4>

                      <p className="text-sm text-[#98A2B3] mt-1">
                        {interview.type} • {interview.difficulty}
                      </p>
                    </div>

                  </div>


                  {/* Score + date */}
                  <div className="flex items-center justify-between md:justify-end gap-8">

                    <div>
                      <p className="text-xs text-[#98A2B3]">
                        Date
                      </p>

                      <p className="text-sm text-[#F5F7FA] mt-1">
                        {interview.date}
                      </p>
                    </div>

                    <div>
                      <p className="text-xs text-[#98A2B3]">
                        Score
                      </p>

                      <p className="text-lg font-semibold text-[#34D399] mt-1">
                        {interview.score}%
                      </p>
                    </div>

                    <button
                      className="hidden sm:block text-sm text-[#8B5CF6]
                                 hover:text-[#A78BFA] transition"
                    >
                      Report
                    </button>

                  </div>

                </div>

              </Card>

            ))}

          </div>

        </div>


        {/* Bottom CTA */}
        <div className="mt-14 border border-[#20283A] rounded-xl p-8
                        bg-[#0D111C]">

          <div className="flex flex-col md:flex-row md:items-center
                          md:justify-between gap-6">

            <div>
              <h3 className="text-xl font-semibold text-[#F5F7FA]">
                Keep improving your interview skills.
              </h3>

              <p className="text-[#98A2B3] mt-2">
                Start another practice session and see how you perform.
              </p>
            </div>

            <Button
              onClick={() => navigate("/interview/setup")}
            >
              Practice Again
            </Button>

          </div>

        </div>

      </div>
    </div>
  );
};

export default Dashboard;

