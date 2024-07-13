import React from 'react';
import { useNavigate } from 'react-router-dom';

// HomePage component with two buttons: "View" and "Sign"
const HomePage = () => {
  const history = useNavigate(); // useNavigate hook to navigate to different routes

  return (
    <div>
      {/* Button to navigate to the SignPage */}
      <button onClick={() => history('/sign')}>Sign</button>
      {/* Button to navigate to the ViewPage */}
      <button onClick={() => history('/view')}>View</button>
    </div>
  );
};

export default HomePage;