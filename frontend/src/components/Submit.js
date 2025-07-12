import React, { useState } from 'react';
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