import { Route, Routes } from "react-router-dom";
import  Landing  from "../pages/Landing";
import  Login  from "../pages/Login";
import  Signup  from "../pages/Signup";
import  Dashboard from "../pages/Dashboard";
import  UploadResume  from "../pages/UploadResume";
import InterviewSetup  from "../pages/InterviewSetup";
import Interview from "../pages/Interview";
import  Report  from "../pages/Report";
import MainLayout from "../components/layout/MainLayout";

export const AppRoutes = () =>{
    return(
    <Routes>
        <Route path="/login" element={<Login />} />
        <Route path="/signup" element={<Signup />} />
        <Route element={<MainLayout/>}>
            <Route path="/" element={<Landing />} />
            <Route path="/dashboard" element={<Dashboard />} />
            <Route path="/upload-resume" element={<UploadResume />} />
            <Route path="/interview/setup" element={<InterviewSetup />} />
            <Route path="/interview/:sessionId" element={<Interview />} />
            <Route path="/report/:sessionId" element={<Report />} />
        </Route>
        
    </Routes>
)
}

//  ye  file sari route definations like Routes, Route hold karegi, then App.jsx will simply render AppRoutes
// keeping it separate makes app easier to maintain 

// AppRoutes.jsx owns what page shows for what URL. As the app grows, AppRoutes.jsx can get nested routes,
//  protected routes, or lazy-loaded pages without ever touching App.jsx.