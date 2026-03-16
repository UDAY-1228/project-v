import React, { useState } from 'react';
import DashboardLayout from '../../components/layout/DashboardLayout';
import { Bell, Megaphone, Calendar as CalendarIcon, FileText, Star, MessageCircle, Share2, MoreHorizontal } from 'lucide-react';
import { motion } from 'framer-motion';

const mockFeed = [
    {
        id: 1,
        author: 'Principal Office',
        role: 'Admin',
        avatar: 'P',
        type: 'important',
        title: 'Annual Sports Day 2024 Registration',
        content: 'Dear Students, the registration for the Annual Sports Day is now open. Please register for track and field events before the end of this week. Late registrations will not be accepted.',
        time: '2 hours ago',
        likes: 124,
        comments: 45,
    },
    {
        id: 2,
        author: 'Dr. Sarah Wilson',
        role: 'Teacher',
        avatar: 'SW',
        type: 'academic',
        title: 'Mid-Term Revision Guidelines',
        content: 'I have uploaded the revision guidelines and previous year question papers for Mathematics. Please review them carefully. Extra doubt-clearing sessions will be held next Monday.',
        time: '5 hours ago',
        likes: 89,
        comments: 12,
        attachments: [{ name: 'Math_Revision_Plan.pdf', size: '2.4 MB' }]
    },
    {
        id: 3,
        author: 'Library Admin',
        role: 'Staff',
        avatar: 'L',
        type: 'general',
        title: 'New Books Arrival',
        content: 'We are excited to announce that over 500 new titles have been added to the library collection, including the latest STEM reference materials. Drop by to check them out!',
        time: '1 day ago',
        likes: 245,
        comments: 18,
    }
];

const Feed: React.FC = () => {
    const [filter, setFilter] = useState('All');

    return (
        <DashboardLayout role="Student">
            <div className="p-6 max-w-4xl mx-auto">
                <div className="flex flex-col md:flex-row justify-between items-start md:items-center mb-8 gap-4">
                    <div>
                        <h1 className="text-3xl font-bold text-slate-800 dark:text-white">Notice Board Feed</h1>
                        <p className="text-slate-500 dark:text-slate-400 mt-1">Stay updated with latest announcements</p>
                    </div>
                </div>

                <div className="flex bg-slate-100 dark:bg-slate-800 p-1 rounded-xl w-max mb-6">
                    {['All', 'Important', 'Academic', 'General'].map(f => (
                        <button
                            key={f}
                            onClick={() => setFilter(f)}
                            className={`px-6 py-2 rounded-lg text-sm font-medium transition-all ${
                                filter === f 
                                ? 'bg-white dark:bg-slate-700 text-indigo-600 dark:text-indigo-400 shadow-sm' 
                                : 'text-slate-600 dark:text-slate-400 hover:text-slate-900 dark:hover:text-white'
                            }`}
                        >
                            {f}
                        </button>
                    ))}
                </div>

                <div className="space-y-6">
                    {mockFeed.map((post, idx) => (
                        <motion.div 
                            key={post.id}
                            initial={{ opacity: 0, y: 20 }}
                            animate={{ opacity: 1, y: 0 }}
                            transition={{ delay: idx * 0.1 }}
                            className="bg-white dark:bg-slate-800 rounded-3xl p-6 shadow-sm border border-slate-200 dark:border-slate-700/50 hover:shadow-xl transition-shadow"
                        >
                            <div className="flex justify-between items-start mb-4">
                                <div className="flex items-center gap-3">
                                    <div className={`w-12 h-12 rounded-2xl flex items-center justify-center font-bold text-lg text-white shadow-inner ${
                                        post.type === 'important' ? 'bg-gradient-to-br from-rose-400 to-red-600' :
                                        post.type === 'academic' ? 'bg-gradient-to-br from-indigo-400 to-blue-600' :
                                        'bg-gradient-to-br from-emerald-400 to-teal-600'
                                    }`}>
                                        {post.avatar}
                                    </div>
                                    <div>
                                        <h4 className="font-bold text-slate-800 dark:text-white">{post.author}</h4>
                                        <div className="flex items-center gap-2 text-xs text-slate-500">
                                            <span>{post.role}</span>
                                            <span>•</span>
                                            <span>{post.time}</span>
                                        </div>
                                    </div>
                                </div>
                                <button className="p-2 text-slate-400 hover:bg-slate-100 dark:hover:bg-slate-700 rounded-lg transition-colors">
                                    <MoreHorizontal className="w-5 h-5" />
                                </button>
                            </div>

                            <div className="mb-4">
                                <div className="flex items-center gap-2 mb-2">
                                    {post.type === 'important' && <Megaphone className="w-4 h-4 text-rose-500" />}
                                    <h3 className="text-xl font-bold text-slate-800 dark:text-white">{post.title}</h3>
                                </div>
                                <p className="text-slate-600 dark:text-slate-300 leading-relaxed">
                                    {post.content}
                                </p>
                            </div>

                            {post.attachments && (
                                <div className="mb-6 flex gap-3">
                                    {post.attachments.map((file, i) => (
                                        <div key={i} className="flex items-center gap-3 p-3 rounded-xl border border-slate-200 dark:border-slate-700 bg-slate-50 dark:bg-slate-900/50 hover:bg-slate-100 dark:hover:bg-slate-800 cursor-pointer transition-colors">
                                            <div className="p-2 bg-indigo-100 dark:bg-indigo-900/30 text-indigo-600 dark:text-indigo-400 rounded-lg">
                                                <FileText className="w-5 h-5" />
                                            </div>
                                            <div>
                                                <p className="text-sm font-semibold text-slate-800 dark:text-white">{file.name}</p>
                                                <p className="text-xs text-slate-500">{file.size}</p>
                                            </div>
                                        </div>
                                    ))}
                                </div>
                            )}

                            <div className="pt-4 border-t border-slate-100 dark:border-slate-700/50 flex items-center gap-6">
                                <button className="flex items-center gap-2 text-slate-500 hover:text-indigo-600 dark:hover:text-indigo-400 transition-colors font-medium text-sm">
                                    <Star className="w-5 h-5" />
                                    <span>{post.likes}</span>
                                </button>
                                <button className="flex items-center gap-2 text-slate-500 hover:text-indigo-600 dark:hover:text-indigo-400 transition-colors font-medium text-sm">
                                    <MessageCircle className="w-5 h-5" />
                                    <span>{post.comments}</span>
                                </button>
                                <button className="flex items-center gap-2 text-slate-500 hover:text-indigo-600 dark:hover:text-indigo-400 transition-colors font-medium text-sm ml-auto">
                                    <Share2 className="w-5 h-5" />
                                    <span>Share</span>
                                </button>
                            </div>
                        </motion.div>
                    ))}
                </div>
            </div>
        </DashboardLayout>
    );
};

export default Feed;
