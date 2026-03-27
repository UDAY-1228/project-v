import React from 'react';
import { useAuth } from '../services/AuthContext';
import { Link } from 'react-router-dom';

const Homepage: React.FC = () => {
  const { user } = useAuth();
  const workspaces = user?.assigned_workspaces || [];

  return (
    <div className="flex flex-col gap-10">
      <header className="flex justify-between items-center">
        <div>
          <h1 className="text-4xl font-black text-black">Welcome back, {user?.username}!</h1>
          <p className="text-lg text-gray-500 mt-1">Select a workspace to manage your institution activities.</p>
        </div>
        <div className="flex gap-6">
          <div className="bg-white p-6 rounded-2xl border border-gray-200 min-w-[160px] shadow-sm">
            <span className="block text-2xl font-black text-black">24</span>
            <span className="block text-[11px] font-bold text-gray-400 uppercase tracking-widest mt-1">New Notices</span>
          </div>
          <div className="bg-white p-6 rounded-2xl border border-gray-200 min-w-[160px] shadow-sm">
            <span className="block text-2xl font-black text-black">12</span>
            <span className="block text-[11px] font-bold text-gray-400 uppercase tracking-widest mt-1">Pending Tasks</span>
          </div>
        </div>
      </header>

      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
        {user?.role === 'super_admin' && (
          <Link to="/super-admin/institutions" className="p-8 rounded-[32px] bg-black text-white hover:scale-[1.02] transition-all group shadow-xl shadow-black/20">
            <span className="text-4xl mb-4 block">🏢</span>
            <h3 className="text-xl font-bold">Manage Institutions</h3>
            <p className="text-gray-400 mt-2">Centralized control for all system tenants and licenses.</p>
          </Link>
        )}

        {user?.role === 'admin' && (
          <Link to="/admin/users" className="p-8 rounded-[32px] border-2 border-dashed border-gray-200 bg-white hover:border-black hover:scale-[1.02] transition-all group">
            <span className="text-4xl mb-4 block">👥</span>
            <h3 className="text-xl font-bold">User Management</h3>
            <p className="text-gray-500 mt-2">Provision new users and assign workspace permissions.</p>
          </Link>
        )}

        {workspaces.map((ws) => (
          <Link key={ws} to={`/workspaces/${ws}`} className="p-8 rounded-[32px] bg-white border border-gray-100 hover:border-black hover:scale-[1.02] transition-all shadow-sm">
            <span className="text-4xl mb-4 block text-gray-300 group-hover:text-black">📂</span>
            <h3 className="text-xl font-bold">{ws.replace('-', ' ').replace(/\b\w/g, c => c.toUpperCase())}</h3>
            <p className="text-gray-500 mt-2">Access your specialized {ws.replace('-', ' ')} module.</p>
          </Link>
        ))}
      </div>
    </div>
  );
};

export default Homepage;
