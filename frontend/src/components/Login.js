
// import React, { useState } from 'react';
// import { loginUser } from '../services/api'; // Import the loginUser function
// import { submitExpertise } from '../services/api'; // Import the submitExpertise function
// import Thome from './Thome'
// const Login = () => {
//     const [email, setEmail] = useState('');
//     const [password, setPassword] = useState('');
//     const [error, setError] = useState('');
//     const [isExpertiseSubmitted, setIsExpertiseSubmitted] = useState(false); // Track if expertise has been submitted

//     const handleSubmit = async (e) => {
//         e.preventDefault();
//         console.log('Form submitted'); // Debugging step
//         console.log('Email:', email); // Debugging step
//         console.log('Password:', password); // Debugging step (be cautious with logging passwords)

//         try {
//             const response = await loginUser(email, password); // Use the loginUser function
//             console.log('Login successful:', response); 
//             <Thome/>// Debugging step
//             setIsExpertiseSubmitted(true); // Set flag to true to show expertise form
            
//         } catch (err) {
//             console.error('Login error:', err); // Debugging step
//             setError('Invalid email or password');
//         }
//     };

//     const handleExpertiseSubmit = async (data) => {
//         try {
//             const response = await submitExpertise(data);
//             console.log('Expertise submitted successfully:', response); // Debugging step
//         } catch (error) {
//             console.error('Error submitting expertise:', error); // Debugging step
//         }
//     };

//     return (
//         <div className="flex items-center justify-center min-h-screen bg-gray-100">
//             <div className="bg-white p-8 rounded shadow-md w-96">
//                 <h2 className="text-2xl font-bold mb-6 text-center">Logivcn</h2>
//                 {error && <p className="text-red-500 text-sm mb-4">{error}</p>}
//                 {!isExpertiseSubmitted ? (
//                     <form onSubmit={handleSubmit} className="flex flex-col">
//                         <input
//                             type="email"
//                             placeholder="Email"
//                             value={email}
//                             onChange={(e) => {
//                                 setEmail(e.target.value);
//                                 console.log('Email input changed:', e.target.value); // Debugging step
//                             }}
//                             required
//                             className="p-3 border border-gray-300 rounded mb-4 focus:outline-none focus:ring-2 focus:ring-blue-500"
//                         />
//                         <input
//                             type="password"
//                             placeholder="Password"
//                             value={password}
//                             onChange={(e) => {
//                                 setPassword(e.target.value);
//                                 console.log('Password input changed:', e.target.value); // Debugging step
//                             }}
//                             required
//                             className="p-3 border border-gray-300 rounded mb-6 focus:outline-none focus:ring-2 focus:ring-blue-500"
//                         />
//                         <button type="submit" className="bg-blue-500 text-white p-3 rounded hover:bg-blue-600 transition duration-200">
//                             Login
//                         </button>
//                     </form>
//                 ) : (
//                     // <ExpertiseForm email={email} onSubmit={handleExpertiseSubmit} />
//                     console.log("a")               )}
//                 <p className="mt-4 text-center">
//                     Don't have an account? <a href="/register" className="text-blue-500 hover:underline">Register</a>
//                 </p>
//             </div>
//         </div>
//     );
// };

// const ExpertiseForm = ({ email, onSubmit }) => {
//     const [expertise, setExpertise] = useState('');
//     const [currentProject, setCurrentProject] = useState('');
//     const [loginTime, setLoginTime] = useState('');
//     const [logoutTime, setLogoutTime] = useState('');

//     const handleSubmit = (e) => {
//         e.preventDefault();
//         const data = {
//             email, // Pass the user's email
//             expertise,
//             current_project: currentProject,
//             login_time: loginTime,
//             logout_time: logoutTime
//         };
//         onSubmit(data); // Submit the expertise data
//     };

//     return (
//         <form onSubmit={handleSubmit} className="flex flex-col mt-4">
//             <input
//                 type="text"
//                 placeholder="Expertise"
//                 value={expertise}
//                 onChange={(e) => setExpertise(e.target.value)}
//                 required
//                 className="p-3 border border-gray-300 rounded mb-4 focus:outline-none focus:ring-2 focus:ring-blue-500"
//             />
//             <input
//                 type="text"
//                 placeholder="Current Project"
//                 value={currentProject}
//                 onChange={(e) => setCurrentProject(e.target.value)}
//                 required
//                 className="p-3 border border-gray-300 rounded mb-4 focus:outline-none focus:ring-2 focus:ring-blue-500"
//             />
//             <input
//                 type="time"
//                 value={loginTime}
//                 onChange={(e) => setLoginTime(e.target.value)}
//                 required
//                 className="p-3 border border-gray-300 rounded mb-4 focus:outline-none focus:ring-2 focus:ring-blue-500"
//             />
//             <input
//                 type="time"
//                 value={logoutTime}
//                 onChange={(e) => setLogoutTime(e.target.value)}
//                 required
//                 className="p-3 border border-gray-300 rounded mb-6 focus:outline-none focus:ring-2 focus:ring-blue-500"
//             />
//             <button type="submit" className="bg-blue-500 text-white p-3 rounded hover:bg-blue-600 transition duration-200">
//                 Submit Expertise
//             </button>
//         </form>
//     );
// };

