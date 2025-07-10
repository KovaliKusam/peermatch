import React, { useState } from 'react';
import { submitExpertise } from '../services/api';
import './ExpertiseForm.css';

const ExpertiseForm = () => {
  const [formData, setFormData] = useState({
    name: '',
    email: '',
    expertise: ''
  });

  const [message, setMessage] = useState('');

  const handleChange = e => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const handleSubmit = async e => {
    e.preventDefault();
    const data = { name: formData.name, email: formData.email, expertise: formData.expertise};
    try {
      await submitExpertise(data);
      alert("Submitted successfully!");
    } catch (err) {
      alert("Something went wrong!");
    }
  };

  return (
    <form className="expertise-form" onSubmit={handleSubmit}>
      <h2>Submit Your Expertise</h2>
      <input name="name" type="text" placeholder="Name" value={formData.name} onChange={handleChange} required />
      <input name="email" type="email" placeholder="Email" value={formData.email} onChange={handleChange} required />
      <textarea name="expertise" placeholder="Your expertise..." value={formData.expertise} onChange={handleChange} required />
      <button type="submit">Submit</button>
      {message && <p className="message">{message}</p>}
    </form>
  );
};

export default ExpertiseForm;
