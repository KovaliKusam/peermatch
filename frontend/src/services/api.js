// // import axios from 'axios';

// // const BASE_URL = "http://127.0.0.1:8000";

// // export const submitExpertise = async (data) => {
// //   try {
// //     console.log("In submit expertise");
    
// //     // Ensure all required fields are included in the data object
// //     const response = await axios.post(`${BASE_URL}/submit_expertise`, {
// //       name: data.name,
// //       email: data.email,
// //       expertise: data.expertise,
// //       current_project: data.current_project, // Include current_project
// //       login_time: data.login_time, // Include login_time
// //       logout_time: data.logout_time // Include logout_time
// //     }, {
// //       timeout: 5000
// //     });
    
// //     console.log("Response from API inside submitExpertise:", response.data);
// //     return response.data;
// //   } catch (error) {
// //     console.error("Error submitting expertise:", error);
// //     throw error;
// //   }
// // };

// // export const fetchExpertise = async (query) => {
// //   try {
// //     const response = await axios.post(`${BASE_URL}/find_experts`, {
// //       query: query
// //     });
// //     return response.data;
// //   } catch (error) {
// //     console.error("Error fetching expertise:", error);
// //     throw error;
// //   }
// // };

// import axios from 'axios';

// const BASE_URL = "http://127.0.0.1:8000"; // Ensure this is the correct base URL for your API

// export const submitExpertise = async (data) => {
//   try {
//     console.log("In submit expertise");
    
//     // Ensure all required fields are included in the data object
//     const response = await axios.post(`${BASE_URL}/submit_expertise`, {
//       name: data.name,
//       email: data.email,
//       expertise: data.expertise,
//       current_project: data.current_project, // Include current_project
//       login_time: data.login_time, // Include login_time
//       logout_time: data.logout_time, // Include logout_time
//       timezone: data.timezone // Include timezone if needed
//     }, {
//       timeout: 5000 // Set a timeout for the request
//     });
    
//     console.log("Response from API inside submitExpertise:", response.data);
//     return response.data; // Return the response data
//   } catch (error) {
//     console.error("Error submitting expertise:", error);
//     throw error; // Rethrow the error for further handling
//   }
// };

// export const fetchExpertise = async (query) => {
//   try {
//     const response = await axios.post(`${BASE_URL}/find_experts`, {
//       query: query
//     });
//     return response.data; // Return the response data
//   } catch (error) {
//     console.error("Error fetching expertise:", error);
//     throw error; // Rethrow the error for further handling
//   }
// };

// export const registerUser = async (name, email, password) => {
//   try {
//     const response = await axios.post(`${BASE_URL}/register`, {
//       name,
//       email,
//       password
//     }, {
//       timeout: 5000 // Set a timeout for the request
//     });
    
//     console.log("Response from API inside registerUser:", response.data);
//     return response.data; // Return the response data
//   } catch (error) {
//     console.error("Error registering user:", error);
//     throw error; // Rethrow the error for further handling
//   }
// };

import axios from 'axios';

const BASE_URL = "http://127.0.0.1:8000"; // Ensure this is the correct base URL for your API

export const submitExpertise = async (data) => {
  try {
    console.log("In submit expertise");
    
    // Ensure all required fields are included in the data object
    const response = await axios.post(`${BASE_URL}/submit_expertise`, {
      name: data.name,
      email: data.email,
      expertise: data.expertise,
      current_project: data.current_project, // Include current_project
      login_time: data.login_time, // Include login_time
      logout_time: data.logout_time // Removed timezone
    }, {
      timeout: 5000 // Set a timeout for the request
    });
    
    console.log("Response from API inside submitExpertise:", response.data);
    return response.data; // Return the response data
  } catch (error) {
    console.error("Error submitting expertise:", error);
    throw error; // Rethrow the error for further handling
  }
};

export const fetchExpertise = async (query) => {
  try {
    const response = await axios.post(`${BASE_URL}/find_experts`, {
      query: query
    });
    return response.data; // Return the response data
  } catch (error) {
    console.error("Error fetching expertise:", error);
    throw error; // Rethrow the error for further handling
  }
};

export const registerUser = async (name, email, password) => {
  try {
    const response = await axios.post(`${BASE_URL}/register`, {
      name,
      email,
      password
    }, {
      timeout: 5000 // Set a timeout for the request
    });
    
    console.log("Response from API inside registerUser:", response.data);
    return response.data; // Return the response data
  } catch (error) {
    console.error("Error registering user:", error);
    throw error; // Rethrow the error for further handling
  }
};

// New loginUser function
export const loginUser = async (email, password) => {
  try {
    const response = await axios.post(`${BASE_URL}/login`, {
      email,
      password
    }, {
      timeout: 5000 // Set a timeout for the request
    });
    
    console.log("Response from API inside loginUser:", response.data);
    return response.data; // Return the response data
  } catch (error) {
    console.error("Error logging in:", error);
    throw error; // Rethrow the error for further handling
  }
};