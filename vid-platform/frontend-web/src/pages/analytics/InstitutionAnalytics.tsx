import React, { useEffect, useState } from 'react';
import DashboardLayout from '../../components/layout/DashboardLayout';
import { getSummary } from '../../services/api';
import { 
    LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, ResponsiveContainer, 
    AreaChart, Area, BarChart, Bar 
} from 'recharts';
import { Users, BookOpen, Clock, IndianRupee, TrendingUp, Bell } from 'lucide-react';
import { motion } from 'framer-motion';

const StatCard = ({ title, value, icon: Icon, colorClass, trend }: any) => (
    <motion.div 
        initial={{ y: 20, opacity: 0 }}
        animate={{ y: 0, opacity: 1 }}
        className="bg-white dark:bg-slate-800 rounded-2xl p-6 shadow-xl border border-slate-100 dark:border-slate-700/50 hover:shadow-2xl transition-all"
    >
        <div className="flex justify-between items-start">
            <div>
                <p className="text-slate-500 dark:text-slate-400 text-sm font-medium">{title}</p>
                <h3 className="text-3xl font-bold text-slate-800 dark:text-white mt-2">{value}</h3>
                {trend && (
                    <p className="text-emerald-500 text-sm font-medium mt-2 flex items-center">
                        <TrendingUp className="w-4 h-4 mr-1" /> {trend}
                    </p>
                )}
            </div>
            <div className={`p-4 rounded-xl ${colorClass}`}>
                <Icon className="w-6 h-6 text-white" />
            </div>
        </div>
    </motion.div>
);

const InstitutionAnalytics: React.FC = () => {
    const [summary, setSummary] = useState<any>(null);

    useEffect(() => {
        getSummary().then(data => setSummary(data)).catch(console.error);
    }, []);

    if (!summary) {
        return (
            <DashboardLayout role="Admin">
                <div className="p-6">
                    <div className="animate-pulse space-y-6">
                        <div className="h-8 bg-slate-200 dark:bg-slate-700 rounded w-1/4"></div>
                        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
                            {[1, 2, 3, 4].map(i => <div key={i} className="h-32 bg-slate-200 dark:bg-slate-700 rounded-2xl"></div>)}
                        </div>
                    </div>
                </div>
            </DashboardLayout>
        );
    }

    const revenueData = summary.revenue_trend.map((val: number, idx: number) => ({ name: `Month ${idx + 1}`, value: val }));
    const attendanceData = summary.attendance_trend.map((val: number, idx: number) => ({ name: `Day ${idx + 1}`, value: val }));

    return (
        <DashboardLayout role="Admin">
            <div className="p-6 space-y-6">
                <div>
                    <h1 className="text-3xl font-bold text-slate-800 dark:text-white">Institution Overview</h1>
                    <p className="text-slate-500 dark:text-slate-400 mt-1">Key metrics and performance indicators</p>
                </div>

                <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
                    <StatCard title="Total Students" value={summary.students} icon={Users} colorClass="bg-indigo-500" trend="+12% this month" />
                    <StatCard title="Total Teachers" value={summary.teachers} icon={BookOpen} colorClass="bg-purple-500" />
                    <StatCard title="Avg Attendance" value={summary.attendance_rate + '%'} icon={Clock} colorClass="bg-emerald-500" trend="+2.5% this week" />
                    <StatCard title="Fees Collected" value={'₹ ' + summary.fees_collected} icon={IndianRupee} colorClass="bg-orange-500" />
                </div>

                <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
                    <div className="bg-white dark:bg-slate-800 rounded-2xl shadow-xl p-6 border border-slate-100 dark:border-slate-700/50">
                        <h3 className="text-lg font-semibold text-slate-800 dark:text-white mb-6">Revenue Trend</h3>
                        <div className="h-72">
                            <ResponsiveContainer width="100%" height="100%">
                                <AreaChart data={revenueData}>
                                    <defs>
                                        <linearGradient id="colorRevenue" x1="0" y1="0" x2="0" y2="1">
                                            <stop offset="5%" stopColor="#6366f1" stopOpacity={0.3}/>
                                            <stop offset="95%" stopColor="#6366f1" stopOpacity={0}/>
                                        </linearGradient>
                                    </defs>
                                    <CartesianGrid strokeDasharray="3 3" stroke="#334155" opacity={0.2} vertical={false} />
                                    <XAxis dataKey="name" stroke="#64748b" fontSize={12} tickLine={false} axisLine={false} />
                                    <YAxis stroke="#64748b" fontSize={12} tickLine={false} axisLine={false} tickFormatter={(value) => `₹${value}`} />
                                    <Tooltip 
                                        contentStyle={{ backgroundColor: '#1e293b', border: 'none', borderRadius: '12px', color: '#f8fafc' }}
                                        itemStyle={{ color: '#818cf8' }}
                                    />
                                    <Area type="monotone" dataKey="value" stroke="#6366f1" strokeWidth={3} fillOpacity={1} fill="url(#colorRevenue)" />
                                </AreaChart>
                            </ResponsiveContainer>
                        </div>
                    </div>

                    <div className="bg-white dark:bg-slate-800 rounded-2xl shadow-xl p-6 border border-slate-100 dark:border-slate-700/50">
                        <h3 className="text-lg font-semibold text-slate-800 dark:text-white mb-6">Attendance Trend</h3>
                        <div className="h-72">
                            <ResponsiveContainer width="100%" height="100%">
                                <BarChart data={attendanceData}>
                                    <CartesianGrid strokeDasharray="3 3" stroke="#334155" opacity={0.2} vertical={false} />
                                    <XAxis dataKey="name" stroke="#64748b" fontSize={12} tickLine={false} axisLine={false} />
                                    <YAxis stroke="#64748b" fontSize={12} tickLine={false} axisLine={false} domain={[80, 100]} />
                                    <Tooltip 
                                        contentStyle={{ backgroundColor: '#1e293b', border: 'none', borderRadius: '12px', color: '#f8fafc' }}
                                        cursor={{ fill: '#334155', opacity: 0.1 }}
                                    />
                                    <Bar dataKey="value" fill="#10b981" radius={[4, 4, 0, 0]} barSize={24} />
                                </BarChart>
                            </ResponsiveContainer>
                        </div>
                    </div>
                </div>
            </div>
        </DashboardLayout>
    );
};

export default InstitutionAnalytics;
