import React, { useState } from 'react';
import { submitExpertise } from '../services/api';
import './ExpertiseForm.css';

const ExpertiseForm = () => {
  const [formData, setFormData] = useState({
    name: '',
    email: '',
    expertise: '',
    current_project: '', // Added this field
    login_time: '',
    logout_time: ''
  });

  const [message, setMessage] = useState('');

  const handleChange = e => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const handleSubmit = async e => {
    e.preventDefault();
    console.log("Form submitted!");
    
    // Prepare data for submission
    const data = {
      name: formData.name,
      email: formData.email,
      expertise: formData.expertise,
      current_project: formData.current_project, // Added this line
      login_time: `${formData.login_time}:00`,  // Keep as HH:MM:SS format
      logout_time: `${formData.logout_time}:00`  // Keep as HH:MM:SS format
    };
    console.log("Data to submit:", data);
    try {
      console.log("Sending request to API...");
      const response = await submitExpertise(data);
      console.log("Response from API:", response); // Log the response
      alert("Submitted successfully!");
    } catch (err) {
      console.error("Error submitting expertise:", err); // Log the error
      alert("Something went wrong!");
    }
  };

  return (
    <form className="expertise-form" onSubmit={handleSubmit}>
      <h2>Submit Your Expertise</h2>
      <input 
        name="name" 
        type="text" 
        placeholder="Name" 
        value={formData.name} 
        onChange={handleChange} 
        required 
      />
      <input 
        name="email" 
        type="email" 
        placeholder="Email" 
        value={formData.email} 
        onChange={handleChange} 
        required 
      />
      <textarea 
        name="expertise" 
        placeholder="Your expertise..." 
        value={formData.expertise} 
        onChange={handleChange} 
        required 
      />
      <input 
        name="current_project" 
        type="text" // Assuming current_project is a text field
        placeholder="Current Project" 
        value={formData.current_project} 
        onChange={handleChange} 
        required 
      />
      <input 
        name="login_time" 
        type="time" 
        placeholder="Login Time" 
        value={formData.login_time} 
        onChange={handleChange} 
        required 
      />
      <input 
        name="logout_time" 
        type="time" 
        placeholder="Logout Time" 
        value={formData.logout_time} 
        onChange={handleChange} 
        required 
      />
      <button type="submit">Submit</button>
      {message && <p className="message">{message}</p>}
    </form>
  );
};

export default ExpertiseForm;