
// import React, { useState } from 'react';
// import { useAuth } from '../AuthContext';
// import { registerUser } from '../services/api'; // Import the registerUser function

// const Register = () => {
//     const { register } = useAuth();
//     const [name, setName] = useState('');
//     const [email, setEmail] = useState('');
//     const [password, setPassword] = useState('');
//     const [error, setError] = useState('');

//     const handleSubmit = async (e) => {
//         e.preventDefault();
//         try {
//             // Call the registerUser function instead of the auth context
//             const response = await registerUser(name, email, password);
//             console.log("Registration successful:", response);
//             // Optionally, you can redirect the user or show a success message
//         } catch (err) {
//             setError('Registration failed');
//         }
//     };

//     return (
//         <div className="flex items-center justify-center min-h-screen bg-gray-100">
//             <div className="bg-white p-8 rounded shadow-md w-96">
//                 <h2 className="text-2xl font-bold mb-6 text-center">Register</h2>
//                 {error && <p className="text-red-500 text-sm mb-4">{error}</p>}
//                 <form onSubmit={handleSubmit} className="flex flex-col">
//                     <input
//                         type="text"
//                         placeholder="Name"
//                         value={name}
//                         onChange={(e) => setName(e.target.value)}
//                         required
//                         className="p-3 border border-gray-300 rounded mb-4 focus:outline-none focus:ring-2 focus:ring-blue-500"
//                     />
//                     <input
//                         type="email"
//                         placeholder="Email"
//                         value={email}
//                         onChange={(e) => setEmail(e.target.value)}
//                         required
//                         className="p-3 border border-gray-300 rounded mb-4 focus:outline-none focus:ring-2 focus:ring-blue-500"
//                     />
//                     <input
//                         type="password"
//                         placeholder="Password"
//                         value={password}
//                         onChange={(e) => setPassword(e.target.value)}
//                         required
//                         className="p-3 border border-gray-300 rounded mb-6 focus:outline-none focus:ring-2 focus:ring-blue-500"
//                     />
//                     <button type="submit" className="bg-blue-500 text-white p-3 rounded hover:bg-blue-600 transition duration-200">
//                         Register
//                     </button>
//                 </form>
//                 <p className="mt-4 text-center">
//                     Already have an account? <a href="/login" className="text-blue-500 hover:underline">Login</a>
//                 </p>
//             </div>
//         </div>
//     );
// };

// export default Register;
import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom'; // Import useNavigate for navigation
import { registerUser } from '../services/api'; // Import the registerUser function

const Register = () => {
    const navigate = useNavigate(); // Initialize useNavigate
    const [name, setName] = useState('');
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');
    const [error, setError] = useState('');

    const handleSubmit = async (e) => {
        e.preventDefault();
        try {
            // Call the registerUser function
            const response = await registerUser(name, email, password);
            console.log("Registration successful:", response);
            alert("Successfully registered! You can now log in."); // Show success alert
            navigate('/login'); // Redirect to login page
        } catch (err) {
            setError('Registration failed');
        }
    };

    return (
        <div className="flex items-center justify-center min-h-screen bg-gray-100">
            <div className="bg-white p-8 rounded shadow-md w-96">
                <h2 className="text-2xl font-bold mb-6 text-center">Register</h2>
                {error && <p className="text-red-500 text-sm mb-4">{error}</p>}
                <form onSubmit={handleSubmit} className="flex flex-col">
                    <input
                        type="text"
                        placeholder="Name"
                        value={name}
                        onChange={(e) => setName(e.target.value)}
                        required
                        className="p-3 border border-gray-300 rounded mb-4 focus:outline-none focus:ring-2 focus:ring-blue-500"
                    />
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
                        Register
                    </button>
                </form>
                <p className="mt-4 text-center">
                    Already have an account? <a href="/login" className="text-blue-500 hover:underline">Login</a>
                </p>
            </div>
        </div>
    );
};

export default Register;