// export default Login;

// import React, { useState } from 'react';
// import { useNavigate } from 'react-router-dom'; // Import useNavigate for navigation
// import { loginUser } from '../services/api'; // Import the loginUser function
// import { submitExpertise } from '../services/api'; // Import the submitExpertise function

// const Login = () => {
//     const navigate = useNavigate(); // Initialize useNavigate
//     const [email, setEmail] = useState('');
//     const [password, setPassword] = useState('');
//     const [error, setError] = useState('');
//     const [isExpertiseSubmitted, setIsExpertiseSubmitted] = useState(false); // Track if expertise has been submitted

//     const handleSubmit = async (e) => {
//         e.preventDefault();
//         console.log('Form submitted'); // Debugging step
//         console.log('Email:', email); // Debugging step
//         console.log('Password:', password); // Debugging step (be cautious with logging passwords)

//         try {
//             const response = await loginUser(email, password); // Use the loginUser function
//             console.log('Login successful:', response); 
//             setIsExpertiseSubmitted(true); // Set flag to true to show expertise form
//             navigate('/'); // Redirect to home page
//         } catch (err) {
//             console.error('Login error:', err); // Debugging step
//             setError('Invalid email or password');
//         }
//     };

//     const handleExpertiseSubmit = async (data) => {
//         try {
//             const response = await submitExpertise(data);
//             console.log('Expertise submitted successfully:', response); // Debugging step
//         } catch (error) {
//             console.error('Error submitting expertise:', error); // Debugging step
//         }
//     };

//     return (
//         <div className="flex items-center justify-center min-h-screen bg-gray-100">
//             <div className="bg-white p-8 rounded shadow-md w-96">
//                 <h2 className="text-2xl font-bold mb-6 text-center">Login</h2>
//                 {error && <p className="text-red-500 text-sm mb-4">{error}</p>}
//                 {!isExpertiseSubmitted ? (
//                     <form onSubmit={handleSubmit} className="flex flex-col">
//                         <input
//                             type="email"
//                             placeholder="Email"
//                             value={email}
//                             onChange={(e) => {
//                                 setEmail(e.target.value);
//                                 console.log('Email input changed:', e.target.value); // Debugging step
//                             }}
//                             required
//                             className="p-3 border border-gray-300 rounded mb-4 focus:outline-none focus:ring-2 focus:ring-blue-500"
//                         />
//                         <input
//                             type="password"
//                             placeholder="Password"
//                             value={password}
//                             onChange={(e) => {
//                                 setPassword(e.target.value);
//                                 console.log('Password input changed:', e.target.value); // Debugging step
//                             }}
//                             required
//                             className="p-3 border border-gray-300 rounded mb-6 focus:outline-none focus:ring-2 focus:ring-blue-500"
//                         />
//                         <button type="submit" className="bg-blue-500 text-white p-3 rounded hover:bg-blue-600 transition duration-200">
//                             Login
//                         </button>
//                     </form>
//                 ) : (
//                     <ExpertiseForm email={email} onSubmit={handleExpertiseSubmit} />
//                 )}
//                 <p className="mt-4 text-center">
//                     Don't have an account? <a href="/register" className="text-blue-500 hover:underline">Register</a>
//                 </p>
//             </div>
//         </div>
//     );
// };

// const ExpertiseForm = ({ email, onSubmit }) => {
//     const [expertise, setExpertise] = useState('');
//     const [currentProject, setCurrentProject] = useState('');
//     const [loginTime, setLoginTime] = useState('');
//     const [logoutTime, setLogoutTime] = useState('');

//     const handleSubmit = (e) => {
//         e.preventDefault();
//         const data = {
//             email, // Pass the user's email
//             expertise,
//             current_project: currentProject,
//             login_time: loginTime,
//             logout_time: logoutTime
//         };
//         onSubmit(data); // Submit the expertise data
//     };

//     return (
//         <form onSubmit={handleSubmit} className="flex flex-col mt-4">
//             <input
//                 type="text"
//                 placeholder="Expertise"
//                 value={expertise}
//                 onChange={(e) => setExpertise(e.target.value)}
//                 required
//                 className="p-3 border border-gray-300 rounded mb-4 focus:outline-none focus:ring-2 focus:ring-blue-500"
//             />
//             <input
//                 type="text"
//                 placeholder="Current Project"
//                 value={currentProject}
//                 onChange={(e) => setCurrentProject(e.target.value)}
//                 required
//                 className="p-3 border border-gray-300 rounded mb-4 focus:outline-none focus:ring-2 focus:ring-blue-500"
//             />
//             <input
//                 type="time"
//                 value={loginTime}
//                 onChange={(e) => setLoginTime(e.target.value)}
//                 required
//                 className="p-3 border border-gray-300 rounded mb-4 focus:outline-none focus:ring-2 focus:ring-blue-500"
//             />
//             <input
//                 type="time"
//                 value={logoutTime}
//                 onChange={(e) => setLogoutTime(e.target.value)}
//                 required
//                 className="p-3 border border-gray-300 rounded mb-6 focus:outline-none focus:ring-2 focus:ring-blue-500"
//             />
//             <button type="submit" className="bg-blue-500 text-white p-3 rounded hover:bg-blue-600 transition duration-200">
//                 Submit Expertise
//             </button>
//         </form>
//     );
// };

