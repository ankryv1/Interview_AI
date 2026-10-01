import React, { useState, useEffect} from "react";
import { useNavigate } from "react-router-dom";
import Card from "../components/ui/Card";
import api from "../services/api";

const InterviewSetup = () => {
  const [allResumes, setAllResumes] = useState([]);
  const [selectedResume, setSelectedResume] = useState(null);
  const [targetRole, setTargetRole] = useState("");
  const [interviewType, setInterviewType] = useState(null);
  const [noOfQues, setNoOfQues] = useState(0);
  const [difficulty, setDifficulty] = useState(null);

  const navigate = useNavigate();

  const handleUpload = async (e) => {
    const file = e.target.files[0];

    if (!file) return;

    const formData = new FormData();
    formData.append("file", file);

    try {
      const response = await api.post("/resume/upload", formData);

      const newResume = response.data;

      // Add uploaded resume to the list
      setAllResumes((prevResumes) => [...prevResumes, newResume]);

      // Automatically select uploaded resume
      setSelectedResume(newResume.resume_id);
    } catch (err) {
      console.error("Error uploading resume:", err);
    }

    // Allows selecting the same file again
    e.target.value = "";
  };

  const getAllResumes = async () => {
    try {
      const response = await api.get("/resume/all");
      setAllResumes(response.data);
    } catch (err) {
      console.error("Error fetching resumes:", err);
    }
  };

  useEffect(() => {
    getAllResumes();
  }, []);

  const handleSubmitForm= async()=>{
     try{
       const response = await api.post("/interview/start",{
           resume_id: selectedResume,
           role: targetRole,
           interview_type: interviewType,
           total_questions: noOfQues,
           difficulty
        })
        // console.log(response);

        const session_id = response.data.session_id
        navigate(`/interview/${session_id}`);
     } catch(err){
        console.log(err);
     }
  }

  const isFormCompleted = selectedResume && targetRole?.trim() && interviewType && noOfQues > 0 && difficulty;

  return (
    <div className="min-h-screen p-6 md:p-10">
      {/* Header */}
      <div className="max-w-5xl mx-auto mb-8">
        <h1 className="text-3xl md:text-4xl font-bold text-white mb-2">
          Configure Your Interview
        </h1>

        <p className="text-gray-400">
          Select a resume to personalize your interview, or upload a new one.
        </p>
      </div>

      <div className="max-w-5xl mx-auto">
        {/* Existing Resumes */}
        <div className="mb-8">
          <div className="flex items-center justify-between mb-4">
            <div>
              <h2 className="text-xl font-semibold text-white">Your Resumes</h2>

              <p className="text-sm text-gray-400 mt-1">
                Choose the resume you want to use
              </p>
            </div>

            <span className="text-sm text-gray-400">
              {allResumes.length} resume{allResumes.length !== 1 && "s"}
            </span>
          </div>

          <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-4">
            {allResumes.map((resume) => {
              const isSelected = selectedResume === resume.resume_id;

              return (
                <Card
                  key={resume.resume_id}
                  onClick={() => setSelectedResume(resume.resume_id)}
                  className={`relative cursor-pointer transition-all duration-200
                    ${
                      isSelected
                        ? "border-2 border-orange-400 bg-orange-400/10"
                        : "border border-gray-700 hover:border-gray-500 hover:bg-white/5"
                    }
                  `}
                >
                  <div className="flex items-center gap-4">
                    {/* Resume Name */}
                    <div className="flex-1 min-w-0">
                      <h3
                        className="text-sm font-medium text-white truncate"
                        title={resume.filename}
                      >
                        {resume.filename}
                      </h3>

                      <p className="text-xs text-gray-500 mt-1">PDF Resume</p>
                    </div>

                    {/* Selected Indicator */}
                    {isSelected && (
                      <div className="w-6 h-6 rounded-full bg-orange-400 flex items-center justify-center">
                        <i className="ri-check-line text-black text-sm"></i>
                      </div>
                    )}
                  </div>
                </Card>
              );
            })}

            {/* Upload New Resume */}
            <label className="cursor-pointer">
              <Card
                className="h-full min-h-[90px] border-2 border-dashed border-gray-700
                           hover:border-orange-400 hover:bg-orange-400/5
                           transition-all duration-200"
              >
                <div className="flex items-center gap-4 h-full">
                  <div
                    className="w-11 h-11 rounded-lg bg-orange-400/10
                                  flex items-center justify-center"
                  >
                    <i className="ri-upload-cloud-2-line text-2xl text-orange-400"></i>
                  </div>

                  <div>
                    <h3 className="text-sm font-medium text-white">
                      Upload New Resume
                    </h3>

                    <p className="text-xs text-gray-500 mt-1">PDF files only</p>
                  </div>
                </div>

                <input
                  type="file"
                  accept=".pdf"
                  onChange={handleUpload}
                  className="hidden"
                />
              </Card>
            </label>
          </div>
        </div>

        {/* Selected Resume */}
        {selectedResume && (
          <div className="mt-8 p-4 rounded-xl border border-orange-400/30 bg-orange-400/5">
            <div className="flex items-center gap-3">
              <i className="ri-checkbox-circle-fill text-yellow-400 text-xl"></i>

              <div>
                <p className="text-xs text-gray-500">Selected Resume</p>

                <p className="text-sm font-medium text-white">
                  {
                    allResumes.find(
                      (resume) => resume.resume_id === selectedResume,
                    )?.filename
                  }
                </p>
              </div>
            </div>
          </div>
        )}

        {/* Other Questions */}

        <div className="flex flex-col gap-4 m-4">
          <h1 className="ring-2 rounded-xl p-3 w-fit bg-pink-900 text-[16px] sm:text-xl">
            Your Target Role
          </h1>
          <h2>What role are you preparing for?</h2>
          <input
            type="text"
            value={targetRole}
            onChange={(e) => setTargetRole(e.target.value)}
            placeholder="Role"
            className="w-[60%] p-4 rounded-lg bg-[#121826] border border-gray-400 text-white focus:outline-none focus:border-orange-400"
          />
          <h2 className="">Select Popular Roles</h2>
          <div className="flex flex-row gap-4 cursor-pointer flex-wrap">
            {[
              "Backend Developer",
              "Frontend Developer",
              "Full Stack Developer",
              "Data Engineer",
              "Software Engineer",
            ].map((role) => {
              const isSelected = role === targetRole;
              return (
                <Card
                  key={role}
                  onClick={() => setTargetRole(role)}
                  className={`${isSelected ? "border-2 border-white" : "border-2 border-gray-600"}`}
                >
                  {role}
                </Card>
              );
            })}
          </div>
        </div>

        <div className="flex flex-col gap-4 mt-10">
          <h1 className="ring-2 rounded-xl p-3 w-fit bg-pink-900 text-xl">
            Select Interview Type
          </h1>
          <div className="flex flex-row gap-4 text-white flex-wrap">
            {["Technical", "Behavioural", "HR"].map((type) => (
              <Card
                key={type}
                onClick={() => {
                  setInterviewType(type);
                  console.log(interviewType);
                }}
                className={`${type === interviewType ? "border-2 border-amber-300" : "border-2 border-gray-400 hover:border-gray-500"}`}
              >
                {type}
              </Card>
            ))}
          </div>
        </div>
<div className="mt-8 sm:mt-10">

  {/* Number of Questions */}
  <div className="flex flex-col gap-5">
    <h1 className="w-fit rounded-xl bg-pink-900 px-4 py-3 text-lg sm:text-xl font-semibold text-white ring-1 ring-pink-500/40 shadow-lg">
      Choose No. of Questions
    </h1>

    <div className="grid grid-cols-2 sm:grid-cols-4 gap-3 sm:gap-5 p-2 sm:p-4">
      {[3, 5, 8, 10].map((no) => (
        <Card
          key={no}
          onClick={() => setNoOfQues(no)}
          className={`

            flex items-center justify-center
            min-h-[70px] sm:min-h-[85px]
            rounded-2xl
            cursor-pointer
            text-xl sm:text-2xl
            font-bold
            transition-all duration-200
            select-none

            ${
              no === noOfQues
                ? "border-2 border-amber-300 bg-amber-300/10 text-amber-200 shadow-[0_0_20px_rgba(252,211,77,0.15)] scale-[1.02]"
                : "border border-gray-600 bg-gray-900/60 text-gray-200 hover:border-gray-400 hover:bg-gray-800 hover:scale-[1.02]"
            }
          `}
        >
          {no}
        </Card>
      ))}
    </div>
  </div>


  {/* Difficulty */}
  <div className="flex flex-col gap-5 mt-10 sm:mt-12">

    <h1 className="w-fit rounded-xl bg-pink-900 px-4 py-3 text-lg sm:text-xl font-semibold text-white ring-1 ring-pink-500/40 shadow-lg">
      Choose Difficulty Level
    </h1>

    <div className="grid grid-cols-1 sm:grid-cols-3 gap-3 sm:gap-5 p-2 sm:p-4">

      {["Easy", "Medium", "Hard"].map((level) => (
        <Card
          key={level}
          onClick={() => setDifficulty(level)}
          className={`

            flex items-center justify-center
            min-h-[70px] sm:min-h-[85px]
            rounded-2xl
            cursor-pointer
            text-lg sm:text-xl
            font-semibold
            transition-all duration-200
            select-none

            ${
              level === difficulty
                ? "border-2 border-amber-300 bg-amber-300/10 text-amber-200 shadow-[0_0_20px_rgba(252,211,77,0.15)] scale-[1.02]"
                : "border border-gray-600 bg-gray-900/60 text-gray-200 hover:border-gray-400 hover:bg-gray-800 hover:scale-[1.02]"
            }
          `}
        >
          {level}
        </Card>
      ))}

    </div>
  </div>
</div>
        {/* Continue Button */}
        <div className="flex justify-end mt-8">
          <button
            disabled={!isFormCompleted}
            onClick = {() => handleSubmitForm()}
            className={`px-6 py-3 rounded-lg font-medium transition-all
              ${
                isFormCompleted
                  ? "bg-orange-400 text-black hover:bg-orange-300"
                  : "bg-gray-700 text-gray-500 cursor-not-allowed"
              }
            `}
          >
            Continue
            <i className="ri-arrow-right-line ml-2"></i>
          </button>
        </div>
      </div>
    </div>
  );
};

