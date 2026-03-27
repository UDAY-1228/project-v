import React from 'react';
import { useAuth } from '../services/AuthContext';
import { Link, Outlet, useLocation, useNavigate } from 'react-router-dom';

const DashboardShell: React.FC = () => {
  const { user, logout } = useAuth();
  const location = useLocation();
  const navigate = useNavigate();

  const handleLogout = () => {
    logout();
    navigate('/login');
  };

  const workspaces = user?.assigned_workspaces || [];

  return (
    <div className="flex h-screen bg-gray-50 font-sans">
      {/* Sidebar */}
      <aside className="w-64 bg-white border-r border-gray-200 flex flex-col p-6 overflow-y-auto">
        <div className="mb-8">
          <span className="text-3xl font-black text-black tracking-tight">VID</span>
          <span className="block text-[10px] font-medium text-gray-500 uppercase tracking-[2px] mt-1">Virtual ID System</span>
        </div>

        <nav className="flex-1 space-y-1">
          <Link to="/dashboard" className={`flex items-center px-4 py-3 rounded-xl text-sm font-medium transition-all ${location.pathname === '/dashboard' ? 'bg-black text-white shadow-lg' : 'text-gray-600 hover:bg-gray-100'}`}>
            Dashboard
          </Link>

          {user?.role === 'super_admin' && (
            <div className="mt-6">
              <span className="block text-[11px] font-bold text-gray-400 uppercase tracking-widest mb-2 ml-4">Super Admin</span>
              <Link to="/super-admin/institutions" className="flex items-center px-4 py-3 rounded-xl text-sm font-medium text-gray-600 hover:bg-gray-100 transition-all">
                Manage Institutions
              </Link>
            </div>
          )}

          {user?.role === 'admin' && (
            <div className="mt-6">
              <span className="block text-[11px] font-bold text-gray-400 uppercase tracking-widest mb-2 ml-4">Admin Panel</span>
              <Link to="/admin/users" className="flex items-center px-4 py-3 rounded-xl text-sm font-medium text-gray-600 hover:bg-gray-100 transition-all">
                Manage Users
              </Link>
              <Link to="/admin/workspaces" className="flex items-center px-4 py-3 rounded-xl text-sm font-medium text-gray-600 hover:bg-gray-100 transition-all">
                Workspace Assignment
              </Link>
            </div>
          )}

          {workspaces.length > 0 && (
            <div className="mt-6">
              <span className="block text-[11px] font-bold text-gray-400 uppercase tracking-widest mb-2 ml-4">Workspaces</span>
              {workspaces.map((ws) => (
                <Link key={ws} to={`/workspaces/${ws}`} className={`flex items-center px-4 py-3 rounded-xl text-sm font-medium transition-all ${location.pathname.includes(ws) ? 'bg-black text-white' : 'text-gray-600 hover:bg-gray-100'}`}>
                  {ws.replace('-', ' ').replace(/\b\w/g, c => c.toUpperCase())}
                </Link>
              ))}
            </div>
          )}
        </nav>

        <div className="mt-auto pt-6 border-t border-gray-100 flex flex-col gap-4">
          <div className="flex flex-col">
            <span className="text-sm font-bold text-black">{user?.username}</span>
            <span className="text-xs text-gray-500 capitalize">{user?.role}</span>
          </div>
          <button onClick={handleLogout} className="p-3 rounded-xl border border-gray-200 text-sm font-semibold text-black hover:bg-red-50 hover:text-red-500 hover:border-red-200 transition-all text-center">
            Logout
          </button>
        </div>
      </aside>

      {/* Main Content */}
      <main className="flex-1 p-10 overflow-y-auto">
        <Outlet />
      </main>
    </div>
  );
};

export default DashboardShell;
