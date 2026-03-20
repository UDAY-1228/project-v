import React, { useState } from 'react';
import Layout from '../../../core/frontend/components/Layout';
import Button from '../../../core/frontend/components/Button';
import axios from 'axios';

const CreateUser: React.FC = () => {
    const [formData, setFormData] = useState({
        name: '', 
        role: 'teacher', 
        username: '', 
        password: '', 
        assignedWorkspaces: [] as string[]
    });
    const [loading, setLoading] = useState(false);
    const [success, setSuccess] = useState(false);

    const workspacesList = [
        { id: "principal", name: "Principal Dashboard" },
        { id: "academic-coordinator", name: "Academic Coordinator" },
        { id: "admission-officer", name: "Admission Officer" },
        { id: "admissions-counselor", name: "Admissions Counselor" },
        { id: "common", name: "Common (UMS)" },
        { id: "team-owner", name: "Team Owner" },
        { id: "transport-coordinator", name: "Transport Coordinator" },
        { id: "employee", name: "Employee Portal" },
        { id: "hostel-admin", name: "Hostel Admin" },
        { id: "payment-administrator", name: "Payment Administrator" },
        { id: "examination", name: "Examination Center" },
        { id: "faculty", name: "Faculty Portal" },
        { id: "student", name: "Student Central" }
    ];

    const roles = [
        { value: "principal", label: "Principal" },
        { value: "vice-principal", label: "Vice Principal" },
        { value: "fees-coordinator", label: "Fees Coordinator" },
        { value: "manager", label: "Manager" },
        { value: "accounts", label: "Accounts" },
        { value: "teacher", label: "Teacher" },
        { value: "academic-coordinator", label: "Academic Coordinator" },
        { value: "student", label: "Student" },
        { value: "transport-coordinator", label: "Transport Coordinator" },
        { value: "admission-officer", label: "Admission Officer" },
        { value: "employee", label: "Employee" },
        { value: "others", label: "Others" }
    ];

    const handleCheckboxChange = (ws: string) => {
        setFormData(prev => ({
            ...prev,
            assignedWorkspaces: prev.assignedWorkspaces.includes(ws)
                ? prev.assignedWorkspaces.filter(item => item !== ws)
                : [...prev.assignedWorkspaces, ws]
        }));
    };

    const handleSubmit = async (e: React.FormEvent) => {
        e.preventDefault();
        if (formData.assignedWorkspaces.length === 0) {
            alert('Please assign at least one workspace.');
            return;
        }
        setLoading(true);
        try {
            const user = JSON.parse(localStorage.getItem('user_data') || '{}');
            await axios.post('/api/admin/users', {
                ...formData,
                institutionId: user.institutionId
            });
            setSuccess(true);
            setFormData({ name: '', role: 'teacher', username: '', password: '', assignedWorkspaces: [] });
            window.scrollTo({ top: 0, behavior: 'smooth' });
        } catch (err) {
            alert('Failed to create user. Please check if username already exists.');
        } finally {
            setLoading(false);
        }
    };

    return (
        <Layout sidebarItems={[
            { label: 'Overview', icon: 'dashboard', path: '/admin/dashboard' },
            { label: 'Manage Users', icon: 'groups', path: '/admin/users' },
            { label: 'Create User', icon: 'person_add', path: '/admin/create-user' },
        ]}>
            <div className="max-w-6xl mx-auto pb-20">
                <div className="mb-12 flex items-center justify-between">
                    <div>
                        <h1 className="text-4xl font-black text-slate-900 tracking-tight">User Provisioning</h1>
                        <p className="text-slate-500 font-medium tracking-tight mt-1">Configure roles and workspace access for institutional members</p>
                    </div>
                </div>

                {success && (
                    <div className="mb-10 p-8 bg-emerald-500 rounded-[2.5rem] shadow-2xl shadow-emerald-200 text-white flex items-center gap-6 animate-in fade-in slide-in-from-top-4 duration-500">
                        <div className="w-16 h-16 bg-white/20 rounded-2xl flex items-center justify-center">
                            <span className="material-icons text-3xl">done_all</span>
                        </div>
                        <div>
                            <p className="text-xl font-black">Success!</p>
                            <p className="text-emerald-50 font-medium tracking-tight opacity-90">User account created and permissions synced across all clusters.</p>
                        </div>
                        <button onClick={() => setSuccess(false)} className="ml-auto bg-white/10 hover:bg-white/20 p-4 rounded-2xl transition-all">
                            <span className="material-icons">close</span>
                        </button>
                    </div>
                )}

                <form className="grid grid-cols-1 lg:grid-cols-3 gap-10" onSubmit={handleSubmit}>
                    <div className="lg:col-span-2 space-y-10">
                        <div className="bg-white p-12 rounded-[3.5rem] shadow-2xl shadow-slate-200/40 border border-slate-100 flex flex-col gap-10">
                            <h3 className="text-xl font-black text-slate-800 tracking-tight flex items-center gap-4">
                                <span className="w-2 h-8 bg-indigo-500 rounded-full"></span>
                                Primary Details
                            </h3>
                            
                            <div className="grid grid-cols-1 md:grid-cols-2 gap-8">
                                <div className="space-y-3">
                                    <label className="text-[10px] font-black text-slate-400 uppercase tracking-[0.2em] px-1">Full Identity Name</label>
                                    <input 
                                        className="w-full bg-slate-50/50 border-2 border-slate-100 rounded-3xl py-5 px-8 outline-none focus:border-indigo-500 focus:bg-white transition-all font-bold placeholder:text-slate-300"
                                        placeholder="E.g. Dr. Robert Wilson"
                                        value={formData.name}
                                        onChange={e => setFormData({...formData, name: e.target.value})}
                                        required
                                    />
                                </div>
                                <div className="space-y-3">
                                    <label className="text-[10px] font-black text-slate-400 uppercase tracking-[0.2em] px-1">Institutional Position</label>
                                    <select 
                                        className="w-full bg-slate-50/50 border-2 border-slate-100 rounded-3xl py-5 px-8 outline-none focus:border-indigo-500 focus:bg-white transition-all font-bold text-slate-700 cursor-pointer appearance-none"
                                        value={formData.role}
                                        onChange={e => setFormData({...formData, role: e.target.value})}
                                    >
                                        {roles.map(role => (
                                            <option key={role.value} value={role.value}>{role.label}</option>
                                        ))}
                                    </select>
                                </div>
                                <div className="space-y-3">
                                    <label className="text-[10px] font-black text-slate-400 uppercase tracking-[0.2em] px-1">Auth Identifier</label>
                                    <input 
                                        className="w-full bg-slate-50/50 border-2 border-slate-100 rounded-3xl py-5 px-8 outline-none focus:border-indigo-500 focus:bg-white transition-all font-bold placeholder:text-slate-300"
                                        placeholder="username or email"
                                        value={formData.username}
                                        onChange={e => setFormData({...formData, username: e.target.value})}
                                        required
                                    />
                                </div>
                                <div className="space-y-3">
                                    <label className="text-[10px] font-black text-slate-400 uppercase tracking-[0.2em] px-1">Security Key</label>
                                    <input 
                                        type="password"
                                        className="w-full bg-slate-50/50 border-2 border-slate-100 rounded-3xl py-5 px-8 outline-none focus:border-indigo-500 focus:bg-white transition-all font-bold placeholder:text-slate-300"
                                        placeholder="••••••••"
                                        value={formData.password}
                                        onChange={e => setFormData({...formData, password: e.target.value})}
                                        required
                                    />
                                </div>
                            </div>
                        </div>

                        <div className="bg-white p-12 rounded-[3.5rem] shadow-2xl shadow-slate-200/40 border border-slate-100">
                            <h3 className="text-xl font-black text-slate-800 tracking-tight flex items-center gap-4 mb-10">
                                <span className="w-2 h-8 bg-violet-500 rounded-full"></span>
                                Granular Workspace Entitlements
                            </h3>
                            <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                                {workspacesList.map(ws => (
                                    <div 
                                        key={ws.id} 
                                        className={`group flex items-center justify-between p-6 rounded-3xl border-2 transition-all cursor-pointer ${formData.assignedWorkspaces.includes(ws.id) ? 'border-indigo-500 bg-indigo-50/50' : 'border-slate-50 bg-slate-50 hover:border-slate-200'}`}
                                        onClick={() => handleCheckboxChange(ws.id)}
                                    >
                                        <div className="flex items-center gap-4">
                                            <div className={`w-10 h-10 rounded-xl flex items-center justify-center transition-all ${formData.assignedWorkspaces.includes(ws.id) ? 'bg-indigo-500 text-white' : 'bg-white text-slate-300 group-hover:text-slate-500'}`}>
                                                <span className="material-icons text-xl">{formData.assignedWorkspaces.includes(ws.id) ? 'check' : 'add'}</span>
                                            </div>
                                            <span className={`text-[11px] font-black uppercase tracking-widest ${formData.assignedWorkspaces.includes(ws.id) ? 'text-indigo-600' : 'text-slate-400 group-hover:text-slate-700'}`}>{ws.name}</span>
                                        </div>
                                        <input 
                                            type="checkbox"
                                            className="hidden"
                                            checked={formData.assignedWorkspaces.includes(ws.id)}
                                            onChange={() => {}} // Controlled component
                                        />
                                    </div>
                                ))}
                            </div>
                        </div>
                    </div>

                    <div className="space-y-10">
                        <div className="bg-slate-900 rounded-[3.5rem] p-10 text-white shadow-2xl shadow-slate-300 relative overflow-hidden">
                            <div className="absolute top-0 right-0 w-32 h-32 bg-indigo-500/20 rounded-full blur-3xl -translate-y-1/2 translate-x-1/2"></div>
                            <h4 className="text-lg font-black mb-6 tracking-tight">Provisioning Summary</h4>
                            <div className="space-y-6">
                                <div className="flex justify-between items-center text-sm">
                                    <span className="text-slate-400 font-bold">Assigned Role</span>
                                    <span className="font-black text-indigo-400 capitalize">{formData.role.replace('-', ' ')}</span>
                                </div>
                                <div className="flex justify-between items-center text-sm">
                                    <span className="text-slate-400 font-bold">Workspaces</span>
                                    <span className="font-black text-indigo-400">{formData.assignedWorkspaces.length} Selected</span>
                                </div>
                                <div className="pt-6 border-t border-white/5 space-y-4">
                                    <p className="text-[10px] font-black text-slate-500 uppercase tracking-[0.2em]">Active Permissions</p>
                                    <div className="flex flex-wrap gap-2">
                                        {formData.assignedWorkspaces.map(ws => (
                                            <span key={ws} className="px-3 py-1 bg-white/5 rounded-lg text-[9px] font-black text-indigo-300 border border-white/5 uppercase tracking-widest">{ws.split('-')[0]}</span>
                                        ))}
                                        {formData.assignedWorkspaces.length === 0 && <span className="text-slate-600 font-bold text-xs">No workspaces assigned</span>}
                                    </div>
                                </div>
                            </div>
                            <Button 
                                type="submit" 
                                className="w-full mt-10 py-6 rounded-3xl text-sm font-black uppercase tracking-widest shadow-2xl shadow-indigo-600/30 bg-indigo-600 text-white border-none hover:bg-indigo-500 transition-all active:scale-95"
                                disabled={loading}
                            >
                                {loading ? 'Processing...' : 'Sync & Activate Access'}
                            </Button>
                        </div>

                        <div className="bg-indigo-50 rounded-[3rem] p-10 border border-indigo-100">
                            <h5 className="text-indigo-900 font-black text-sm mb-4">Security Advisory</h5>
                            <p className="text-indigo-600/70 text-xs font-medium leading-relaxed">
                                Once provisioned, the user will receive a system notification. You can revoke access or re-assign workspaces at any time from the Manage Users panel.
                            </p>
                        </div>
                    </div>
                </form>
            </div>
        </Layout>
    );
};

export default CreateUser;
