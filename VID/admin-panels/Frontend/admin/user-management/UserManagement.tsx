import React, { useState } from 'react';

interface User {
  username: string;
  role: string;
  is_active: boolean;
}

const UserManagement: React.FC = () => {
  const [users] = useState<User[]>([
    { username: 'john_doe', role: 'student', is_active: true },
    { username: 'jane_smith', role: 'faculty', is_active: true }
  ]);

  const createUser = () => {
    console.log('Creating user...');
  };

  const manageUser = (id: string) => {
    console.log('Managing user:', id);
  };

  const assignWorkspaces = (id: string) => {
    console.log('Assigning workspaces to user:', id);
  };

  const updateUser = (id: string) => {
    console.log('Updating user:', id);
  };

  const deactivateUser = (id: string) => {
    console.log('Deactivating user:', id);
  };

  return (
    <div className="user-management-page">
      <h1>User Management</h1>
      <button onClick={createUser}>Create User</button>
      <table>
        <thead>
          <tr><th>Username</th><th>Role</th><th>Status</th><th>Actions</th></tr>
        </thead>
        <tbody>
          {users.map((user, idx) => (
            <tr key={idx}>
              <td>{user.username}</td>
              <td>{user.role}</td>
              <td>{user.is_active ? 'Active' : 'Inactive'}</td>
              <td>
                <button onClick={() => manageUser(user.username)}>Manage</button>
                <button onClick={() => assignWorkspaces(user.username)}>Assign</button>
                <button onClick={() => updateUser(user.username)}>Update</button>
                <button onClick={() => deactivateUser(user.username)}>Deactivate</button>
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default UserManagement;
