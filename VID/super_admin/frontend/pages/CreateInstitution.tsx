import React, { useState } from 'react';
import Layout from '../../../core/frontend/components/Layout';
import Button from '../../../core/frontend/components/Button';
import axios from 'axios';

const CreateInstitution: React.FC = () => {
    const [formData, setFormData] = useState({
        name: '', code: '', adminEmail: '', adminPassword: ''
    });
    const [loading, setLoading] = useState(false);
    const [successData, setSuccessData] = useState<any>(null);

    const handleSubmit = async (e: React.FormEvent) => {
        e.preventDefault();
        setLoading(true);
        try {
            const res = await axios.post('/api/super-admin/institutions', formData);
            setSuccessData(res.data);
        } catch (err: any) {
            alert(err.response?.data?.detail || 'Failed to create institution');
        } finally {
            setLoading(false);
        }
    };

    if (successData) {
        return (
            <Layout>
                <div className="max-w-4xl mx-auto py-12 px-6">
                    <div className="bg-emerald-50 border-2 border-emerald-100 p-16 rounded-[4rem] text-center shadow-2xl relative overflow-hidden group">
                        <div className="w-28 h-28 bg-emerald-500 rounded-full flex items-center justify-center mx-auto mb-10 shadow-xl shadow-emerald-200">
                            <span className="material-icons text-white text-5xl">check_circle</span>
                        </div>
                        <h1 className="text-5xl font-black text-emerald-900 mb-4 tracking-tight">Institution Provisioned!</h1>
                        <p className="text-emerald-700 text-lg font-medium mb-12">The system has been initialized for the institution.</p>
                        
                        <div className="bg-white p-12 rounded-[2.5rem] shadow-xl text-left border border-emerald-100 relative z-10">
                            <h3 className="text-sm font-bold text-slate-400 uppercase tracking-widest mb-8">Access Credentials</h3>
                            <div className="space-y-8">
                                <div className="p-6 bg-slate-50 rounded-3xl border border-slate-100">
                                    <label className="block text-[10px] font-black text-slate-400 uppercase tracking-widest mb-2 px-1">Institutional Admin Identifier</label>
                                    <span className="text-xl font-bold text-slate-800 tracking-tight">{formData.adminEmail}</span>
                                </div>
                                <div className="p-6 bg-slate-50 rounded-3xl border border-slate-100">
                                    <label className="block text-[10px] font-black text-slate-400 uppercase tracking-widest mb-2 px-1">Security Key</label>
                                    <span className="text-xl font-mono font-bold text-slate-800 tracking-wider">{formData.adminPassword}</span>
                                </div>
                            </div>
                        </div>
                        <div className="mt-12">
                            <Button onClick={() => window.location.href = '/super-admin/dashboard'} className="bg-slate-900 border-none px-12 py-5 rounded-3xl hover:bg-black">Return to Central Hub</Button>
                        </div>
                    </div>
                </div>
            </Layout>
        );
    }

    return (
        <Layout sidebarItems={[
            { label: 'Central Hub', icon: 'dashboard', path: '/super-admin/dashboard' },
            { label: 'Add Institution', icon: 'add_business', path: '/super-admin/institutions' },
        ]}>
            <div className="max-w-4xl mx-auto">
                <div className="mb-12">
                    <h1 className="text-4xl font-black text-slate-800 tracking-tight mb-2 uppercase tracking-widest text-[10px] text-indigo-500 font-bold">System Configuration</h1>
                    <h2 className="text-4xl font-black text-slate-800 tracking-tight">Provision New Institution</h2>
                </div>

                <form className="bg-white p-16 rounded-[4rem] shadow-2xl shadow-indigo-100/30 border border-slate-100 space-y-12" onSubmit={handleSubmit}>
                    <div className="grid grid-cols-1 md:grid-cols-2 gap-12">
                        <div className="space-y-4">
                            <label className="text-xs font-black text-slate-400 uppercase tracking-widest px-1">Institution Name</label>
                            <input 
                                className="w-full bg-slate-50 border-2 border-slate-100 rounded-3xl py-5 px-8 outline-none focus:border-indigo-500 transition-all font-bold placeholder:text-slate-300"
                                placeholder="E.g. Green Valley Academy"
                                value={formData.name}
                                onChange={e => setFormData({...formData, name: e.target.value})}
                                required
                            />
                        </div>
                        <div className="space-y-4">
                            <label className="text-xs font-black text-slate-400 uppercase tracking-widest px-1">Institutional Identifier (Unique Code)</label>
                            <input 
                                className="w-full bg-slate-50 border-2 border-slate-100 rounded-3xl py-5 px-8 outline-none focus:border-indigo-500 transition-all font-bold placeholder:text-slate-300"
                                placeholder="E.g. GVA-001"
                                value={formData.code}
                                onChange={e => setFormData({...formData, code: e.target.value})}
                                required
                            />
                        </div>
                        <div className="space-y-4">
                            <label className="text-xs font-black text-slate-400 uppercase tracking-widest px-1">Institutional Admin Email</label>
                            <input 
                                type="email"
                                className="w-full bg-slate-50 border-2 border-slate-100 rounded-3xl py-5 px-8 outline-none focus:border-indigo-500 transition-all font-bold placeholder:text-slate-300"
                                placeholder="admin@institution.edu"
                                value={formData.adminEmail}
                                onChange={e => setFormData({...formData, adminEmail: e.target.value})}
                                required
                            />
                        </div>
                        <div className="space-y-4">
                            <label className="text-xs font-black text-slate-400 uppercase tracking-widest px-1">Default Security Key (Password)</label>
                            <input 
                                type="password"
                                className="w-full bg-slate-50 border-2 border-slate-100 rounded-3xl py-5 px-8 outline-none focus:border-indigo-500 transition-all font-bold placeholder:text-slate-300"
                                placeholder="••••••••"
                                value={formData.adminPassword}
                                onChange={e => setFormData({...formData, adminPassword: e.target.value})}
                                required
                            />
                        </div>
                    </div>

                    <div className="pt-10 flex items-center justify-between">
                        <button type="button" className="text-sm font-black text-slate-300 hover:text-rose-500 transition-colors uppercase tracking-widest">Abort Process</button>
                        <Button 
                            type="submit" 
                            className="px-16 py-6 rounded-[2rem] text-lg font-black uppercase tracking-widest shadow-2xl shadow-indigo-600/30 bg-slate-900 text-white border-none hover:bg-black"
                            disabled={loading}
                        >
                            {loading ? 'Initializing...' : 'Deploy Institutional Engine'}
                        </Button>
                    </div>
                </form>
            </div>
        </Layout>
    );
};

export default CreateInstitution;
