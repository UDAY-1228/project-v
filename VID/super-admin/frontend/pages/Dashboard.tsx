import React from 'react';
import Layout from '../../../core/frontend/components/Layout';
import Card from '../../core/frontend/components/Card'; // Not used here as we have custom ones

const SuperAdminDashboard: React.FC = () => {
    const sidebarItems = [
        { label: 'Add/Manage Institutions', icon: 'business', path: '/super-admin/institutions' },
        { label: 'Institution Analytics', icon: 'bar_chart', path: '/super-admin/analytics' },
        { label: 'Institution Switching', icon: 'swap_horiz', path: '/super-admin/switch' },
        { label: 'Issue Management', icon: 'bug_report', path: '/super-admin/issues' },
        { label: 'Health Dashboard', icon: 'monitor_heart', path: '/super-admin/health' },
        { label: 'Multi-tenancy Features', icon: 'groups_3', path: '/super-admin/tenancy' },
        { label: 'Admin Logs', icon: 'history', path: '/super-admin/logs' },
    ];

    return (
        <Layout sidebarItems={sidebarItems}>
            <div className="flex flex-col gap-12 max-w-7xl mx-auto">
                <div className="flex items-center justify-between">
                    <div>
                        <h1 className="text-5xl font-black text-slate-900 tracking-tight mb-2">CAMPUX <span className="text-indigo-600">CENTRAL</span></h1>
                        <p className="text-slate-400 text-lg font-medium tracking-tight uppercase tracking-widest text-[10px]">Super Admin Hub</p>
                    </div>
                    <div className="flex gap-4">
                        <button className="px-8 py-4 bg-indigo-50 text-indigo-600 rounded-3xl font-black text-sm uppercase tracking-widest border-2 border-indigo-100 hover:bg-indigo-100 hover:border-indigo-200 transition-all">Export Report</button>
                        <button className="px-10 py-4 bg-slate-900 text-white rounded-3xl font-black text-sm uppercase tracking-widest shadow-2xl shadow-slate-200 hover:bg-black transition-all">Manage System</button>
                    </div>
                </div>

                <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-8">
                    <div className="bg-white p-10 rounded-[3rem] shadow-2xl shadow-indigo-100/30 border border-slate-100/50 hover:translate-y-[-10px] transition-all cursor-pointer group">
                        <div className="w-16 h-16 bg-blue-50 text-blue-500 rounded-2xl flex items-center justify-center mb-6 group-hover:bg-blue-500 group-hover:text-white transition-all"><span className="material-icons text-3xl">business</span></div>
                        <h3 className="text-sm font-black text-slate-400 uppercase tracking-widest mb-2 px-1">Total institutions</h3>
                        <p className="text-5xl font-black text-slate-900 tracking-tight">124</p>
                    </div>
                    <div className="bg-white p-10 rounded-[3rem] shadow-2xl shadow-emerald-100/30 border border-slate-100/50 hover:translate-y-[-10px] transition-all cursor-pointer group">
                        <div className="w-16 h-16 bg-emerald-50 text-emerald-500 rounded-2xl flex items-center justify-center mb-6 group-hover:bg-emerald-500 group-hover:text-white transition-all"><span className="material-icons text-3xl">trending_up</span></div>
                        <h3 className="text-sm font-black text-slate-400 uppercase tracking-widest mb-2 px-1">Active users</h3>
                        <p className="text-5xl font-black text-slate-900 tracking-tight">45.2K</p>
                    </div>
                    <div className="bg-white p-10 rounded-[3rem] shadow-2xl shadow-rose-100/30 border border-slate-100/50 hover:translate-y-[-10px] transition-all cursor-pointer group">
                        <div className="w-16 h-16 bg-rose-50 text-rose-500 rounded-2xl flex items-center justify-center mb-6 group-hover:bg-rose-500 group-hover:text-white transition-all"><span className="material-icons text-3xl">currency_exchange</span></div>
                        <h3 className="text-sm font-black text-slate-400 uppercase tracking-widest mb-2 px-1">Revenue</h3>
                        <p className="text-5xl font-black text-slate-900 tracking-tight">$1.2M</p>
                    </div>
                    <div className="bg-white p-10 rounded-[3rem] shadow-2xl shadow-amber-100/30 border border-slate-100/50 hover:translate-y-[-10px] transition-all cursor-pointer group">
                        <div className="w-16 h-16 bg-amber-50 text-amber-500 rounded-2xl flex items-center justify-center mb-6 group-hover:bg-amber-500 group-hover:text-white transition-all"><span className="material-icons text-3xl">health_and_safety</span></div>
                        <h3 className="text-sm font-black text-slate-400 uppercase tracking-widest mb-2 px-1">System status</h3>
                        <p className="text-4xl font-black text-slate-900 tracking-tight uppercase tracking-widest">A++</p>
                    </div>
                </div>

                <div className="grid grid-cols-1 lg:grid-cols-3 gap-10">
                    <div className="lg:col-span-2 bg-white rounded-[4rem] shadow-2xl shadow-indigo-100/20 border border-slate-100 overflow-hidden">
                        <div className="p-12 border-b border-slate-50 flex items-center justify-between">
                            <h3 className="text-2xl font-black text-slate-800 tracking-tight flex items-center gap-4">
                                <span className="material-icons text-indigo-500">analytics</span>
                                Institutional Analytics
                            </h3>
                            <button className="text-sm font-black text-indigo-500 uppercase tracking-widest hover:text-indigo-700 transition-colors">Show More Details</button>
                        </div>
                        <div className="p-12 min-h-[400px]">
                            {/* Analytics chart dummy */}
                            <div className="flex items-end justify-between h-64 gap-6">
                                {[60, 45, 80, 55, 90, 75, 40].map((h, i) => (
                                    <div key={i} className="flex-1 bg-slate-100/50 rounded-2xl relative group overflow-hidden">
                                        <div 
                                            className="absolute bottom-0 w-full bg-gradient-to-t from-indigo-500 to-indigo-400 group-hover:from-indigo-600 group-hover:to-indigo-500 transition-all rounded-2xl" 
                                            style={{ height: `${h}%` }}
                                        ></div>
                                    </div>
                                ))}
                            </div>
                            <div className="flex justify-between mt-8 text-xs font-black text-slate-400 uppercase tracking-widest">
                                <span>Mon</span><span>Tue</span><span>Wed</span><span>Thu</span><span>Fri</span><span>Sat</span><span>Sun</span>
                            </div>
                        </div>
                    </div>

                    <div className="bg-slate-900 rounded-[4rem] p-12 text-white relative overflow-hidden shadow-2xl shadow-slate-400">
                        <div className="absolute top-0 right-0 w-64 h-64 bg-indigo-500/20 rounded-full blur-[100px] -translate-y-1/2 translate-x-1/2"></div>
                        <h3 className="text-2xl font-black mb-10 tracking-tight flex items-center gap-4">
                            <span className="material-icons text-indigo-400">notifications_active</span>
                            Latest Alerts
                        </h3>
                        <div className="space-y-8">
                            {[1, 2, 3].map(i => (
                                <div key={i} className="flex items-start gap-5 group cursor-pointer">
                                    <div className="w-12 h-12 bg-white/5 rounded-2xl flex-shrink-0 flex items-center justify-center border border-white/10 group-hover:bg-indigo-500 group-hover:border-indigo-400 transition-all">
                                        <span className="material-icons text-slate-400 group-hover:text-white text-lg">error_outline</span>
                                    </div>
                                    <div>
                                        <p className="font-bold text-slate-200 text-sm group-hover:text-white">Institution {i} Status Alert</p>
                                        <p className="text-xs text-slate-500 font-medium tracking-tight mt-1 leading-relaxed">The server response for GVA Academy has exceeded the threshold limit of 500ms.</p>
                                    </div>
                                </div>
                            ))}
                        </div>
                        <button className="w-full mt-12 py-5 bg-white/5 border border-white/10 rounded-3xl font-black text-sm uppercase tracking-widest hover:bg-white/10 transition-all active:scale-[0.98]">System Monitor</button>
                    </div>
                </div>
            </div>
        </Layout>
    );
};

export default SuperAdminDashboard;
