import axios from "axios";

const api = axios.create({
    baseURL: "http://localhost:8000",
    withCredentials: true
})

export default api;

// This is the axios instance we created, so anywhere we want to use axios, we
// can directly do like api.post("/login", ..)


//  condt api = axios.