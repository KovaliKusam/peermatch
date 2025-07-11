import React, { useState } from 'react';
import Navbar from './Navbar';  // Assuming you have a Navbar component
import Hero from './Hero';      // Assuming you have a Hero component
import Footer from './Footer';  // Assuming you have a Footer component
import ExpertiseForm from './ExpertiseForm'; // Your submit form component
import SearchExpertiseForm from './SearchExpertiseForm'; // Your search form component
import '../App.css'; // CSS for styling

const MainPage = () => {
  const [showSearchForm, setShowSearchForm] = useState(false);

  const handleFindExpertiseClick = () => {
    setShowSearchForm(true);
  };

  return (
    <div className="main-page">
      <Navbar />
      {/* <Hero /> */}
      <div className="form-container">
        {!showSearchForm ? (
          <>
            <ExpertiseForm />
            <button onClick={handleFindExpertiseClick}>Find Expertise</button>
          </>
        ) : (
          <SearchExpertiseForm />
        )}
      </div>
      <Footer />
    </div>
  );
};

export default MainPage;