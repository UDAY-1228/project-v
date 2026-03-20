import React from 'react';

interface LayoutProps {
    children: React.ReactNode;
    sidebarItems?: { label: string; icon: string; path: string }[];
}

const Layout: React.FC<LayoutProps> = ({ children, sidebarItems = [] }) => {
    return (
        <div className="flex h-screen bg-slate-50 font-outfit">
            {/* Sidebar */}
            <div className="w-72 bg-white shadow-2xl border-r border-slate-200 flex flex-col z-20 overflow-hidden">
                <div className="p-8 border-b border-slate-100 flex items-center gap-3">
                    <div className="w-10 h-10 bg-gradient-to-br from-indigo-500 to-violet-600 rounded-xl shadow-lg shadow-indigo-100 flex items-center justify-center">
                        <span className="text-white font-black text-xl">V</span>
                    </div>
                    <div>
                        <h2 className="text-xl font-black text-slate-800 tracking-tight">VID</h2>
                        <span className="text-[10px] font-bold text-slate-400 tracking-widest uppercase">Management</span>
                    </div>
                </div>
                
                <nav className="flex-1 overflow-y-auto p-6 space-y-2">
                    {sidebarItems.map((item, idx) => (
                        <a 
                            key={idx} 
                            href={item.path} 
                            className="flex items-center gap-4 px-4 py-3.5 rounded-xl text-slate-600 hover:bg-slate-50 hover:text-indigo-600 transition-all duration-300 group"
                        >
                            <span className="material-icons opacity-70 group-hover:opacity-100 transition-opacity">{item.icon}</span>
                            <span className="font-semibold">{item.label}</span>
                        </a>
                    ))}
                </nav>
            </div>

            {/* Main Content Area */}
            <div className="flex-1 flex flex-col overflow-hidden">
                {/* Header */}
                <header className="h-20 bg-white/80 backdrop-blur-md border-b border-slate-200 flex items-center justify-between px-10 sticky top-0 z-10">
                    <div className="flex items-center bg-slate-100 px-4 py-2 rounded-xl border border-slate-200 min-w-[300px]">
                        <span className="material-icons text-slate-400 text-sm">search</span>
                        <input type="text" placeholder="Quick search..." className="bg-transparent border-none outline-none px-3 text-sm text-slate-600 w-full" />
                    </div>
                    <div className="flex items-center gap-6">
                        <button className="relative p-2.5 rounded-xl bg-slate-50 hover:bg-slate-100 transition-all">
                            <span className="material-icons text-slate-500">notifications_none</span>
                            <span className="absolute top-2 right-2 w-2.5 h-2.5 bg-rose-500 rounded-full border-2 border-white"></span>
                        </button>
                        <div className="flex items-center gap-4 pl-6 border-l border-slate-200">
                            <div className="text-right">
                                <p className="text-sm font-bold text-slate-700">John Doe</p>
                                <p className="text-[11px] font-medium text-slate-400 uppercase tracking-wider">Super Admin</p>
                            </div>
                            <div className="w-11 h-11 bg-indigo-100 rounded-xl overflow-hidden shadow-inner">
                                <img src="https://ui-avatars.com/api/?name=John+Doe&background=random" alt="Avatar" />
                            </div>
                        </div>
                    </div>
                </header>

                {/* Page Content */}
                <main className="flex-1 overflow-y-auto scroll-smooth custom-scrollbar">
                    <div className="p-10 max-w-[1600px] mx-auto animate-fadeIn">
                        {children}
                    </div>
                </main>
            </div>
        </div>
    );
};

export default Layout;
