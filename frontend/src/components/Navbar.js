import React from 'react';
import '../App.css'; // CSS for styling

const Navbar = () => {
  return (
    <nav className="navbar">
      <h1>Expertise Finder</h1>
      <ul>
        <li><a href="#contact">Profile</a></li>
      </ul>
    </nav>
  );
};

export default Navbar;