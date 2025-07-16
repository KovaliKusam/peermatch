// // src/App.js
// // import React from 'react';
// // import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
// // import { AuthProvider } from './AuthContext';
// // import Login from './components/Login';
// // import Register from './components/Register';
// // import Navbar from './components/Navbar';
// // import Home from './components/Home';
// //  import Thome from './components/Thome';
// // const App1 = () => {
// //     return (
// //         <AuthProvider>
// //             <Router>
// //                 <Navbar />
// //                 <Routes>
// //                     <Route path="/" element={<Thome />} />
// //                     <Route path="/login" element={<Login />} />
// //                     <Route path="/register" element={<Register />} />
// //                 </Routes>
// //             </Router>
// //         </AuthProvider>
// //     );
// // };
 
// // export default App1;

// import React from 'react';
// import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
// import { AuthProvider } from './AuthContext'; // Import the AuthProvider
// import Navbar from './components/Navbar'; // Import the Navbar component
// import Thome from './components/Thome'; // Main home component
// import Submit from './components/Submit'; // Import the Submit component
// import SearchExpertiseForm from './components/SearchExpertiseForm'; // Import the SearchExpertise component
// import Footer from './components/Footer'; // Import the Footer component (if needed)
// import Login from './components/Login'; // Import the Login component
// import Register from './components/Register'; // Import the Register component
// import Chatbot from './components/Chatbot';
// const App = () => {
//       const apiKey = 'eyJraWQiOiJMd29kQ04wZFNtbXRlVFpEZG5YUVpxZzBwU3NQLUlUU1JGM19aamgzSWZjIiwiYWxnIjoiUlMyNTYifQ.eyJ2ZXIiOjEsImp0aSI6IkFULmljM1NVM1lON0VGSVJJZ1ZyNW9pM3dmeDdtWjJBLWlhTnhXWGJoYmt2eTAub2FyM2p2amY0dTV3ZjEzTzc1ZDciLCJpc3MiOiJodHRwczovL3NwZ2xvYmFsLm9rdGEuY29tL29hdXRoMi9kZWZhdWx0IiwiYXVkIjoiYXBpOi8vZGVmYXVsdCIsImlhdCI6MTc1MjY1Nzk2MywiZXhwIjoxNzUyNjYxNTYzLCJjaWQiOiIwb2Fld3gyeGxudE9jMVFUazVkNyIsInVpZCI6IjAwdXAwZmppeXNWTWIzak9XNWQ3Iiwic2NwIjpbInByb2ZpbGUiLCJvZmZsaW5lX2FjY2VzcyIsImVtYWlsIiwib3BlbmlkIl0sImF1dGhfdGltZSI6MTc1MjYyNzYzMCwiY291bnRyeSI6IklORElBIiwic3ViIjoia292YWxpLmt1c2FtQHNwZ2xvYmFsLmNvbSJ9.FVgU6qqOR0YVxUGdTa96ll4qdDY52nAK5lSB7yT4hDjeY2-n_T794i8lTBPaBiAMdsnyhWXpTwdVj_Lq3_IIAyjfXzUFvsqkXbz78kbhS69mG0Mp1wss700QpwUiq9Nsi1j75f4xs4ulzUpj-y6E2908UQKaZtkL-8PxPyNIpkiGRhtgaPqq864V2YSdWt8A1N4durQKO8el3msBzvspbPNMV7_-3IOeAW7mOJwEpw_vZ-idjQ6TdHWEtn2_rPvHNIpPNH242jZo9W8swiaK-gZYBVCx1NdFtRedsocFlGe8-YHjkTNE1_PGHJIO_5cp-d1m5mngvHSz8FmeU-eDUQ'; // Replace with your actual API key
//     const environmentUrl = 'https://sparkapi.spglobal.com';
 
//   return (
//     <AuthProvider>
//       <Router>
//         <div>
//           <Navbar />
//           <Routes>
//             <Route path="/" element={<Thome />} /> {/* Route for the home page */}
//             <Route path="/submit" element={<Submit />} /> {/* Route for the Submit component */}
//             <Route path="/search-expertise" element={<SearchExpertiseForm />} /> {/* Route for SearchExpertise component */}
//             <Route path="/login" element={<Login />} /> {/* Route for Login component */}
//             <Route path="/register" element={<Register />} /> {/* Route for Register component */}
//           </Routes>
//                           <Chatbot apiKey={apiKey} environmentUrl={environmentUrl} /> {/* Add the Chatbot component */}
 
 
//           <Footer /> {/* Optional: If you want a footer on all pages */}
//         </div>
//       </Router>
//     </AuthProvider>
//   );
// };

