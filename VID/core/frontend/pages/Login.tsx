import React, { useState } from 'react';
import axios from 'axios';

const Login: React.FC = () => {
    const [credentials, setCredentials] = useState({ username: '', password: '' });
    const [loading, setLoading] = useState(false);
    const [error, setError] = useState('');

    const handleSubmit = async (e: React.FormEvent) => {
        e.preventDefault();
        setLoading(true);
        setError('');
        try {
            const res = await axios.post('/api/auth/login', credentials);
            localStorage.setItem('user_data', JSON.stringify(res.data));
            window.location.href = res.data.redirect;
        } catch (err: any) {
            setError(err.response?.data?.detail || 'Authentication failed. Please check your credentials.');
        } finally {
            setLoading(false);
        }
    };

    return (
        <div className="min-h-screen grid items-center justify-center p-8 bg-slate-900 overflow-hidden relative font-outfit">
            {/* Back to home */}
            <a href="/" className="fixed top-6 left-8 z-50 flex items-center gap-2 text-white/50 hover:text-white font-bold text-sm transition-colors">
                <span className="material-icons text-lg">arrow_back</span>
                Back to Home
            </a>
            {/* Background elements */}
            <div className="absolute top-0 left-0 w-full h-full opacity-40 pointer-events-none">
                <div className="absolute top-1/4 left-1/4 w-[45rem] h-[45rem] bg-indigo-600 rounded-full blur-[140px] animate-pulse"></div>
                <div className="absolute bottom-1/4 right-1/4 w-[45rem] h-[45rem] bg-violet-600 rounded-full blur-[140px]"></div>
            </div>

            <div className="w-full max-w-[500px] bg-white/5 backdrop-blur-3xl p-16 rounded-[3.5rem] shadow-2xl border border-white/10 relative z-10 transition-all hover:border-white/20">
                <div className="text-center mb-16">
                    <div className="inline-flex items-center justify-center w-24 h-24 bg-gradient-to-br from-indigo-500 to-violet-600 rounded-3xl shadow-xl shadow-indigo-500/30 mb-8 border border-white/20">
                        <span className="text-white text-5xl font-black">V</span>
                    </div>
                    <h1 className="text-5xl font-black text-white tracking-tight mb-4">VID PLATFORM</h1>
                    <p className="text-slate-400 font-bold uppercase tracking-widest text-[10px]">Virtual Identification System</p>
                </div>

                <form className="space-y-10" onSubmit={handleSubmit}>
                    <div className="space-y-8">
                        <div className="space-y-3">
                            <label className="text-xs font-black text-slate-300 uppercase tracking-widest ml-1">Username / Email</label>
                            <div className="relative group">
                                <span className="absolute left-6 top-1/2 -translate-y-1/2 material-icons text-slate-500 text-xl transition-colors group-focus-within:text-indigo-400">alternate_email</span>
                                <input 
                                    type="text" 
                                    className="w-full bg-slate-800/40 border-2 border-slate-700/50 focus:border-indigo-500 rounded-2xl py-5 pl-16 pr-8 text-white outline-none transition-all placeholder:text-slate-600 font-medium"
                                    placeholder="Enter identifier"
                                    value={credentials.username}
                                    onChange={(e) => setCredentials({...credentials, username: e.target.value})}
                                    required
                                />
                            </div>
                        </div>
                        <div className="space-y-3">
                            <label className="text-xs font-black text-slate-300 uppercase tracking-widest ml-1">Secret Key</label>
                            <div className="relative group">
                                <span className="absolute left-6 top-1/2 -translate-y-1/2 material-icons text-slate-500 text-xl transition-colors group-focus-within:text-indigo-400">vpn_key</span>
                                <input 
                                    type="password" 
                                    className="w-full bg-slate-800/40 border-2 border-slate-700/50 focus:border-indigo-500 rounded-2xl py-5 pl-16 pr-8 text-white outline-none transition-all placeholder:text-slate-600 font-medium"
                                    placeholder="Enter password"
                                    value={credentials.password}
                                    onChange={(e) => setCredentials({...credentials, password: e.target.value})}
                                    required
                                />
                            </div>
                        </div>
                    </div>

                    {error && <div className="p-4 bg-rose-500/10 border border-rose-500/20 text-rose-400 text-sm font-bold rounded-2xl text-center uppercase tracking-wide">{error}</div>}

                    <button 
                        type="submit" 
                        disabled={loading}
                        className="w-full py-6 text-lg font-black uppercase tracking-widest shadow-2xl shadow-indigo-600/30 bg-gradient-to-r from-indigo-500 to-violet-600 hover:from-indigo-600 hover:to-violet-700 text-white border-none rounded-3xl transition-all active:scale-[0.98] disabled:opacity-50 disabled:cursor-not-allowed"
                    >
                        {loading ? 'Validating...' : 'Authenticate Access'}
                    </button>
                    
                    <div className="text-center">
                        <p className="text-slate-500 text-xs font-bold uppercase tracking-widest">Multi-Institutional Portals</p>
                    </div>
                </form>
            </div>
        </div>
    );
};

export default Login;
