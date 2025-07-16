// import React, { useState } from 'react';
// import { submitExpertise } from '../services/api'; // Ensure this path is correct
// import './ExpertiseForm.css';

// const timezones = [
//   "Asia/Kolkata", "Asia/Tokyo", "Asia/Dubai", "Europe/London", "Europe/Berlin",
//   "America/New_York", "America/Chicago", "America/Los_Angeles", "Australia/Sydney"
// ];

// const ExpertiseForm = () => {
//   const [formData, setFormData] = useState({
//     name: '',
//     email: '',
//     expertise: '',
//     current_project: '',
//     login_time: '',
//     logout_time: '',
//     timezone: Intl.DateTimeFormat().resolvedOptions().timeZone || 'UTC' // auto-detect
//   });

//   const [message, setMessage] = useState('');

//   const handleChange = e => {
//     setFormData({ ...formData, [e.target.name]: e.target.value });
//   };

//   const handleSubmit = async e => {
//     e.preventDefault();
//     console.log("Form submitted!");

//     const data = {
//       name: formData.name,
//       email: formData.email,
//       expertise: formData.expertise,
//       current_project: formData.current_project,
//       login_time: `${formData.login_time}:00`, // Append seconds
//       logout_time: `${formData.logout_time}:00`, // Append seconds
//       timezone: formData.timezone
//     };

//     console.log("Data to submit:", data);
//     try {
//       const response = await submitExpertise(data); // Call the submitExpertise function
//       console.log("Response from API:", response);
//       setMessage("Submitted successfully!"); // Update message state
//     } catch (err) {
//       console.error("Error submitting expertise:", err);
//       setMessage("Something went wrong!"); // Update message state
//     }
//   };

//   return (
//     <form className="expertise-form" onSubmit={handleSubmit}>
//       <h2>Submit Your Expertise</h2>
//       <input name="name" type="text" placeholder="Name" value={formData.name} onChange={handleChange} required />
//       <input name="email" type="email" placeholder="Email" value={formData.email} onChange={handleChange} required />
//       <textarea name="expertise" placeholder="Your expertise..." value={formData.expertise} onChange={handleChange} required />
//       <input name="current_project" type="text" placeholder="Current Project" value={formData.current_project} onChange={handleChange} required />
//       <input name="login_time" type="time" value={formData.login_time} onChange={handleChange} required />
//       <input name="logout_time" type="time" value={formData.logout_time} onChange={handleChange} required />
      
//       <select name="timezone" value={formData.timezone} onChange={handleChange} required>
//         {timezones.map(tz => (
//           <option key={tz} value={tz}>{tz}</option>
//         ))}
//       </select>

//       <button type="submit">Submit</button>
//       {message && <p className="message">{message}</p>}
//     </form>
//   );
// };

// export default ExpertiseForm;

import React, { useState } from 'react';
import { submitExpertise } from '../services/api'; // Ensure this path is correct
import './ExpertiseForm.css';

const ExpertiseForm = () => {
  const [formData, setFormData] = useState({
    name: '',
    email: '',
    expertise: '',
    current_project: '',
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

    const data = {
      name: formData.name,
      email: formData.email,
      expertise: formData.expertise,
      current_project: formData.current_project,
      login_time: `${formData.login_time}:00`, // Append seconds
      logout_time: `${formData.logout_time}:00` // Append seconds
    };

    console.log("Data to submit:", data);
    try {
      const response = await submitExpertise(data); // Call the submitExpertise function
      console.log("Response from API:", response);
      setMessage("Submitted successfully!"); // Update message state
    } catch (err) {
      console.error("Error submitting expertise:", err);
      setMessage("Something went wrong!"); // Update message state
    }
  };

  return (
    <form className="expertise-form" onSubmit={handleSubmit}>
      <h2>Submit Your Expertise</h2>
      <input name="name" type="text" placeholder="Name" value={formData.name} onChange={handleChange} required />
      <input name="email" type="email" placeholder="Email" value={formData.email} onChange={handleChange} required />
      <textarea name="expertise" placeholder="Your expertise..." value={formData.expertise} onChange={handleChange} required />
      <input name="current_project" type="text" placeholder="Current Project" value={formData.current_project} onChange={handleChange} required />
      <input name="login_time" type="time" value={formData.login_time} onChange={handleChange} required />
      <input name="logout_time" type="time" value={formData.logout_time} onChange={handleChange} required />

      <button type="submit">Submit</button>
      {message && <p className="message">{message}</p>}
    </form>
  );
};

export default ExpertiseForm;