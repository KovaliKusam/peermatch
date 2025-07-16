import React from 'react';
import Navbar from './Navbar';  // Assuming you have a Navbar component
import Hero from './Hero';      // Assuming you have a Hero component
import Footer from './Footer';  // Assuming you have a Footer component
import SearchExpertiseForm from './SearchExpertiseForm'; // Your form component
import '../App.css'; // CSS for styling
import Chatbot from './Chatbot';
const HomePage = () => {
  return (
    <div className="home-page">
     
      {/* <Hero /> */}
      <div className="form-container">
        <SearchExpertiseForm />
      </div>
      <Chatbot/>
      <Footer />
    </div>
  );
};

export default HomePage;