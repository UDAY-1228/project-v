import React, { useState } from 'react';

interface ProfileData {
  username: string;
  email: string;
  role: string;
}

const SuperAdminProfile: React.FC = () => {
  const [profile] = useState<ProfileData>({
    username: 'superadmin',
    email: 'superadmin@vid.edu',
    role: 'Super Admin'
  });

  return (
    <div className="profile-page">
      <h1>Profile</h1>
      <div className="profile-card">
        <p><strong>Username:</strong> {profile.username}</p>
        <p><strong>Email:</strong> {profile.email}</p>
        <p><strong>Role:</strong> {profile.role}</p>
      </div>
    </div>
  );
};

export default SuperAdminProfile;