// export default App;

import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import { AuthProvider } from './AuthContext'; // Import the AuthProvider
import Navbar from './components/Navbar'; // Import the Navbar component
import Thome from './components/Thome'; // Main home component
import Submit from './components/Submit'; // Import the Submit component
import SearchExpertiseForm from './components/SearchExpertiseForm'; // Import the SearchExpertise component
import Footer from './components/Footer'; // Import the Footer component (if needed)
import Login from './components/Login'; // Import the Login component
import Register from './components/Register'; // Import the Register component
import Chatbot from './components/Chatbot'; // Import the Chatbot component

const App = () => {
  const apiKey = 'eyJraWQiOiJMd29kQ04wZFNtbXRlVFpEZG5YUVpxZzBwU3NQLUlUU1JGM19aamgzSWZjIiwiYWxnIjoiUlMyNTYifQ.eyJ2ZXIiOjEsImp0aSI6IkFULlNiVGtqbHhWQjlBbk9OMG1BOE5SMjR4QUVkME52X0J5SHZteWt2VHpoaW8ub2FyM2p2amY0dTV3ZjEzTzc1ZDciLCJpc3MiOiJodHRwczovL3NwZ2xvYmFsLm9rdGEuY29tL29hdXRoMi9kZWZhdWx0IiwiYXVkIjoiYXBpOi8vZGVmYXVsdCIsImlhdCI6MTc1MjY2MTY4NiwiZXhwIjoxNzUyNjY1Mjg2LCJjaWQiOiIwb2Fld3gyeGxudE9jMVFUazVkNyIsInVpZCI6IjAwdXAwZmppeXNWTWIzak9XNWQ3Iiwic2NwIjpbIm9mZmxpbmVfYWNjZXNzIiwiZW1haWwiLCJwcm9maWxlIiwib3BlbmlkIl0sImF1dGhfdGltZSI6MTc1MjYyNzYzMCwiY291bnRyeSI6IklORElBIiwic3ViIjoia292YWxpLmt1c2FtQHNwZ2xvYmFsLmNvbSJ9.S9fg5pivOlMlrvu0ZD-dVGsg7BVN-Gp51YfDi-PwomVYlAiJA6eBcIoWhnpAow7gjy3hlFOtSrfrvf_7TZwZVprpzb9dp1GRuBfH-S6GsLP3-pVuN2139D3Py--pc7A_gHq8hw9pGU8PZgs5SC0I3ZMym9FfFuFeEwnjMMY2HmRRIVDiu2F7kmsnBapvqcWpRtLNUlUZGLrABTbFsD0dc0nU5WM9DgF2ck1QVhif-q5j_rQSeJTFkid8YN69xlH6qV2qaO_vp2oJGVTYlA9gbufdKkBB0N2jJTCBXsTabaLCwNLocPJNt_zAm-rSHBsYcRisZebIxZ6J4YLmVc94AQ'; // Replace with your actual API key
  const environmentUrl = 'https://sparkapi.spglobal.com';

  return (
    <AuthProvider>
      <Router>
        <div>
          <Navbar />
          <Routes>
            <Route path="/" element={<Thome />} /> {/* Route for the home page */}
            <Route path="/submit" element={<Submit />} /> {/* Route for the Submit component */}
            <Route path="/search-expertise" element={<SearchExpertiseForm />} /> {/* Route for SearchExpertise component */}
            <Route path="/login" element={<Login />} /> {/* Route for Login component */}
            <Route path="/register" element={<Register />} /> {/* Route for Register component */}
          </Routes>
          <Chatbot apiKey={apiKey} environmentUrl={environmentUrl} /> {/* Add the Chatbot component */}
          <Footer /> {/* Optional: If you want a footer on all pages */}
        </div>
      </Router>
    </AuthProvider>
  );
};

export default App;