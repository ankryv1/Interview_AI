import { useNavigate} from "react-router-dom";

import Navbar from "../components/layout/Navbar";
import Footer from "../components/layout/Footer";
import Container from "../components/layout/Container";
import Button from "../components/ui/Button";
import Card from "../components/ui/Card";
import { FaFileAlt, FaMicrophone, FaRobot, FaChartBar } from "react-icons/fa";

export default function Landing() {

  const navigate = useNavigate();

  return (
    <>
      {/*  HERO section */}
      <section className="bg-[#080B12]">
        <Container className="py-24 text-center">
          <h1 className="text-5xl md:text-6xl font-bold leading-tight">
            <span className="text-[#8B5CF6]">Ace</span>{" "}
            <span className="bg-red-600 px-3 pb-4 rounded-full text-6xl font-semibold mx-1 align-middle text-[#F5F7FA]">
              Your
            </span>{" "}
            <span className='text-orange-300 italic '>TECHNICAL</span>  <span className="text-[#A78BFA]">Interviews</span>
          </h1>

          <p className="mt-6 text-lg text-[#98A2B3] max-w-2xl mx-auto">
            Practice resume-based mock interviews powered by AI, receive instant
            feedback, and improve your confidence.
          </p>

          <div className="mt-10 flex justify-center gap-4 flex-wrap">
            <Button className="text-2xl" onClick={()=> navigate("/signup")}>Start Interview</Button>

            <Button variant="outline">Upload Resume</Button>
          </div>
        </Container>
      </section>

      {/* Feature Section */}
      <section className="py-20 bg-[#0D111C]">
        <Container>
          <div className="bg-orange-900 px-10 py-4 rounded-4xl w-fit mx-auto">
            <h2 className="text-4xl font-bold text-center text-[#F5F7FA]">
              Why Choose InterviewAI?
            </h2>
          </div>

          <p className="text-center text-[#98A2B3] mt-4">
            Everything you need to prepare for your next interview.
          </p>

          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6 mt-14">
            <Card>
              <FaFileAlt className="text-4xl text-[#6366F1] mb-4" />

              <h3 className="font-bold text-xl text-[#A78BFA]">
                Resume Analysis
              </h3>

              <p className="text-[#98A2B3] mt-2">
                Upload your resume and receive interview questions tailored to
                your experience.
              </p>
            </Card>

            <Card>
              <FaMicrophone className="text-4xl text-[#6366F1] mb-4" />

              <h3 className="font-bold text-xl text-[#22D3EE]">
                Voice Interview
              </h3>

              <p className="text-[#98A2B3] mt-2">
                Practice realistic AI voice interviews with natural
                conversations.
              </p>
            </Card>

            <Card>
              <FaRobot className="text-4xl text-[#6366F1] mb-4" />

              <h3 className="font-bold text-xl text-[#34D399]">
                AI Feedback
              </h3>

              <p className="text-[#98A2B3] mt-2">
                Get detailed feedback on your technical answers and
                communication.
              </p>
            </Card>

            <Card>
              <FaChartBar className="text-4xl text-[#6366F1] mb-4" />

              <h3 className="font-bold text-xl text-[#F59E0B]">
                Performance Reports
              </h3>

              <p className="text-[#98A2B3] mt-2">
                Track your interview progress and identify areas for
                improvement.
              </p>
            </Card>
          </div>
        </Container>
      </section>

      {/* How to use Section */}

      <section className="py-24 bg-[#080B12]">
        <Container>
          <h2 className="text-4xl font-bold text-center text-[#F5F7FA]">
            How It Works
          </h2>

          <p className="text-[#98A2B3] text-center mt-4">
            Prepare for your dream job in four simple steps.
          </p>

          <div className="mt-16 grid grid-cols-1 md:grid-cols-4 gap-8">
            <div className="text-center">
              <div className="w-16 h-16 bg-[#6366F1] rounded-full text-white flex items-center justify-center text-2xl font-bold mx-auto">
                1
              </div>

              <h3 className="mt-6 font-bold text-xl text-[#F5F7FA]">
                Upload Resume
              </h3>

              <p className="text-[#98A2B3] mt-2">
                Upload your resume so the AI understands your background.
              </p>
            </div>

            <div className="text-center">
              <div className="w-16 h-16 bg-[#6366F1] rounded-full text-white flex items-center justify-center text-2xl font-bold mx-auto">
                2
              </div>

              <h3 className="mt-6 font-bold text-xl text-[#F5F7FA]">
                Configure Interview
              </h3>

              <p className="text-[#98A2B3] mt-2">
                Choose your role, difficulty, and interview type.
              </p>
            </div>

            <div className="text-center">
              <div className="w-16 h-16 bg-[#6366F1] rounded-full text-white flex items-center justify-center text-2xl font-bold mx-auto">
                3
              </div>

              <h3 className="mt-6 font-bold text-xl text-[#F5F7FA]">
                Answer Questions
              </h3>

              <p className="text-[#98A2B3] mt-2">
                Respond to AI-generated questions through text or voice.
              </p>
            </div>

            <div className="text-center">
              <div className="w-16 h-16 bg-[#6366F1] rounded-full text-white flex items-center justify-center text-2xl font-bold mx-auto">
                4
              </div>

              <h3 className="mt-6 font-bold text-xl text-[#F5F7FA]">
                Get Your Report
              </h3>

              <p className="text-[#98A2B3] mt-2">
                Receive detailed feedback and actionable improvement tips.
              </p>
            </div>
          </div>
        </Container>
      </section>

      <section className="py-24 bg-[#0D111C]">
        <Container>
          <div className="text-center">

            <h2 className="text-4xl md:text-5xl font-bold text-[#F5F7FA]">
              Ready to Ace Your Next Interview?
            </h2>

            <p className="mt-6 text-lg text-[#98A2B3] max-w-2xl mx-auto">
              Practice with AI-powered mock interviews and get
              personalized feedback to improve your performance.
            </p>

            <div className="mt-10">
              <Button
                onClick={() => navigate("/signup")}
                className="hover:bg-[#F5F7FA] hover:text-[#080B12]"
              >
                Get Started
              </Button>
            </div>

          </div>
        </Container>
      </section>

    </>
  );
}

