import React from 'react';
import Layout from '../components/Layout';

interface Notice {
    id: number;
    title: string;
    content: string;
    date: string;
    category: string;
}

const SharedNoticeBoard: React.FC<{ sidebarItems: any[] }> = ({ sidebarItems }) => {
    const notices: Notice[] = [
        { id: 1, title: "Final Examination Schedule", content: "The final exam schedule for the current semester has been released. Please check the academics section for details.", date: "2024-03-22", category: "Academics" },
        { id: 2, title: "Campus-wide Maintenance", content: "The main building will be undergoing routine maintenance this Sunday.", date: "2024-03-21", category: "Facilities" },
        { id: 3, title: "Health Advisory", content: "Reminder to all students and staff regarding hygiene protocols.", date: "2024-03-20", category: "Health" }
    ];

    return (
        <Layout sidebarItems={sidebarItems}>
            <div className="flex flex-col gap-8">
                <div className="flex items-center justify-between">
                    <div>
                        <h1 className="text-4xl font-black text-slate-800 tracking-tight">Digital Notice Board</h1>
                        <p className="text-slate-500 font-medium tracking-tight">Broadcast announcements across the institution</p>
                    </div>
                </div>

                <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
                    {notices.map((notice) => (
                        <div key={notice.id} className="bg-white p-10 rounded-[3.5rem] border border-slate-100 shadow-2xl shadow-indigo-100/10 hover:shadow-indigo-200/20 transition-all group">
                            <div className="flex items-center justify-between mb-8">
                                <span className="px-5 py-2 bg-indigo-50 text-indigo-600 text-[10px] font-black uppercase tracking-widest rounded-full">{notice.category}</span>
                                <span className="text-slate-300 text-xs font-bold">{notice.date}</span>
                            </div>
                            <h3 className="text-2xl font-black text-slate-800 mb-4 tracking-tight group-hover:text-indigo-600 transition-colors uppercase">{notice.title}</h3>
                            <p className="text-slate-500 font-medium leading-relaxed text-sm mb-10">
                                {notice.content}
                            </p>
                            <div className="pt-8 border-t border-slate-50 flex items-center justify-between">
                                <button className="text-indigo-600 font-black text-xs uppercase tracking-widest hover:translate-x-1 transition-transform inline-flex items-center gap-2">
                                    Read Full Announcement
                                    <span className="material-icons text-lg">east</span>
                                </button>
                            </div>
                        </div>
                    ))}
                </div>
            </div>
        </Layout>
    );
};

export default SharedNoticeBoard;
