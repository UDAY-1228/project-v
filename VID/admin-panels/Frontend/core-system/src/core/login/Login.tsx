import React, { useState } from 'react';
import { useAuth } from '../services/AuthContext';
import { useNavigate } from 'react-router-dom';

const Login: React.FC = () => {
  const { login } = useAuth();
  const navigate = useNavigate();
  const [credentials, setCredentials] = useState({ institution_id: '', username: '', password: '' });
  const [error, setError] = useState<string | null>(null);
  const [loading, setLoading] = useState(false);

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setLoading(true);
    setError(null);
    try {
      await login(credentials);
      navigate('/dashboard');
    } catch (err) {
      setError('Invalid credentials. Please contact your administrator.');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="flex h-screen items-center justify-center bg-gray-50 font-sans p-6">
      <div className="w-full max-w-md bg-white p-12 rounded-[32px] shadow-2xl shadow-black/5 flex flex-col">
        <div className="text-center mb-10">
          <h1 className="text-5xl font-black text-black tracking-tightest">VID</h1>
          <p className="text-sm font-medium text-gray-500 uppercase tracking-widest mt-2">Virtual ID System</p>
        </div>

        <form onSubmit={handleSubmit} className="flex flex-col gap-5">
          <div className="flex flex-col gap-2">
            <label className="text-[13px] font-bold text-gray-400 uppercase tracking-wider ml-1">Institution ID</label>
            <input 
              type="text" 
              className="px-5 py-4 rounded-2xl border-2 border-gray-100 bg-gray-50/50 text-[15px] focus:outline-none focus:border-black focus:bg-white transition-all placeholder-gray-300"
              placeholder="Enter ID (optional for Super Admin)"
              value={credentials.institution_id}
              onChange={(e) => setCredentials({ ...credentials, institution_id: e.target.value })}
            />
          </div>

          <div className="flex flex-col gap-2">
            <label className="text-[13px] font-bold text-gray-400 uppercase tracking-wider ml-1">Username</label>
            <input 
              type="text" 
              required
              className="px-5 py-4 rounded-2xl border-2 border-gray-100 bg-gray-50/50 text-[15px] focus:outline-none focus:border-black focus:bg-white transition-all placeholder-gray-300"
              placeholder="Username"
              value={credentials.username}
              onChange={(e) => setCredentials({ ...credentials, username: e.target.value })}
            />
          </div>

          <div className="flex flex-col gap-2">
            <label className="text-[13px] font-bold text-gray-400 uppercase tracking-wider ml-1">Password</label>
            <input 
              type="password" 
              required
              className="px-5 py-4 rounded-2xl border-2 border-gray-100 bg-gray-50/50 text-[15px] focus:outline-none focus:border-black focus:bg-white transition-all placeholder-gray-300"
              placeholder="Password"
              value={credentials.password}
              onChange={(e) => setCredentials({ ...credentials, password: e.target.value })}
            />
          </div>

          {error && <div className="text-red-500 text-sm font-bold text-center bg-red-50 p-4 rounded-2xl mb-4">{error}</div>}

          <button 
            type="submit" 
            disabled={loading}
            className="mt-4 p-4 rounded-2xl bg-black text-white text-lg font-bold hover:scale-[1.02] active:scale-95 transition-all disabled:opacity-50"
          >
            {loading ? 'Authenticating...' : 'Login'}
          </button>
        </form>

        <div className="mt-12 text-center text-xs font-medium text-gray-400">
          &copy; 2026 VID Enterprise. All rights reserved.
        </div>
      </div>
    </div>
  );
};

export default Login;
