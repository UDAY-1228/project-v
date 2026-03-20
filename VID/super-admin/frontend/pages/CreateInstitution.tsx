import React, { useState } from 'react';
import Layout from '../../../core/frontend/components/Layout';
import { createInstitution } from '../services/api';
import Button from '../../../core/frontend/components/Button';

const CreateInstitution: React.FC = () => {
    const [formData, setFormData] = useState({
        name: '', address: '', phone: '', email: ''
    });
    const [loading, setLoading] = useState(false);
    const [successData, setSuccessData] = useState<any>(null);

    const handleSubmit = async (e: React.FormEvent) => {
        e.preventDefault();
        setLoading(true);
        try {
            const res = await createInstitution(formData);
            setSuccessData(res);
        } catch (err) {
            alert('Failed to create institution');
        } finally {
            setLoading(false);
        }
    };

    if (successData) {
        return (
            <Layout>
                <div className="max-w-4xl mx-auto py-12 px-6">
                    <div className="bg-emerald-50 border-2 border-emerald-100 p-16 rounded-[4rem] text-center shadow-2xl relative overflow-hidden group">
                        <div className="absolute top-0 right-0 w-64 h-64 bg-emerald-200/20 rounded-full -translate-y-1/2 translate-x-1/2 animate-ping opacity-20"></div>
                        <div className="w-28 h-28 bg-emerald-500 rounded-full flex items-center justify-center mx-auto mb-10 shadow-xl shadow-emerald-200">
                            <span className="material-icons text-white text-5xl">check_circle</span>
                        </div>
                        <h1 className="text-5xl font-black text-emerald-900 mb-4 tracking-tight">Institution Created!</h1>
                        <p className="text-emerald-700 text-lg font-medium mb-12">Account details have been generated successfully.</p>
                        
                        <div className="bg-white p-12 rounded-[2.5rem] shadow-xl text-left border border-emerald-100 relative z-10">
                            <h3 className="text-sm font-bold text-slate-400 uppercase tracking-widest mb-8 flex items-center gap-3">
                                <span className="w-8 h-[1px] bg-slate-200"></span>
                                Admin Credentials
                            </h3>
                            <div className="space-y-8">
                                <div className="p-6 bg-slate-50 rounded-3xl border border-slate-100 hover:border-indigo-200 hover:bg-slate-50/50 transition-all group">
                                    <label className="block text-[10px] font-black text-slate-400 uppercase tracking-widest mb-2 px-1">Username</label>
                                    <div className="flex items-center justify-between">
                                        <span className="text-xl font-bold text-slate-800 tracking-tight">{successData.admin_credentials.username}</span>
                                        <button className="p-2.5 rounded-xl hover:bg-white hover:shadow-md transition-all text-indigo-500 opacity-0 group-hover:opacity-100"><span className="material-icons text-sm">content_copy</span></button>
                                    </div>
                                </div>
                                <div className="p-6 bg-slate-50 rounded-3xl border border-slate-100 hover:border-indigo-200 hover:bg-slate-50/50 transition-all group">
                                    <label className="block text-[10px] font-black text-slate-400 uppercase tracking-widest mb-2 px-1">Temporary Password</label>
                                    <div className="flex items-center justify-between">
                                        <span className="text-xl font-mono font-bold text-slate-800 tracking-wider">{successData.admin_credentials.temporary_password}</span>
                                        <button className="p-2.5 rounded-xl hover:bg-white hover:shadow-md transition-all text-indigo-500 opacity-0 group-hover:opacity-100"><span className="material-icons text-sm">content_copy</span></button>
                                    </div>
                                </div>
                            </div>
                            <div className="mt-12 p-5 bg-amber-50 rounded-2xl border border-amber-100 flex items-start gap-4">
                                <span className="material-icons text-amber-500 text-xl mt-0.5">warning_amber</span>
                                <p className="text-xs font-bold text-amber-700/80 leading-relaxed uppercase tracking-wide">Please copy these credentials immediately. They will not be shown again for security reasons.</p>
                            </div>
                        </div>
                        <div className="mt-12">
                            <Button onClick={() => window.location.href = '/super-admin/dashboard'} className="bg-slate-900 border-none px-12 py-5 rounded-3xl hover:bg-black">Return to Dashboard</Button>
                        </div>
                    </div>
                </div>
            </Layout>
        );
    }

    return (
        <Layout sidebarItems={[
            { label: 'Dashboard', icon: 'dashboard', path: '/super-admin/dashboard' },
            { label: 'Institutions', icon: 'business', path: '/super-admin/institutions' },
            { label: 'Admins', icon: 'admin_panel_settings', path: '/super-admin/admins' },
            { label: 'System Logs', icon: 'history', path: '/super-admin/logs' },
            { label: 'Settings', icon: 'settings', path: '/super-admin/settings' },
        ]}>
            <div className="max-w-4xl mx-auto">
                <div className="mb-12 flex items-center justify-between">
                    <div>
                        <h1 className="text-4xl font-black text-slate-800 tracking-tight mb-2">Create Institution</h1>
                        <p className="text-slate-500 font-medium">Add a new organization to the platform</p>
                    </div>
                    <div className="w-16 h-16 bg-white rounded-2xl shadow-lg shadow-slate-200 flex items-center justify-center border border-slate-100">
                        <span className="material-icons text-slate-400">add_business</span>
                    </div>
                </div>

                <form className="space-y-10 bg-white p-16 rounded-[3rem] shadow-2xl shadow-indigo-100/30 border border-slate-100 relative overflow-hidden" onSubmit={handleSubmit}>
                    <div className="absolute top-0 right-0 w-48 h-48 bg-indigo-50/20 rounded-full -translate-y-1/2 translate-x-1/2"></div>
                    
                    <div className="grid grid-cols-1 md:grid-cols-2 gap-10">
                        <div className="space-y-3">
                            <label className="text-xs font-black text-slate-400 uppercase tracking-widest px-1">Institution Name</label>
                            <input 
                                className="w-full bg-slate-50/50 border border-slate-200 rounded-2xl py-4.5 px-6 outline-none focus:ring-4 focus:ring-indigo-500/10 focus:border-indigo-500 transition-all font-semibold placeholder:text-slate-300"
                                placeholder="E.g. Green Valley Academy"
                                onChange={(e) => setFormData({...formData, name: e.target.value})}
                                required
                            />
                        </div>
                        <div className="space-y-3">
                            <label className="text-xs font-black text-slate-400 uppercase tracking-widest px-1">Email Address</label>
                            <input 
                                type="email"
                                className="w-full bg-slate-50/50 border border-slate-200 rounded-2xl py-4.5 px-6 outline-none focus:ring-4 focus:ring-indigo-500/10 focus:border-indigo-500 transition-all font-semibold placeholder:text-slate-300"
                                placeholder="admin@institution.com"
                                onChange={(e) => setFormData({...formData, email: e.target.value})}
                                required
                            />
                        </div>
                        <div className="space-y-3">
                            <label className="text-xs font-black text-slate-400 uppercase tracking-widest px-1">Phone Number</label>
                            <input 
                                className="w-full bg-slate-50/50 border border-slate-200 rounded-2xl py-4.5 px-6 outline-none focus:ring-4 focus:ring-indigo-500/10 focus:border-indigo-500 transition-all font-semibold placeholder:text-slate-300"
                                placeholder="+1 234 567 890"
                                onChange={(e) => setFormData({...formData, phone: e.target.value})}
                                required
                            />
                        </div>
                    </div>
                    
                    <div className="space-y-3">
                        <label className="text-xs font-black text-slate-400 uppercase tracking-widest px-1">Physical Address</label>
                        <textarea 
                            className="w-full bg-slate-50/50 border border-slate-200 rounded-2xl py-4.5 px-6 outline-none focus:ring-4 focus:ring-indigo-500/10 focus:border-indigo-500 transition-all font-semibold placeholder:text-slate-300"
                            rows={3}
                            placeholder="Enter the full street address..."
                            onChange={(e) => setFormData({...formData, address: e.target.value})}
                            required
                        ></textarea>
                    </div>

                    <div className="pt-8 border-t border-slate-50 flex items-center justify-between">
                        <button type="button" className="text-sm font-bold text-slate-400 hover:text-slate-600 px-4 py-2 transition-colors">Discard Draft</button>
                        <Button 
                            type="submit" 
                            className="px-12 py-5 rounded-3xl text-lg shadow-xl shadow-indigo-600/20 bg-indigo-600 hover:bg-indigo-700 active:scale-[0.98] border-none"
                        >
                            {loading ? 'Processing...' : 'Create Institution & Generate Admin'}
                        </Button>
                    </div>
                </form>
            </div>
        </Layout>
    );
};

export default CreateInstitution;
