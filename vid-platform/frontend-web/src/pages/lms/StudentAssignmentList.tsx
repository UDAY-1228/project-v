import React, { useState } from 'react';
import DashboardLayout from '../../components/layout/DashboardLayout';
import { BookOpen, Calendar, Clock, CheckCircle2, AlertCircle, FileText, ChevronRight } from 'lucide-react';

const mockAssignments = [
    { id: '1', title: 'Calculus Advanced Derivatives', course: 'Mathematics', dueDate: '2024-03-25T23:59:00', status: 'Pending', type: 'Quiz', points: 100 },
    { id: '2', title: 'Quantum Physics Report', course: 'Physics', dueDate: '2024-03-28T17:00:00', status: 'Submitted', type: 'Report', points: 50 },
    { id: '3', title: 'Shakespeare Essay', course: 'English Literature', dueDate: '2024-03-15T23:59:00', status: 'Graded', type: 'Essay', points: 100, score: 92 },
    { id: '4', title: 'Cell Biology Lab', course: 'Biology', dueDate: '2024-03-22T23:59:00', status: 'Late', type: 'Lab', points: 20 },
];

const getStatusStyle = (status: string) => {
    switch(status) {
        case 'Pending': return 'bg-amber-100 text-amber-700 dark:bg-amber-500/10 dark:text-amber-400 border-amber-200 dark:border-amber-500/20';
        case 'Submitted': return 'bg-blue-100 text-blue-700 dark:bg-blue-500/10 dark:text-blue-400 border-blue-200 dark:border-blue-500/20';
        case 'Graded': return 'bg-emerald-100 text-emerald-700 dark:bg-emerald-500/10 dark:text-emerald-400 border-emerald-200 dark:border-emerald-500/20';
        case 'Late': return 'bg-rose-100 text-rose-700 dark:bg-rose-500/10 dark:text-rose-400 border-rose-200 dark:border-rose-500/20';
        default: return 'bg-slate-100 text-slate-700 dark:bg-slate-500/10 dark:text-slate-400 border-slate-200 dark:border-slate-500/20';
    }
};

const getStatusIcon = (status: string) => {
    switch(status) {
        case 'Graded': return <CheckCircle2 className="w-4 h-4" />;
        case 'Late': return <AlertCircle className="w-4 h-4" />;
        case 'Pending': return <Clock className="w-4 h-4" />;
        case 'Submitted': return <FileText className="w-4 h-4" />;
        default: return <BookOpen className="w-4 h-4" />;
    }
};

const StudentAssignmentList: React.FC = () => {
    const [filter, setFilter] = useState('All');

    const filteredAssignments = filter === 'All' ? mockAssignments : mockAssignments.filter(a => a.status === filter);

    return (
        <DashboardLayout role="Student">
            <div className="p-6">
                <div className="flex flex-col md:flex-row justify-between items-start md:items-center mb-8 gap-4">
                    <div>
                        <h1 className="text-3xl font-bold text-slate-800 dark:text-white">Assignments</h1>
                        <p className="text-slate-500 dark:text-slate-400 mt-1">Track and submit your coursework</p>
                    </div>
                    <div className="flex bg-slate-100 dark:bg-slate-800 p-1 rounded-xl shrink-0">
                        {['All', 'Pending', 'Submitted', 'Graded'].map(f => (
                            <button
                                key={f}
                                onClick={() => setFilter(f)}
                                className={`px-4 py-2 rounded-lg text-sm font-medium transition-all ${
                                    filter === f 
                                    ? 'bg-white dark:bg-slate-700 text-indigo-600 dark:text-indigo-400 shadow-sm' 
                                    : 'text-slate-600 dark:text-slate-400 hover:text-slate-900 dark:hover:text-white'
                                }`}
                            >
                                {f}
                            </button>
                        ))}
                    </div>
                </div>

                <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
                    {filteredAssignments.map((assignment) => (
                        <div key={assignment.id} className="bg-white dark:bg-slate-800 rounded-2xl shadow-sm border border-slate-200 dark:border-slate-700/50 hover:shadow-xl hover:border-indigo-500/30 transition-all group flex flex-col">
                            <div className="p-6 flex-1">
                                <div className="flex justify-between items-start mb-4">
                                    <span className="text-xs font-semibold px-3 py-1 bg-slate-100 dark:bg-slate-700 text-slate-600 dark:text-slate-300 rounded-full">
                                        {assignment.course}
                                    </span>
                                    <span className={`px-3 py-1 flex items-center gap-1.5 text-xs font-semibold border rounded-full ${getStatusStyle(assignment.status)}`}>
                                        {getStatusIcon(assignment.status)}
                                        {assignment.status}
                                    </span>
                                </div>
                                <h3 className="text-lg font-bold text-slate-800 dark:text-white leading-tight mb-2 group-hover:text-indigo-600 dark:group-hover:text-indigo-400 transition-colors">
                                    {assignment.title}
                                </h3>
                                
                                <div className="mt-4 space-y-2">
                                    <div className="flex items-center text-sm text-slate-500 dark:text-slate-400">
                                        <Calendar className="w-4 h-4 mr-2" />
                                        Due: {new Date(assignment.dueDate).toLocaleDateString()}
                                    </div>
                                    <div className="flexItems-center text-sm text-slate-500 dark:text-slate-400">
                                        <FileText className="w-4 h-4 mr-2 inline" />
                                        {assignment.type} • {assignment.points} Points
                                    </div>
                                    
                                    {assignment.status === 'Graded' && (
                                        <div className="mt-4 pt-4 border-t border-slate-100 dark:border-slate-700/50 flex justify-between items-center">
                                            <span className="text-sm font-medium text-slate-500 dark:text-slate-400">Score</span>
                                            <span className="text-xl font-bold text-emerald-600 dark:text-emerald-400">{assignment.score}/{assignment.points}</span>
                                        </div>
                                    )}
                                </div>
                            </div>
                            
                            <div className="p-4 bg-slate-50 dark:bg-slate-800/50 border-t border-slate-100 dark:border-slate-700/50 rounded-b-2xl">
                                <button className="w-full justify-between items-center flex text-sm font-semibold text-indigo-600 dark:text-indigo-400 hover:text-indigo-700 dark:hover:text-indigo-300">
                                    {assignment.status === 'Pending' ? 'Start Assignment' : 'View Details'}
                                    <ChevronRight className="w-4 h-4" />
                                </button>
                            </div>
                        </div>
                    ))}
                    
                    {filteredAssignments.length === 0 && (
                        <div className="col-span-1 md:col-span-2 lg:col-span-3 text-center py-12">
                            <BookOpen className="w-16 h-16 text-slate-300 dark:text-slate-600 mx-auto mb-4" />
                            <h3 className="text-xl font-semibold text-slate-700 dark:text-slate-300">No Assignments Found</h3>
                            <p className="text-slate-500 mt-2">You don't have any {filter.toLowerCase()} assignments right now.</p>
                        </div>
                    )}
                </div>
            </div>
        </DashboardLayout>
    );
};

export default StudentAssignmentList;
