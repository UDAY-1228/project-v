import React from 'react';
import { useNavigate } from 'react-router-dom';

const BasicSettings: React.FC = () => {
  const navigate = useNavigate();
  return (
    <div className="settings-page">
      <h1>Basic Settings</h1>
      <p>Configure your basic settings here.</p>
    </div>
  );
};

export default BasicSettings;
