import React, { useState } from 'react';
import Navbar from './Navbar';  // Assuming you have a Navbar component
import Footer from './Footer';  // Assuming you have a Footer component
import ExpertiseForm from './ExpertiseForm'; // Your submit form component
import '../App.css'; // CSS for styling

const Submit = () => {
  const [formSubmitted, setFormSubmitted] = useState(false);

  const handleFormSubmit = () => {
    // Logic for form submission can go here
    // For demonstration, we will just set formSubmitted to true
    setFormSubmitted(true);
  };

  return (
    <div className="submit-page">
      <div className="form-container">
        {!formSubmitted ? (
          <>
            <h1>Submit Your Expertise</h1>
            <ExpertiseForm onSubmit={handleFormSubmit} />
          </>
        ) : (
          <div>
            <h2>Thank You!</h2>
            <p>Your expertise has been submitted successfully.</p>
          </div>
        )}
      </div>
    </div>
  );
};

export default Submit;