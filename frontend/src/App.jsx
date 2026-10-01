import React from "react";
import { Toaster } from "react-hot-toast";
import { AppRoutes } from "./routes/AppRoutes";

const App = () => {
  return (
    <>
      <Toaster
        position="top-right"
        toastOptions={{
          style: {
            background: "#1e293b",
            color: "#fff",
            border: "1px solid #334155",
          },
        }}
      />
      <AppRoutes />
    </>
  );
};

export default App;
