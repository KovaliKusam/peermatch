import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Navbar from './components/Navbar'; // Import the Navbar component
import Thome from './components/Thome'; // Main home component
import Submit from './components/Submit'; // Import the Submit component
import SearchExpertiseForm from './components/SearchExpertiseForm'; // Import the SearchExpertise component
import Footer from './components/Footer'; // Import the Footer component (if needed)

const App = () => {
  return (
    <Router>
      <div>
        <Navbar />
        <Routes>
          <Route path="/" element={<Thome />} /> {/* Route for the home page */}
          <Route path="/submit" element={<Submit />} /> {/* Route for the Submit component */}
          <Route path="/search-expertise" element={<SearchExpertiseForm />} /> {/* Route for SearchExpertise component */}
        </Routes>
        <Footer /> {/* Optional: If you want a footer on all pages */}
      </div>
    </Router>
  );
};

export default App;