import React, { useState } from 'react';
import DashboardLayout from '../../components/layout/DashboardLayout';
import { Calendar, Clock, MapPin, UserCheck, BookOpen } from 'lucide-react';
import { motion } from 'framer-motion';

const DAYS = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'];
const PERIODS = [
    { time: '09:00 - 09:45', name: '1st Period' },
    { time: '09:45 - 10:30', name: '2nd Period' },
    { time: '10:30 - 10:45', name: 'Break', isBreak: true },
    { time: '10:45 - 11:30', name: '3rd Period' },
    { time: '11:30 - 12:15', name: '4th Period' },
    { time: '12:15 - 13:00', name: 'Lunch', isBreak: true },
    { time: '13:00 - 13:45', name: '5th Period' },
    { time: '13:45 - 14:30', name: '6th Period' },
];

const mockSchedule: any = {
    'Monday': [
        { subject: 'Mathematics', teacher: 'Dr. Sarah Wilson', room: 'R-101', color: 'bg-blue-500' },
        { subject: 'Physics', teacher: 'Prof. James Chen', room: 'L-204', color: 'bg-emerald-500' },
        null,
        { subject: 'English Lit.', teacher: 'Ms. Emily Bronte', room: 'R-302', color: 'bg-purple-500' },
        { subject: 'Computer Sci', teacher: 'Mr. Alan Turing', room: 'Lab-1', color: 'bg-indigo-500' },
        null,
        { subject: 'Chemistry', teacher: 'Dr. Marie Curie', room: 'L-105', color: 'bg-orange-500' },
        { subject: 'P.E.', teacher: 'Mr. Jack Coach', room: 'Gym', color: 'bg-rose-500' }
    ],
    'Tuesday': [
        { subject: 'Computer Sci', teacher: 'Mr. Alan Turing', room: 'Lab-1', color: 'bg-indigo-500' },
        { subject: 'Mathematics', teacher: 'Dr. Sarah Wilson', room: 'R-101', color: 'bg-blue-500' },
        null,
        { subject: 'Physics', teacher: 'Prof. James Chen', room: 'L-204', color: 'bg-emerald-500' },
        { subject: 'English Lit.', teacher: 'Ms. Emily Bronte', room: 'R-302', color: 'bg-purple-500' },
        null,
        { subject: 'Art', teacher: 'Mrs. D. Vinci', room: 'Art-Rt', color: 'bg-pink-500' },
        { subject: 'Chemistry', teacher: 'Dr. Marie Curie', room: 'L-105', color: 'bg-orange-500' }
    ]
};

const MyTimetableStudent: React.FC = () => {
    const [selectedDay, setSelectedDay] = useState(DAYS[0]);

    return (
        <DashboardLayout role="Student">
            <div className="p-6">
                <div className="flex flex-col md:flex-row justify-between items-start md:items-center mb-8 gap-4">
                    <div>
                        <h1 className="text-3xl font-bold text-slate-800 dark:text-white">My Timetable</h1>
                        <p className="text-slate-500 dark:text-slate-400 mt-1">Grade 10, Section A - Current Week</p>
                    </div>
                    <div className="flex bg-slate-100 dark:bg-slate-800 p-1 rounded-xl">
                        {DAYS.map(day => (
                            <button
                                key={day}
                                onClick={() => setSelectedDay(day)}
                                className={`px-4 py-2 rounded-lg text-sm font-medium transition-all ${
                                    selectedDay === day 
                                    ? 'bg-white dark:bg-slate-700 text-indigo-600 dark:text-indigo-400 shadow-sm' 
                                    : 'text-slate-600 dark:text-slate-400 hover:text-slate-900 dark:hover:text-white'
                                }`}
                            >
                                {day.substring(0, 3)}
                            </button>
                        ))}
                    </div>
                </div>

                <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4">
                    {PERIODS.map((period, index) => {
                        if (period.isBreak) {
                            return (
                                <div key={index} className="col-span-1 md:col-span-2 lg:col-span-4 bg-slate-100 dark:bg-slate-800/50 rounded-2xl p-4 flex items-center justify-center border border-slate-200 dark:border-slate-700/50">
                                    <div className="flex items-center gap-2 text-slate-500 dark:text-slate-400 font-medium">
                                        <Clock className="w-5 h-5" />
                                        <span>{period.time} - {period.name}</span>
                                    </div>
                                </div>
                            );
                        }

                        const daySchedule = mockSchedule[selectedDay] || mockSchedule['Monday'];
                        const classData = daySchedule[index];

                        return (
                            <motion.div 
                                key={index}
                                initial={{ opacity: 0, y: 10 }}
                                animate={{ opacity: 1, y: 0 }}
                                transition={{ delay: index * 0.05 }}
                                className={`rounded-2xl p-5 border shadow-sm hover:shadow-md transition-all ${classData ? 'bg-white dark:bg-slate-800 border-slate-200 dark:border-slate-700' : 'bg-slate-50 dark:bg-slate-900/50 border-dashed border-slate-300 dark:border-slate-700'}`}
                            >
                                <div className="flex justify-between items-start mb-4">
                                    <span className="text-xs font-semibold px-2.5 py-1 rounded-full bg-slate-100 dark:bg-slate-700 text-slate-600 dark:text-slate-300">
                                        {period.time}
                                    </span>
                                    {classData && (
                                        <span className={`w-3 h-3 rounded-full ${classData.color}`}></span>
                                    )}
                                </div>
                                
                                {classData ? (
                                    <>
                                        <h3 className="text-xl font-bold text-slate-800 dark:text-white mb-3">
                                            {classData.subject}
                                        </h3>
                                        <div className="space-y-2">
                                            <div className="flex items-center gap-2 text-sm text-slate-600 dark:text-slate-400">
                                                <UserCheck className="w-4 h-4" />
                                                <span>{classData.teacher}</span>
                                            </div>
                                            <div className="flex items-center gap-2 text-sm text-slate-600 dark:text-slate-400">
                                                <MapPin className="w-4 h-4" />
                                                <span>{classData.room}</span>
                                            </div>
                                        </div>
                                    </>
                                ) : (
                                    <div className="h-full flex flex-col items-center justify-center text-slate-400 dark:text-slate-600 py-4">
                                        <BookOpen className="w-8 h-8 mb-2 opacity-50" />
                                        <span className="text-sm font-medium">Free Study</span>
                                    </div>
                                )}
                            </motion.div>
                        );
                    })}
                </div>
            </div>
        </DashboardLayout>
    );
};

export default MyTimetableStudent;
