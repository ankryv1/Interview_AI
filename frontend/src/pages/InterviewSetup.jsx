
import React, { useState, useEffect } from "react";
import Card from "../components/ui/Card";
import api from "../services/api";

const InterviewSetup = () => {
  const [allResumes, setAllResumes] = useState([]);
  const [selectedResume, setSelectedResume] = useState(null);

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
              <h2 className="text-xl font-semibold text-white">
                Your Resumes
              </h2>

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
              const isSelected =
                selectedResume === resume.resume_id;

              return (
                <Card
                  key={resume.resume_id}
                  onClick={() =>
                    setSelectedResume(resume.resume_id)
                  }
                  className={`relative cursor-pointer transition-all duration-200
                    ${
                      isSelected
                        ? "border-2 border-orange-400 bg-orange-400/10"
                        : "border border-gray-700 hover:border-gray-500 hover:bg-white/5"
                    }
                  `}
                >
                  <div className="flex items-center gap-4">

                    {/* PDF Icon */}
                    <div
                      className={`w-11 h-11 rounded-lg flex items-center justify-center
                        ${
                          isSelected
                            ? "bg-orange-400/20 text-orange-400"
                            : "bg-gray-700 text-gray-300"
                        }
                      `}
                    >
                      <i className="ri-file-pdf-line text-2xl"></i>
                    </div>

                    {/* Resume Name */}
                    <div className="flex-1 min-w-0">
                      <h3
                        className="text-sm font-medium text-white truncate"
                        title={resume.filename}
                      >
                        {resume.filename}
                      </h3>

                      <p className="text-xs text-gray-500 mt-1">
                        PDF Resume
                      </p>
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

                  <div className="w-11 h-11 rounded-lg bg-orange-400/10
                                  flex items-center justify-center">
                    <i className="ri-upload-cloud-2-line text-2xl text-orange-400"></i>
                  </div>

                  <div>
                    <h3 className="text-sm font-medium text-white">
                      Upload New Resume
                    </h3>

                    <p className="text-xs text-gray-500 mt-1">
                      PDF files only
                    </p>
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
              <i className="ri-checkbox-circle-fill text-orange-400 text-xl"></i>

              <div>
                <p className="text-xs text-gray-500">
                  Selected Resume
                </p>

                <p className="text-sm font-medium text-white">
                  {
                    allResumes.find(
                      (resume) =>
                        resume.resume_id === selectedResume
                    )?.filename
                  }
                </p>
              </div>
            </div>
          </div>
        )}

        {/* Continue Button */}
        <div className="flex justify-end mt-8">
          <button
            disabled={!selectedResume}
            className={`px-6 py-3 rounded-lg font-medium transition-all
              ${
                selectedResume
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