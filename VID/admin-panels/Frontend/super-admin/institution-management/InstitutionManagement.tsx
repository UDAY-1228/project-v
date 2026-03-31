import React, { useState } from 'react';

interface Institution {
  id: string;
  name: string;
  code: string;
  is_active: boolean;
}

const InstitutionManagement: React.FC = () => {
  const [institutions] = useState<Institution[]>([
    { id: '1', name: 'Example University', code: 'EU001', is_active: true },
    { id: '2', name: 'Global Academy', code: 'GA101', is_active: false }
  ]);

  const createInstitution = () => {
    console.log('Creating institution...');
  };

  const updateInstitution = (id: string) => {
    console.log('Updating institution:', id);
  };

  const deleteInstitution = (id: string) => {
    console.log('Deleting institution:', id);
  };

  const toggleActivation = (id: string) => {
    console.log('Toggling activation for institution:', id);
  };

  return (
    <div className="institution-management-page">
      <h1>Institution Management</h1>
      <button onClick={createInstitution}>Create Institution</button>
      <table>
        <thead>
          <tr><th>Name</th><th>Code</th><th>Status</th><th>Actions</th></tr>
        </thead>
        <tbody>
          {institutions.map((inst) => (
            <tr key={inst.id}>
              <td>{inst.name}</td>
              <td>{inst.code}</td>
              <td>{inst.is_active ? 'Active' : 'Inactive'}</td>
              <td>
                <button onClick={() => updateInstitution(inst.id)}>Update</button>
                <button onClick={() => deleteInstitution(inst.id)}>Delete</button>
                <button onClick={() => toggleActivation(inst.id)}>
                  {inst.is_active ? 'Deactivate' : 'Activate'}
                </button>
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default InstitutionManagement;
