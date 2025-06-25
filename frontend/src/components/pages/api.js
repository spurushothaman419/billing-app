import axios from "axios";

const api = axios.create({
  baseURL: "http://localhost:8000",
});

let token = null;

export const setToken = (newToken) => {
  token = newToken;
  api.defaults.headers.common["Authorization"] = `Bearer ${token}`;
};

export default api;