// export default Login;

import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { loginUser } from '../services/api';
import { useAuth } from '../AuthContext'; // Import useAuth hook
import { submitExpertise } from '../services/api'; // Ensure the path is correct

const Login = () => {
    const navigate = useNavigate();
    const { login } = useAuth(); // Use login function from AuthContext
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');
    const [error, setError] = useState('');
    const [isExpertiseSubmitted, setIsExpertiseSubmitted] = useState(false);

    const handleSubmit = async (e) => {
        e.preventDefault();
        try {
            const response = await loginUser(email, password);
            console.log('Login successful:', response);
            login(response.token); // Store the token and update auth state
            setIsExpertiseSubmitted(true);
            navigate('/'); // Redirect to home page
        } catch (err) {
            console.error('Login error:', err);
            setError('Invalid email or password');
        }
    };

    const handleExpertiseSubmit = async (data) => {
        try {
            const response = await submitExpertise(data);
            console.log('Expertise submitted successfully:', response);
        } catch (error) {
            console.error('Error submitting expertise:', error);
        }
    };

    return (
        <div className="flex items-center justify-center min-h-screen bg-gray-100">
            <div className="bg-white p-8 rounded shadow-md w-96">
                <h2 className="text-2xl font-bold mb-6 text-center">Login</h2>
                {error && <p className="text-red-500 text-sm mb-4">{error}</p>}
                {!isExpertiseSubmitted ? (
                    <form onSubmit={handleSubmit} className="flex flex-col">
                        <input
                            type="email"
                            placeholder="Email"
                            value={email}
                            onChange={(e) => setEmail(e.target.value)}
                            required
                            className="p-3 border border-gray-300 rounded mb-4 focus:outline-none focus:ring-2 focus:ring-blue-500"
                        />
                        <input
                            type="password"
                            placeholder="Password"
                            value={password}
                            onChange={(e) => setPassword(e.target.value)}
                            required
                            className="p-3 border border-gray-300 rounded mb-6 focus:outline-none focus:ring-2 focus:ring-blue-500"
                        />
                        <button type="submit" className="bg-blue-500 text-white p-3 rounded hover:bg-blue-600 transition duration-200">
                            Login
                        </button>
                    </form>
                ) : (
                    <ExpertiseForm email={email} onSubmit={handleExpertiseSubmit} />
                )}
                <p className="mt-4 text-center">
                    Don't have an account? <a href="/register" className="text-blue-500 hover:underline">Register</a>
                </p>
            </div>
        </div>
    );
};

const ExpertiseForm = ({ email, onSubmit }) => {
    const [expertise, setExpertise] = useState('');
    const [currentProject, setCurrentProject] = useState('');
    const [loginTime, setLoginTime] = useState('');
    const [logoutTime, setLogoutTime] = useState('');

    const handleSubmit = (e) => {
        e.preventDefault();
        const data = {
            email,
            expertise,
            current_project: currentProject,
            login_time: loginTime,
            logout_time: logoutTime
        };
        onSubmit(data);
    };

    return (
        <form onSubmit={handleSubmit} className="flex flex-col mt-4">
            <input
                type="text"
                placeholder="Expertise"
                value={expertise}
                onChange={(e) => setExpertise(e.target.value)}
                required
                className="p-3 border border-gray-300 rounded mb-4 focus:outline-none focus:ring-2 focus:ring-blue-500"
            />
            <input
                type="text"
                placeholder="Current Project"
                value={currentProject}
                onChange={(e) => setCurrentProject(e.target.value)}
                required
                className="p-3 border border-gray-300 rounded mb-4 focus:outline-none focus:ring-2 focus:ring-blue-500"
            />
            <input
                type="time"
                value={loginTime}
                onChange={(e) => setLoginTime(e.target.value)}
                required
                className="p-3 border border-gray-300 rounded mb-4 focus:outline-none focus:ring-2 focus:ring-blue-500"
            />
            <input
                type="time"
                value={logoutTime}
                onChange={(e) => setLogoutTime(e.target.value)}
                required
                className="p-3 border border-gray-300 rounded mb-6 focus:outline-none focus:ring-2 focus:ring-blue-500"
            />
            <button type="submit" className="bg-blue-500 text-white p-3 rounded hover:bg-blue-600 transition duration-200">
                Submit Expertise
            </button>
        </form>
    );
};

export default Login;