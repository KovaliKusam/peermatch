// import React, { createContext, useState, useEffect, useContext } from 'react';

// // Create the AuthContext
// const AuthContext = createContext();

// // AuthProvider component to wrap the application and provide authentication state
// export const AuthProvider = ({ children }) => {
//     const [isAuthenticated, setIsAuthenticated] = useState(false);

//     useEffect(() => {
//         // Check local storage for authentication token on component mount
//         const token = localStorage.getItem('authToken');
//         if (token) {
//             setIsAuthenticated(true);
//         }
//     }, []);

//     // Function to log in the user and store the token
//     const login = (token) => {
//         localStorage.setItem('authToken', token);
//         setIsAuthenticated(true);
//     };

//     // Function to log out the user and remove the token
//     const logout = () => {
//         localStorage.removeItem('authToken');
//         setIsAuthenticated(false);
//     };

//     // Provide the authentication state and functions to children components
//     return (
//         <AuthContext.Provider value={{ isAuthenticated, login, logout }}>
//             {children}
//         </AuthContext.Provider>
//     );
// };

// // Custom hook to use the AuthContext
// export const useAuth = () => {
//     return useContext(AuthContext);
// };

// import React, { createContext, useState, useEffect, useContext } from 'react';

// // Create the AuthContext
// const AuthContext = createContext();

// // AuthProvider component to wrap the application and provide authentication state
// export const AuthProvider = ({ children }) => {
//     const [isAuthenticated, setIsAuthenticated] = useState(false);

//     useEffect(() => {
//         // Check local storage for authentication token on component mount
//         const token = localStorage.getItem('authToken');
//         if (token) {
//             setIsAuthenticated(true);
//         }
//     }, []);

//     // Function to log in the user and store the token
//     const login = (token) => {
//         localStorage.setItem('authToken', token);
//         setIsAuthenticated(true);
//     };

//     // Function to log out the user and remove the token
//     const logout = () => {
//         localStorage.removeItem('authToken');
//         setIsAuthenticated(false);
//     };

//     // Provide the authentication state and functions to children components
//     return (
//         <AuthContext.Provider value={{ isAuthenticated, login, logout }}>
//             {children}
//         </AuthContext.Provider>
//     );
// };

// // Custom hook to use the AuthContext
// export const useAuth = () => {
//     return useContext(AuthContext);
// };

import React, { createContext, useState, useEffect, useContext } from 'react';

// Create the AuthContext
const AuthContext = createContext();

// AuthProvider component to wrap the application and provide authentication state
export const AuthProvider = ({ children }) => {
    const [isAuthenticated, setIsAuthenticated] = useState(false);

    useEffect(() => {
        // Check local storage for authentication token on component mount
        const token = localStorage.getItem('authToken');
        if (token) {
            setIsAuthenticated(true);
        }
    }, []);

    // Function to log in the user and store the token
    const login = (token) => {
        localStorage.setItem('authToken', token);
        setIsAuthenticated(true);
    };

    // Function to log out the user and remove the token
    const logout = () => {
        localStorage.removeItem('authToken');
        setIsAuthenticated(false);
    };

    // Provide the authentication state and functions to children components
    return (
        <AuthContext.Provider value={{ isAuthenticated, login, logout }}>
            {children}
        </AuthContext.Provider>
    );
};

// Custom hook to use the AuthContext
export const useAuth = () => {
    return useContext(AuthContext);
};