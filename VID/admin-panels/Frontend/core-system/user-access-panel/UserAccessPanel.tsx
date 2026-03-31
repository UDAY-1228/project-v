import React, { useState } from 'react';

interface UserAccess {
  userId: string;
  name: string;
  accessLevel: string;
}

const UserAccessPanel: React.FC = () => {
  const [accessList] = useState<UserAccess[]>([
    { userId: '1', name: 'John Doe', accessLevel: 'Admin' },
    { userId: '2', name: 'Jane Smith', accessLevel: 'User' }
  ]);

  return (
    <div className="user-access-panel">
      <h1>User Access Panel</h1>
      <ul>
        {accessList.map((user) => (
          <li key={user.userId}>{user.name} - {user.accessLevel}</li>
        ))}
      </ul>
    </div>
  );
};

export default UserAccessPanel;
