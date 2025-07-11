import axios from 'axios';

const BASE_URL = "http://127.0.0.1:8000";

export const submitExpertise = async (data) => {
  try {
    console.log("In submit expertise")
    // Ensure login_time and logout_time are included in the data object
    const response = await axios.post(`${BASE_URL}/submit_expertise`, {
      name: data.name,
      email: data.email,
      expertise: data.expertise,
      login_time: data.login_time, // Include login_time
      logout_time: data.logout_time // Include logout_time
    }, {
      timeout: 5000
    });
    console.log("Response from API inside submitExpertise:", response.data);
    return response.data;
  } catch (error) {
    console.error("Error submitting expertise:", error);
    throw error;
  }
};

export const fetchExpertise = async (query) => {
  try {
    const response = await axios.post(`${BASE_URL}/find_experts`, {
      query: query
    });
    return response.data;
  } catch (error) {
    console.error("Error fetching expertise:", error);
    throw error;
  }
};