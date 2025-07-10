import axios from 'axios';

const BASE_URL = "http://127.0.0.1:8000";

export const submitExpertise = async (data) => {
  try {
    const response = await axios.post(`${BASE_URL}/submit_expertise`, data);
    return response.data;
  } catch (error) {
    console.error("Error submitting expertise:", error);
    throw error;
  }
};

export const fetchExpertise = async (query) => {
  try {
    const response = await axios.post(`${BASE_URL}/find_experts`, {
      query:query
    });
    return response.data;
  } catch (error) {
    console.error("Error fetching expertise:", error);
    throw error;
  }
};