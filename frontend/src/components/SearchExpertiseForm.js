import React, { useState } from 'react';
import { fetchExpertise } from '../services/api'; // Ensure this is the correct import
import './ExpertiseForm.css';

const SearchExpertiseForm = () => {
  const [searchData, setSearchData] = useState({ name: '' });
  const [expertiseDetails, setExpertiseDetails] = useState([]);
  const [message, setMessage] = useState('');

  const handleChange = (e) => {
    setSearchData({ ...searchData, [e.target.name]: e.target.value });
  };

  const handleSearch = async (e) => {
    e.preventDefault();
    try {
      const data = await fetchExpertise(searchData.name);
      setExpertiseDetails(data);
      setMessage('');
    } catch (err) {
      setMessage("No expertise found for this user.");
      setExpertiseDetails([]);
    }
  };

  return (
    <div className="search-expertise-container" style={{ paddingBottom: '145px' }}> {/* Corrected inline style */}
      <form className="search-expertise-form" onSubmit={handleSearch}>
        <h2>Search Expertise</h2>
        <input
          name="name"
          type="text"
          placeholder="Enter Name"
          value={searchData.name}
          onChange={handleChange}
          required
        />
        <button type="submit">Search</button>
      </form>
      {message && <p className="message">{message}</p>}
      {expertiseDetails.length > 0 ? (
        <div className="expertise-details">
          <h3>Expertise Details:</h3>
          {expertiseDetails.map((expert, index) => (
            <div key={index}>
              <p><strong>Name:</strong> {expert.name}</p>
              <p><strong>Email:</strong> {expert.email}</p>
              <p><strong>Expertise:</strong> {expert.expertise}</p>
              <p><strong>Similarity:</strong> {expert.similarity}</p>
            </div>
          ))}
        </div>
      ) : (
        <p style={{'textAlign': 'center'}}>No expertise found for this user.</p>
      )}
    </div>
  );
};

export default SearchExpertiseForm;