export default InterviewSetup;

//  Old  UI

// import React, { useState, useEffect } from "react";

// import Card from "../components/ui/Card";

// import api from "../services/api";

// const InterviewSetup = () => {

//   const [allResumes, setAllResumes] = useState([]);

//   const [selectedResume, setSelectedResume] = useState(null);

//   const handleUpload =async (*e*) => {

//     console.log(*e*)

//     const file = *e*.target.files[0];

//     if (!file)  return;

//     const formData = new FormData();

//     formData.append("file",file);

//     try{

//       const response = await api.post("/resume/upload", formData)

//       console.log("uploaded successfully", response)

//       const newResume = response.data;

//       setSelectedResume(newResume.resume\_id)

//       setAllResumes(*prevResumes* => [...*prevResumes*, newResume])

//     }  catch(err){

//       console.error("Error uploading resume:", err);

//     }

//   };

//   const getAllResumes = async () => {

//     const response = await api.get("/resume/all");

//     setAllResumes(response.data);

//   };

//   *//  to use allResumes, we can't do map as it is objec,not array , so we can use Object.entries to convert it into array of key value pairs and then we can map over it*

//   useEffect(() => {

//     getAllResumes();

//   }, []);

//   return (

//     \<div className="flex flex-col gap-4 p-6">

//       \<h1>Configure Your Interview and Let's Get Started!\</h1>

//        {*/\* here display and select existing resume \*/*}

//       \<h2>Select the Existing resume or start with a new one\</h2>

//       \<div className="flex flex-row flex-wrap gap-4 mb-4 items-stretch">

//         {allResumes.map((*resume*) => (

//           \<Card

//             key={*resume*.resume\_id}

//             onClick={() => {setSelectedResume(*resume*.resume\_id); console.log(*resume*.resume\_id)}}

//             className={\`cursor-pointer ${selectedResume === *resume*.resume\_id ? "border-2 border-orange-400": "border-gray-200"}\`}

//           >

//             \<h1 className="text-[14px] text-white">{*resume*.filename}\</h1>

//           \</Card>

//         ))}

//       \</div>

//     {*/\*    select the new resume \*/*}

//       \<Card clasName="flex flex-row gap-2 items-center justify-center cursor-pointer">

//         \<input type="file"  accept=".pdf" onChange={(*e*)=> handleUpload(*e*)}/>

//         \<h1 className="text-xl text-white">Upload new Resume\</h1>

//       \</Card>

//     \</div>

//   );

// };

// export default InterviewSetup;
// make its ui better
