import React from 'react';
import '../App.css'; // CSS for styling

const Navbar = () => {
  return (
    <nav className="navbar">
      <h1>Expertise Finder</h1>
      <ul>
        <li><a href="#home">Home</a></li>
        <li><a href="#about">About</a></li>
        <li><a href="#contact">Contact</a></li>
      </ul>
    </nav>
  );
};

export default Navbar;