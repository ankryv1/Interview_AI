import axios from "axios";

const api = axios.create({
    baseURL: import.meta.env.VITE_API_URL,
    withCredentials: true
})

export default api;

// This is the axios instance we created, so anywhere we want to use axios, we
// can directly do like api.post("/login", ..)


//  const api = axios.