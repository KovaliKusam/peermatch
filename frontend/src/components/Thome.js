

// import React from 'react';
// import { useNavigate } from 'react-router-dom';
// import './Thome.css'; // Ensure this CSS file exists
// import Chatbot from './Chatbot';

// const Thome = () => {
//   const navigate = useNavigate();

//   // This is a placeholder for checking if the user is logged in.
//   // You should replace this with your actual authentication logic.
//   const isLoggedIn = false; // Replace with actual authentication check

//   const handleNavigation = (path) => {
//     if (!isLoggedIn) {
//       alert("Please log in or register to access this feature.");
//       navigate('/login'); // Redirect to login page
//     } else {
//       navigate(path);
//     }
//   };

//   return (
//     <div className="home-container">
//       <div className="hero">
//         <h1>ColabMate</h1>
//         <p>Find the right expert at the right time. Seamless, smart, and fast.</p>
//         <div className="home-buttons">
//           <button onClick={() => handleNavigation('/submit')} aria-label="Submit your expertise">Submit Your Expertise</button>
//           <button onClick={() => handleNavigation('/search-expertise')} aria-label="Find an expert">Find an Expert</button> {/* Updated path */}
//         </div>
//       </div>

//       <section className="how-it-works">
//         <h2>How It Works</h2>
//         <ol>
//           <li>Submit your name, email, expertise, and available time.</li>
//           <li>We store your profile and embedding.</li>
//           <li>Others can find you based on expertise and your available time.</li>
//           <li>Start a conversation via Outlook.</li>
//         </ol>
//       </section>

//       <section className="cta-section">
//         <h2>Ready to connect?</h2>
//         <button onClick={() => handleNavigation('/submit')} aria-label="Get started with submitting expertise">Get Started</button>
//       </section>
//       <Chatbot/>
//     </div>
//   );
// };

// export default Thome;
// import React from 'react';
// import { useNavigate } from 'react-router-dom';
// import './Thome.css'; // Ensure this CSS file exists
// import Chatbot from './Chatbot';
// import { useAuth } from '../AuthContext'; // Import useAuth hook

// const Thome = () => {
//   const navigate = useNavigate();
//   const { isAuthenticated } = useAuth(); // Use authentication state from the useAuth hook

//   const handleNavigation = (path) => {
//     if (!isAuthenticated) {
//       alert("Please log in or register to access this feature.");
//       navigate('/login'); // Redirect to login page
//     } else {
//       navigate(path);
//     }
//   };

//   return (
//     <div className="home-container">
//       <div className="hero">
//         <h1>ColabMate</h1>
//         <p>Find the right expert at the right time. Seamless, smart, and fast.</p>
//         <div className="home-buttons">
//           <button onClick={() => handleNavigation('/submit')} aria-label="Submit your expertise">Submit Your Expertise</button>
//           <button onClick={() => handleNavigation('/search-expertise')} aria-label="Find an expert">Find an Expert</button>
//         </div>
//       </div>

//       <section className="how-it-works">
//         <h2>How It Works</h2>
//         <ol>
//           <li>Submit your name, email, expertise, and available time.</li>
//           <li>We store your profile and embedding.</li>
//           <li>Others can find you based on expertise and your available time.</li>
//           <li>Start a conversation via Outlook.</li>
//         </ol>
//       </section>

//       <section className="cta-section">
//         <h2>Ready to connect?</h2>
//         <button onClick={() => handleNavigation('/submit')} aria-label="Get started with submitting expertise">Get Started</button>
//       </section>
//       <Chatbot />
//     </div>
//   );
// };

// export default Thome;

// import React from 'react';
// import { useNavigate } from 'react-router-dom';
// import './Thome.css'; // Ensure this CSS file exists
// import Chatbot from './Chatbot';
// import { useAuth } from '../AuthContext'; // Import useAuth hook

// const Thome = () => {
//   const navigate = useNavigate();
//   const { isAuthenticated } = useAuth(); // Use authentication state from the useAuth hook

//   const handleNavigation = (path) => {
//     if (!isAuthenticated) {
//       alert("Please log in or register to access this feature.");
//       navigate('/login'); // Redirect to login page
//     } else {
//       navigate(path);
//     }
//   };

//   return (
//     <div className="home-container">
//       <div className="hero">
//         <h1>ColabMate</h1>
//         <p>Find the right expert at the right time. Seamless, smart, and fast.</p>
//         <div className="home-buttons">
//           <button onClick={() => handleNavigation('/submit')} aria-label="Submit your expertise">Submit Your Expertise</button>
//           <button onClick={() => handleNavigation('/search-expertise')} aria-label="Find an expert">Find an Expert</button>
//         </div>
//       </div>

//       <section className="how-it-works">
//         <h2>How It Works</h2>
//         <ol>
//           <li>Submit your name, email, expertise, and available time.</li>
//           <li>We store your profile and embedding.</li>
//           <li>Others can find you based on expertise and your available time.</li>
//           <li>Start a conversation via Outlook.</li>
//         </ol>
//       </section>

//       <section className="cta-section">
//         <h2>Ready to connect?</h2>
//         <button onClick={() => handleNavigation('/submit')} aria-label="Get started with submitting expertise">Get Started</button>
//       </section>
//       <Chatbot />
//     </div>
//   );
// };

// export default Thome;

import React from 'react';
import { useNavigate } from 'react-router-dom';
import './Thome.css'; // Ensure this CSS file exists
import Chatbot from './Chatbot';
import { useAuth } from '../AuthContext'; // Import useAuth hook

const Thome = () => {
  const navigate = useNavigate();
  const { isAuthenticated } = useAuth(); // Use authentication state from the useAuth hook

  const handleNavigation = (path) => {
    if (!isAuthenticated) {
      alert("Please log in or register to access this feature.");
      navigate('/login'); // Redirect to login page
    } else {
      navigate(path);
    }
  };

  return (
    <div className="home-container">
      <div className="hero">
        <h1>ColabMate</h1>
        <p>Find the right expert at the right time. Seamless, smart, and fast.</p>
        <div className="home-buttons">
          <button onClick={() => handleNavigation('/submit')} aria-label="Submit your expertise">Submit Your Expertise</button>
          <button onClick={() => handleNavigation('/search-expertise')} aria-label="Find an expert">Find an Expert</button>
        </div>
      </div>

      <section className="how-it-works">
        <h2>How It Works</h2>
        <ol>
          <li>Submit your name, email, expertise, and available time.</li>
          <li>We store your profile and embedding.</li>
          <li>Others can find you based on expertise and your available time.</li>
          <li>Start a conversation via Outlook.</li>
        </ol>
      </section>

      <section className="cta-section">
        <h2>Ready to connect?</h2>
        <button onClick={() => handleNavigation('/submit')} aria-label="Get started with submitting expertise">Get Started</button>
      </section>
      <Chatbot />
    </div>
  );
};

export default Thome;