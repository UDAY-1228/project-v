import React from 'react';
import { NavLink } from 'react-router-dom';

interface SidebarProps {
    isOpen: boolean;
    setOpen: (open: boolean) => void;
    role: string;
}

const Sidebar: React.FC<SidebarProps> = ({ isOpen, setOpen, role }) => {
    const navItems = [
        {
            name: 'Tools Hub', path: '/tools/toolshome', icon: (
                <svg className="w-5 h-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                    <path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M4 6a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2H6a2 2 0 01-2-2V6zM14 6a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2h-2a2 2 0 01-2-2V6zM4 16a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2H6a2 2 0 01-2-2v-2zM14 16a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2h-2a2 2 0 01-2-2v-2z" />
                </svg>
            )
        },
        {
            name: 'Analytics', path: '/analytics/studentanalytics', icon: (
                <svg className="w-5 h-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                    <path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M9 19v-6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2a2 2 0 002-2zm0 0V9a2 2 0 012-2h2a2 2 0 012 2v10m-6 0a2 2 0 002 2h2a2 2 0 002-2m0 0V5a2 2 0 012-2h2a2 2 0 012 2v14a2 2 0 002 2h2a2 2 0 002-2" />
                </svg>
            )
        },
        {
            name: 'LMS', path: '/lms/mycourses', icon: (
                <svg className="w-5 h-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                    <path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M12 6.253v13m0-13C10.832 5.477 9.246 5 7.5 5S4.168 5.477 3 6.253v13C4.168 18.477 5.754 18 7.5 18s3.332.477 4.5 1.253m0-13C13.168 5.477 14.754 5 16.5 5c1.747 0 3.332.477 4.5 1.253v13C19.832 18.477 18.247 18 16.5 18c-1.746 0-3.332.477-4.5 1.253" />
                </svg>
            )
        },
        {
            name: 'Virtual ID', path: '/profiles/virtualid', icon: (
                <svg className="w-5 h-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                    <path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M10 6H5a2 2 0 00-2 2v9a2 2 0 002 2h14a2 2 0 002-2V8a2 2 0 00-2-2h-5m-4 0V5a2 2 0 114 0v1m-4 0a2 2 0 014 0m-5 8a2 2 0 100-4 2 2 0 000 4zm0 0c1.306 0 2.417.835 2.83 2M9 14a3.001 3.001 0 00-2.83 2M15 11h3m-3 4h2" />
                </svg>
            )
        },
        {
            name: 'Messages', path: '/messaging/messagesinbox', icon: (
                <svg className="w-5 h-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                    <path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M8 10h.01M12 10h.01M16 10h.01M9 16H5a2 2 0 01-2-2V6a2 2 0 012-2h14a2 2 0 012 2v8a2 2 0 01-2 2h-5l-5 5v-5z" />
                </svg>
            )
        },
    ];

    return (
        <aside className={`fixed inset-y-0 left-0 z-50 w-72 bg-gradient-to-b from-indigo-950 to-indigo-900 text-white transition-all duration-300 transform ${isOpen ? 'translate-x-0' : '-translate-x-full'} lg:translate-x-0 lg:static lg:inset-0 shadow-2xl`}>
            <div className="flex flex-col h-full">
                {/* Logo Area */}
                <div className="p-8 flex items-center space-x-4">
                    <div className="w-10 h-10 bg-indigo-500 rounded-xl flex items-center justify-center shadow-lg transform rotate-3">
                        <span className="text-2xl font-black text-white italic">V</span>
                    </div>
                    <div>
                        <h1 className="text-xl font-black tracking-tighter uppercase leading-none">VID Platform</h1>
                        <p className="text-[10px] text-indigo-300 font-bold uppercase tracking-[0.2em] mt-1">Education Hub</p>
                    </div>
                </div>

                {/* User Info (Mini) */}
                <div className="px-6 mb-8">
                    <div className="bg-indigo-800/40 rounded-2xl p-4 border border-indigo-700/50">
                        <div className="flex items-center space-x-3">
                            <div className="w-8 h-8 rounded-full bg-indigo-400 flex items-center justify-center font-bold text-xs">JD</div>
                            <div>
                                <p className="text-sm font-bold truncate">John Doe</p>
                                <p className="text-[10px] text-indigo-300">{role}</p>
                            </div>
                        </div>
                    </div>
                </div>

                {/* Navigation */}
                <nav className="flex-1 px-4 space-y-2 overflow-y-auto custom-scrollbar">
                    <p className="px-4 text-[10px] font-bold text-indigo-400 uppercase tracking-widest mb-4">Main Menu</p>
                    {navItems.map((item) => (
                        <NavLink
                            key={item.name}
                            to={item.path}
                            className={({ isActive }) => `
                                flex items-center space-x-4 px-4 py-3 rounded-xl transition-all duration-200 group
                                ${isActive
                                    ? 'bg-indigo-500 text-white shadow-lg shadow-indigo-500/30 font-bold'
                                    : 'text-indigo-200 hover:bg-white/5 hover:text-white'}
                            `}
                        >
                            <span className="opacity-80 group-hover:scale-110 transition-transform">
                                {item.icon}
                            </span>
                            <span className="text-sm tracking-wide">{item.name}</span>
                        </NavLink>
                    ))}
                </nav>

                {/* Footer */}
                <div className="p-6 border-t border-indigo-800/50">
                    <button className="flex items-center space-x-4 w-full px-4 py-3 rounded-xl text-indigo-300 hover:bg-red-500/10 hover:text-red-400 transition-colors">
                        <svg className="w-5 h-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                            <path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M17 16l4-4m0 0l-4-4m4 4H7m6 4v1a3 3 0 01-3 3H6a3 3 0 01-3-3V7a3 3 0 013-3h4a3 3 0 013 3v1" />
                        </svg>
                        <span className="text-sm font-bold">Sign Out</span>
                    </button>
                </div>
            </div>

            {/* Mobile Close Button */}
            <button
                onClick={() => setOpen(false)}
                className="lg:hidden absolute top-4 right-[-50px] bg-indigo-900 text-white p-3 rounded-xl shadow-xl border border-indigo-700"
            >
                <svg className="w-6 h-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                    <path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M6 18L18 6M6 6l12 12" />
                </svg>
            </button>
        </aside>
    );
};

export default Sidebar;
