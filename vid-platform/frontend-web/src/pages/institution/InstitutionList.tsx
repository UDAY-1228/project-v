import React, { useState } from 'react';
import DashboardLayout from '../../components/layout/DashboardLayout';
import { Building2, Search, MoreVertical, Edit2, Trash2, Plus } from 'lucide-react';

const mockInstitutions = [
    { id: 'INST-001', name: 'Dolla Academic Excellence', code: 'DAE001', students: 1250, license: 'premium', status: 'Active' },
    { id: 'INST-002', name: 'Valley Regional High', code: 'VRH002', students: 850, license: 'standard', status: 'Active' },
    { id: 'INST-003', name: 'Springfield Academy', code: 'SFA003', students: 420, license: 'trial', status: 'Evaluating' }
];

const InstitutionList: React.FC = () => {
    const [searchTerm, setSearchTerm] = useState('');

    return (
        <DashboardLayout role="SuperAdmin">
            <div className="p-6">
                <div className="flex justify-between items-center mb-6">
                    <div>
                        <h1 className="text-3xl font-bold text-slate-800 dark:text-white">Institutions</h1>
                        <p className="text-slate-500 dark:text-slate-400 mt-1">Manage tenant institutions and their licenses</p>
                    </div>
                    <button className="bg-indigo-600 hover:bg-indigo-500 text-white px-5 py-2.5 rounded-xl font-medium flex items-center gap-2 shadow-lg shadow-indigo-600/20 transition-all">
                        <Plus className="w-5 h-5" />
                        Add Institution
                    </button>
                </div>

                <div className="bg-white dark:bg-slate-800 rounded-3xl shadow-xl border border-slate-100 dark:border-slate-700/50 overflow-hidden">
                    <div className="p-4 border-b border-slate-100 dark:border-slate-700/50 flex justify-between items-center bg-slate-50 dark:bg-slate-800/50">
                        <div className="relative w-96">
                            <Search className="absolute left-3 top-1/2 -translate-y-1/2 w-5 h-5 text-slate-400" />
                            <input 
                                type="text" 
                                placeholder="Search institutions..."
                                value={searchTerm}
                                onChange={(e) => setSearchTerm(e.target.value)}
                                className="w-full bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-700 rounded-lg py-2 pl-10 pr-4 focus:outline-none focus:ring-2 focus:ring-indigo-500/50 text-slate-800 dark:text-slate-200"
                            />
                        </div>
                    </div>

                    <div className="overflow-x-auto">
                        <table className="w-full text-left border-collapse">
                            <thead>
                                <tr className="bg-slate-50 dark:bg-slate-800/80 text-slate-500 dark:text-slate-400 text-sm uppercase tracking-wider">
                                    <th className="p-4 font-semibold">Name & Code</th>
                                    <th className="p-4 font-semibold">Students</th>
                                    <th className="p-4 font-semibold">License</th>
                                    <th className="p-4 font-semibold">Status</th>
                                    <th className="p-4 font-semibold text-right">Actions</th>
                                </tr>
                            </thead>
                            <tbody className="divide-y divide-slate-100 dark:divide-slate-700/50">
                                {mockInstitutions.filter(i => i.name.toLowerCase().includes(searchTerm.toLowerCase())).map(inst => (
                                    <tr key={inst.id} className="hover:bg-slate-50 dark:hover:bg-slate-700/20 transition-colors group">
                                        <td className="p-4">
                                            <div className="flex items-center gap-3">
                                                <div className="w-10 h-10 rounded-lg bg-indigo-500/10 flex items-center justify-center text-indigo-500">
                                                    <Building2 className="w-5 h-5" />
                                                </div>
                                                <div>
                                                    <p className="font-semibold text-slate-800 dark:text-white">{inst.name}</p>
                                                    <p className="text-xs text-slate-500">{inst.code}</p>
                                                </div>
                                            </div>
                                        </td>
                                        <td className="p-4 text-slate-600 dark:text-slate-300">
                                            {inst.students.toLocaleString()}
                                        </td>
                                        <td className="p-4">
                                            <span className={`px-3 py-1 text-xs font-semibold rounded-full capitalize ${
                                                inst.license === 'premium' ? 'bg-amber-100 text-amber-700 dark:bg-amber-500/10 dark:text-amber-400 border border-amber-200 dark:border-amber-500/20' : 
                                                inst.license === 'standard' ? 'bg-blue-100 text-blue-700 dark:bg-blue-500/10 dark:text-blue-400 border border-blue-200 dark:border-blue-500/20' : 
                                                'bg-slate-100 text-slate-700 dark:bg-slate-500/10 dark:text-slate-400 border border-slate-200 dark:border-slate-500/20'
                                            }`}>
                                                {inst.license}
                                            </span>
                                        </td>
                                        <td className="p-4">
                                            <span className={`flex items-center gap-1.5 text-sm font-medium ${
                                                inst.status === 'Active' ? 'text-emerald-500' : 'text-orange-500'
                                            }`}>
                                                <span className={`w-2 h-2 rounded-full ${inst.status === 'Active' ? 'bg-emerald-500' : 'bg-orange-500'}`}></span>
                                                {inst.status}
                                            </span>
                                        </td>
                                        <td className="p-4">
                                            <div className="flex items-center justify-end gap-2 opacity-0 group-hover:opacity-100 transition-opacity">
                                                <button className="p-2 text-slate-400 hover:text-indigo-500 hover:bg-slate-100 dark:hover:bg-slate-800 rounded-lg transition-colors">
                                                    <Edit2 className="w-4 h-4" />
                                                </button>
                                                <button className="p-2 text-slate-400 hover:text-red-500 hover:bg-red-50 dark:hover:bg-red-500/10 rounded-lg transition-colors">
                                                    <Trash2 className="w-4 h-4" />
                                                </button>
                                                <button className="p-2 text-slate-400 hover:text-slate-600 dark:hover:text-slate-300 rounded-lg transition-colors">
                                                    <MoreVertical className="w-4 h-4" />
                                                </button>
                                            </div>
                                        </td>
                                    </tr>
                                ))}
                            </tbody>
                        </table>
                    </div>
                </div>
            </div>
        </DashboardLayout>
    );
};

export default InstitutionList;
