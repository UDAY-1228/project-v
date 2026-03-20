import React, { useState } from 'react';
import Button from '../../../core/frontend/components/Button';
import { login } from '../services/api';

const Login: React.FC = () => {
    const [credentials, setCredentials] = useState({ username: '', password: '' });
    const [loading, setLoading] = useState(false);
    const [error, setError] = useState('');

    const handleSubmit = async (e: React.FormEvent) => {
        e.preventDefault();
        setLoading(true);
        setError('');
        try {
            await login(credentials);
            window.location.href = '/super-admin/dashboard';
        } catch (err: any) {
            setError(err.response?.data?.detail || 'Login failed. Please check your credentials.');
        } finally {
            setLoading(false);
        }
    };

    return (
        <div className="min-h-screen grid items-center justify-center p-6 bg-slate-900 overflow-hidden relative">
            {/* Background elements */}
            <div className="absolute top-0 left-0 w-full h-full opacity-30 pointer-events-none">
                <div className="absolute top-1/4 left-1/4 w-[40rem] h-[40rem] bg-indigo-600 rounded-full blur-[120px] mix-blend-screen animate-pulse"></div>
                <div className="absolute bottom-1/4 right-1/4 w-[40rem] h-[40rem] bg-violet-600 rounded-full blur-[120px] mix-blend-screen"></div>
            </div>

            <div className="w-full max-w-[480px] bg-white/5 backdrop-blur-2xl p-12 rounded-[2.5rem] shadow-2xl border border-white/10 relative z-10">
                <div className="text-center mb-12">
                    <div className="inline-flex items-center justify-center w-20 h-20 bg-indigo-500 rounded-3xl shadow-xl shadow-indigo-500/20 mb-8 border border-white/20">
                        <span className="text-white text-4xl font-black">V</span>
                    </div>
                    <h1 className="text-4xl font-black text-white tracking-tight mb-3">Super Admin</h1>
                    <p className="text-slate-400 font-medium">Please sign in to your dashboard</p>
                </div>

                <form className="space-y-8" onSubmit={handleSubmit}>
                    <div className="space-y-6">
                        <div className="space-y-2">
                            <label className="text-sm font-bold text-slate-300 ml-1">Username</label>
                            <div className="relative group">
                                <span className="absolute left-5 top-1/2 -translate-y-1/2 material-icons text-slate-500 text-lg transition-colors group-focus-within:text-indigo-400">person_outline</span>
                                <input 
                                    type="text" 
                                    className="w-full bg-slate-800/50 border border-slate-700 focus:border-indigo-500 rounded-2xl py-4 pl-14 pr-6 text-white outline-none transition-all placeholder:text-slate-600"
                                    placeholder="Enter your username"
                                    value={credentials.username}
                                    onChange={(e) => setCredentials({...credentials, username: e.target.value})}
                                    required
                                />
                            </div>
                        </div>
                        <div className="space-y-2">
                            <label className="text-sm font-bold text-slate-300 ml-1">Password</label>
                            <div className="relative group">
                                <span className="absolute left-5 top-1/2 -translate-y-1/2 material-icons text-slate-500 text-lg transition-colors group-focus-within:text-indigo-400">lock_open</span>
                                <input 
                                    type="password" 
                                    className="w-full bg-slate-800/50 border border-slate-700 focus:border-indigo-500 rounded-2xl py-4 pl-14 pr-6 text-white outline-none transition-all placeholder:text-slate-600"
                                    placeholder="Enter your password"
                                    value={credentials.password}
                                    onChange={(e) => setCredentials({...credentials, password: e.target.value})}
                                    required
                                />
                            </div>
                        </div>
                    </div>

                    {error && <div className="p-4 bg-rose-500/10 border border-rose-500/20 text-rose-400 text-sm font-medium rounded-xl text-center">{error}</div>}

                    <div className="flex items-center justify-between text-sm px-1">
                        <label className="flex items-center gap-3 cursor-pointer text-slate-400 hover:text-slate-300">
                            <input type="checkbox" className="w-4 h-4 rounded bg-slate-800 border-slate-700 checked:bg-indigo-500" />
                            <span>Remember me</span>
                        </label>
                        <a href="/super-admin/forgot-password" name="forgot-password-link" className="text-indigo-400 font-bold hover:text-indigo-300 transition-colors">Forgot password?</a>
                    </div>

                    <Button 
                        type="submit" 
                        className="w-full py-5 text-lg shadow-xl shadow-indigo-600/20 bg-indigo-500 hover:bg-indigo-600 border-none"
                    >
                        {loading ? 'Authenticating...' : 'Sign In Now'}
                    </Button>
                </form>
            </div>
        </div>
    );
};

export default Login;
