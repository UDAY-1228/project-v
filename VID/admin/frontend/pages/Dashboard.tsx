import React from 'react';
import Layout from '../../../core/frontend/components/Layout';
import Card from '../../../core/frontend/components/Card';

const AdminDashboard: React.FC = () => {
    const sidebarItems = [
        { label: 'Overview', icon: 'dashboard', path: '/admin/dashboard' },
        { label: 'User Management', icon: 'groups', path: '/admin/users' },
        { label: 'Create User', icon: 'person_add', path: '/admin/create-user' },
        { label: 'Institution Settings', icon: 'settings', path: '/admin/settings' },
    ];

    return (
        <Layout sidebarItems={sidebarItems}>
            <div className="flex flex-col gap-12">
                <div>
                    <h1 className="text-4xl font-black text-slate-900 tracking-tight">Institutional Admin Console</h1>
                    <p className="text-slate-500 font-medium mt-1">Manage your campus users and system configurations</p>
                </div>

                <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-8">
                    <Card title="Total Users" value="24" icon="people" color="indigo" />
                    <Card title="Active Workspaces" value="13" icon="apps" color="blue" />
                    <Card title="System Alerts" value="0" icon="notifications" color="green" />
                    <Card title="Storage Used" value="1.2GB" icon="storage" color="yellow" />
                </div>

                <div className="bg-white p-12 rounded-[4rem] shadow-2xl shadow-indigo-100/20 border border-slate-100">
                    <h3 className="text-xl font-black text-slate-800 mb-8 px-2 tracking-tight">Quick Actions</h3>
                    <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
                        <a href="/admin/create-user" className="p-10 bg-slate-50 rounded-[2.5rem] border border-slate-100 hover:border-indigo-500 hover:bg-white transition-all group">
                            <div className="w-14 h-14 bg-white rounded-2xl shadow-md flex items-center justify-center text-indigo-500 group-hover:bg-indigo-500 group-hover:text-white transition-all mb-6">
                                <span className="material-icons">person_add</span>
                            </div>
                            <p className="font-black text-slate-800 tracking-tight">Add New User</p>
                            <p className="text-xs text-slate-400 mt-2 font-medium">Provision access for staff or students</p>
                        </a>
                        <a href="/admin/users" className="p-10 bg-slate-50 rounded-[2.5rem] border border-slate-100 hover:border-indigo-500 hover:bg-white transition-all group">
                            <div className="w-14 h-14 bg-white rounded-2xl shadow-md flex items-center justify-center text-emerald-500 group-hover:bg-emerald-500 group-hover:text-white transition-all mb-6">
                                <span className="material-icons">manage_accounts</span>
                            </div>
                            <p className="font-black text-slate-800 tracking-tight">Manage Roles</p>
                            <p className="text-xs text-slate-400 mt-2 font-medium">Update perms and access levels</p>
                        </a>
                        <a href="/admin/settings" className="p-10 bg-slate-50 rounded-[2.5rem] border border-slate-100 hover:border-indigo-500 hover:bg-white transition-all group">
                            <div className="w-14 h-14 bg-white rounded-2xl shadow-md flex items-center justify-center text-amber-500 group-hover:bg-amber-500 group-hover:text-white transition-all mb-6">
                                <span className="material-icons">settings</span>
                            </div>
                            <p className="font-black text-slate-800 tracking-tight">Config Cluster</p>
                            <p className="text-xs text-slate-400 mt-2 font-medium">Core institutional settings</p>
                        </a>
                    </div>
                </div>
            </div>
        </Layout>
    );
};

export default AdminDashboard;
