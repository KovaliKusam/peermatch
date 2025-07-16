// import React from 'react';
// import '../App.css'; // CSS for styling

// const Navbar = () => {
//   return (
//     <nav className="navbar">
//       <h1> ColabMate </h1>
//       <ul>
//         <li><a href="#contact">Profile</a></li>
//       </ul>
//     </nav>
//   );
// };

// export default Navbar;
// src/components/Navbar.js
import React from 'react';
import { useAuth } from '../AuthContext';
import { Link } from 'react-router-dom';
 
const Navbar = () => {
    const { user, logout } = useAuth();
 
    return (
        <nav className="flex justify-between p-4 bg-gray-800 text-white">
            <Link to="/">Home</Link>
            <div>
                {user ? (
                    <>
                        <span>{user.name}</span>
                        <button onClick={logout} className="ml-4">Logout</button>
                    </>
                ) : (
                    <>
                        <Link to="/login" className="ml-4">Login</Link>
                        <Link to="/register" className="ml-4">Register</Link>
                    </>
                )}
            </div>
        </nav>
    );
};
 
export default Navbar;
 