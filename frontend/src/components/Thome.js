import React from 'react';
import { useNavigate } from 'react-router-dom';
import './Thome.css'; // Ensure this CSS file exists

const Thome = () => {
  const navigate = useNavigate();

  return (
    <div className="home-container">
      <section className="hero">
        <h1>PeerCanvas</h1>
        <p>Find the right expert at the right time. Seamless, smart, and fast.</p>
        <div className="home-buttons">
          <button onClick={() => navigate('/submit')} aria-label="Submit your expertise">Submit Your Expertise</button>
          <button onClick={() => navigate('/search-expertise')} aria-label="Find an expert">Find an Expert</button> {/* Updated path */}
        </div>
      </section>

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
        <button onClick={() => navigate('/submit')} aria-label="Get started with submitting expertise">Get Started</button>
      </section>
    </div>
  );
};

export default Thome;