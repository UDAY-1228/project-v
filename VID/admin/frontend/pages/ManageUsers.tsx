import React, { useState, useEffect } from 'react';
import Layout from '../../../core/frontend/components/Layout';
import Button from '../../../core/frontend/components/Button';
import axios from 'axios';

const ManageUsers: React.FC = () => {
    const [users, setUsers] = useState<any[]>([]);
    const [loading, setLoading] = useState(true);

    const fetchUsers = async () => {
        try {
            const res = await axios.get('/api/admin/users');
            setUsers(res.data);
        } catch (err) {
            console.error('Failed to fetch users');
        } finally {
            setLoading(false);
        }
    };

    useEffect(() => {
        fetchUsers();
    }, []);

    return (
        <Layout sidebarItems={[
            { label: 'Overview', icon: 'dashboard', path: '/admin/dashboard' },
            { label: 'Manage Users', icon: 'groups', path: '/admin/users' },
            { label: 'Attendance', icon: 'event_available', path: '/admin/attendance' },
            { label: 'Academics', icon: 'school', path: '/admin/academic' },
            { label: 'Reports', icon: 'analytics', path: '/admin/reports' },
        ]}>
            <div className="flex flex-col gap-10">
                <div className="flex items-center justify-between">
                    <div>
                        <h1 className="text-4xl font-black text-slate-800 tracking-tight">Institutional Users</h1>
                        <p className="text-slate-500 font-medium">Manage your teachers, staff, and student accounts</p>
                    </div>
                    <Button className="px-10 py-5 rounded-3xl bg-indigo-600 border-none shadow-xl shadow-indigo-100 flex items-center gap-3">
                        <span className="material-icons text-white">person_add</span>
                        <span>Add New User</span>
                    </Button>
                </div>

                <div className="grid grid-cols-1 lg:grid-cols-4 gap-8">
                    {['Teachers', 'Students', 'Staff', 'Admin'].map((role) => (
                        <div key={role} className="bg-white p-8 rounded-[2.5rem] shadow-xl shadow-slate-200/50 border border-slate-100/50 hover:border-indigo-100 transition-all hover:translate-y-[-5px] cursor-pointer">
                            <h3 className="text-sm font-bold text-slate-400 uppercase tracking-widest mb-2 px-1">{role}</h3>
                            <div className="flex items-end justify-between">
                                <span className="text-4xl font-black text-slate-800">42</span>
                                <span className="text-xs font-bold text-emerald-500 bg-emerald-50 px-3 py-1.5 rounded-full">+12%</span>
                            </div>
                        </div>
                    ))}
                </div>

                <div className="bg-white rounded-[3.5rem] shadow-2xl shadow-indigo-100/20 border border-slate-100 overflow-hidden relative">
                    <div className="p-10 border-b border-slate-50 flex items-center justify-between bg-white sticky top-0 z-10">
                        <div className="flex items-center gap-8">
                            <h3 className="text-xl font-black text-slate-800 tracking-tight px-2">User Registry</h3>
                            <div className="flex bg-slate-100 p-1.5 rounded-2xl border border-slate-200">
                                <button className="px-6 py-2.5 rounded-xl bg-white shadow-md text-sm font-bold text-indigo-600 transition-all">All Users</button>
                                <button className="px-6 py-2.5 rounded-xl text-sm font-bold text-slate-500 hover:text-indigo-600 transition-all">Active Only</button>
                            </div>
                        </div>
                        <div className="flex items-center gap-4">
                            <div className="relative group">
                                <span className="absolute left-4 top-1/2 -translate-y-1/2 material-icons text-slate-400 text-lg">search</span>
                                <input type="text" placeholder="Search by name or email" className="bg-slate-50 border border-slate-200 rounded-2xl py-3 pl-12 pr-6 outline-none focus:border-indigo-400 transition-all text-sm font-medium w-80" />
                            </div>
                            <button className="p-3 bg-slate-50 border border-slate-200 rounded-2xl hover:bg-slate-100 transition-all text-slate-400">
                                <span className="material-icons">filter_list</span>
                            </button>
                        </div>
                    </div>

                    <div className="overflow-x-auto min-h-[500px]">
                        <table className="w-full text-left border-collapse">
                            <thead>
                                <tr className="bg-slate-50/50">
                                    <th className="px-10 py-6 text-xs font-black text-slate-400 uppercase tracking-widest">User Profile</th>
                                    <th className="px-10 py-6 text-xs font-black text-slate-400 uppercase tracking-widest">Role & Permissions</th>
                                    <th className="px-10 py-6 text-xs font-black text-slate-400 uppercase tracking-widest">Status</th>
                                    <th className="px-10 py-6 text-xs font-black text-slate-400 uppercase tracking-widest text-right pr-16">Actions</th>
                                </tr>
                            </thead>
                            <tbody>
                                {[1, 2, 3, 4, 5].map((i) => (
                                    <tr key={i} className="hover:bg-slate-50/100 border-b border-slate-50 transition-colors group">
                                        <td className="px-10 py-8">
                                            <div className="flex items-center gap-5">
                                                <div className="w-14 h-14 bg-indigo-50 rounded-2xl overflow-hidden border-2 border-white shadow-lg">
                                                    <img src={`https://ui-avatars.com/api/?name=User+${i}&background=random`} alt="User" />
                                                </div>
                                                <div>
                                                    <p className="font-bold text-slate-800 text-lg tracking-tight">User Number {i}</p>
                                                    <p className="text-sm text-slate-400 font-medium tracking-tight">user.{i}@institution.com</p>
                                                </div>
                                            </div>
                                        </td>
                                        <td className="px-10 py-8">
                                            <span className="px-5 py-2.5 rounded-2xl bg-indigo-50 text-indigo-600 text-xs font-black uppercase tracking-widest shadow-sm shadow-indigo-100/50">Teacher</span>
                                        </td>
                                        <td className="px-10 py-8">
                                            <div className="flex items-center gap-3">
                                                <span className="w-2.5 h-2.5 bg-emerald-500 rounded-full animate-pulse"></span>
                                                <span className="text-sm font-bold text-slate-600">Active</span>
                                            </div>
                                        </td>
                                        <td className="px-10 py-8 text-right pr-16">
                                            <div className="flex items-center justify-end gap-3 opacity-0 group-hover:opacity-100 transition-opacity">
                                                <button className="p-3 bg-white border border-slate-100 rounded-xl hover:border-indigo-400 hover:text-indigo-600 shadow-md text-slate-400 transition-all"><span className="material-icons text-xl">edit</span></button>
                                                <button className="p-3 bg-white border border-slate-100 rounded-xl hover:border-rose-400 hover:text-rose-600 shadow-md text-slate-400 transition-all"><span className="material-icons text-xl">delete_outline</span></button>
                                                <button className="p-3 bg-white border border-slate-100 rounded-xl hover:border-indigo-400 hover:text-indigo-600 shadow-md text-slate-400 transition-all"><span className="material-icons text-xl">more_horiz</span></button>
                                            </div>
                                        </td>
                                    </tr>
                                ))}
                            </tbody>
                        </table>
                    </div>
                    
                    <div className="p-10 border-t border-slate-50 flex items-center justify-between text-sm text-slate-400 font-bold uppercase tracking-widest">
                        <span>Showing 5 of 124 users</span>
                        <div className="flex items-center gap-4">
                            <button className="p-2 hover:text-indigo-600 transition-colors"><span className="material-icons">chevron_left</span></button>
                            <span className="bg-indigo-600 text-white px-5 py-2.5 rounded-xl shadow-lg shadow-indigo-100">1</span>
                            <button className="p-2 hover:text-indigo-600 transition-colors hover:bg-slate-50 rounded-xl transition-all">2</button>
                            <button className="p-2 hover:text-indigo-600 transition-colors hover:bg-slate-50 rounded-xl transition-all">3</button>
                            <button className="p-2 hover:text-indigo-600 transition-colors"><span className="material-icons">chevron_right</span></button>
                        </div>
                    </div>
                </div>
            </div>
        </Layout>
    );
};

export default ManageUsers;
