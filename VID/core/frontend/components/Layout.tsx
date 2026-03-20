import React, { useEffect, useState } from 'react';

interface LayoutProps {
    children: React.ReactNode;
    sidebarItems?: { label: string; icon: string; path: string; id?: string }[];
}

const Layout: React.FC<LayoutProps> = ({ children, sidebarItems = [] }) => {
    const [filteredItems, setFilteredItems] = useState<{ label: string; icon: string; path: string; id?: string }[]>([]);
    
    useEffect(() => {
        const userData = localStorage.getItem('user_data');
        if (!userData) {
            setFilteredItems([]);
            return;
        }
        
        const user = JSON.parse(userData);
        const assignedWorkspaces = user.assignedWorkspaces || [];
        const role = user.role;

        if (role === 'super-admin') {
            setFilteredItems(sidebarItems);
        } else {
            const filtered = sidebarItems.filter(item => {
                const itemPath = item.path.split('/').pop() || '';
                const itemLabel = item.label.toLowerCase();
                return assignedWorkspaces.some((ws: string) => 
                    itemPath.includes(ws.toLowerCase()) || itemLabel.includes(ws.toLowerCase())
                );
            });
            setFilteredItems(filtered);
        }
    }, [sidebarItems]);

    return (
        <div className="flex h-screen bg-slate-50 font-outfit">
            <div className="w-72 bg-white shadow-2xl border-r border-slate-200 flex flex-col z-20 overflow-hidden">
                <div className="p-8 border-b border-slate-100 flex items-center gap-4">
                    <div className="w-12 h-12 bg-gradient-to-br from-indigo-600 to-violet-700 rounded-2xl shadow-xl shadow-indigo-100 flex items-center justify-center">
                        <span className="text-white font-black text-2xl">V</span>
                    </div>
                    <div>
                        <h2 className="text-xl font-black text-slate-900 tracking-tight">VID PLATFORM</h2>
                        <span className="text-[10px] font-bold text-slate-400 tracking-widest uppercase">Management</span>
                    </div>
                </div>
                
                <nav className="flex-1 overflow-y-auto p-6 space-y-2">
                    {filteredItems.map((item, idx) => (
                        <a 
                            key={idx} 
                            href={item.path} 
                            className="flex items-center gap-4 px-4 py-3.5 rounded-xl text-slate-600 hover:bg-slate-50 hover:text-indigo-600 transition-all duration-300 group"
                        >
                            <span className="material-icons opacity-70 group-hover:opacity-100 transition-opacity">{item.icon}</span>
                            <span className="font-semibold text-sm">{item.label}</span>
                        </a>
                    ))}
                    {filteredItems.length === 0 && (
                        <div className="p-10 text-center">
                            <p className="text-[10px] font-black text-slate-300 uppercase tracking-widest leading-relaxed">No access granted</p>
                        </div>
                    )}
                </nav>
                
                <div className="p-8 border-t border-slate-100">
                    <button 
                        onClick={() => { localStorage.clear(); window.location.href='/'; }}
                        className="w-full py-4 rounded-2xl bg-slate-50 text-slate-400 font-bold text-xs uppercase tracking-widest hover:bg-rose-50 hover:text-rose-500 transition-all"
                    >
                        Sign Out
                    </button>
                </div>
            </div>

            <div className="flex-1 flex flex-col overflow-hidden">
                <header className="h-20 bg-white/80 backdrop-blur-md border-b border-slate-200 flex items-center justify-between px-10 shrink-0">
                    <div className="flex items-center bg-slate-100 px-5 py-2.5 rounded-2xl border border-slate-200 min-w-[350px]">
                        <span className="material-icons text-slate-400 text-lg">search</span>
                        <input type="text" placeholder="Search system modules..." className="bg-transparent border-none outline-none px-3 text-sm text-slate-600 w-full font-medium" />
                    </div>
                    <div className="flex items-center gap-4">
                        <div className="w-10 h-10 bg-slate-100 rounded-full flex items-center justify-center text-slate-400">
                            <span className="material-icons text-xl">notifications_none</span>
                        </div>
                        <div className="w-10 h-10 bg-indigo-500 rounded-full flex items-center justify-center text-white font-bold text-xs uppercase tracking-widest">
                            {JSON.parse(localStorage.getItem('user_data') || '{}').username?.substring(0,2) || 'AD'}
                        </div>
                    </div>
                </header>

                <main className="flex-1 overflow-y-auto">
                    <div className="p-10 max-w-[1600px] mx-auto animate-fadeIn">
                        {children}
                    </div>
                </main>
            </div>
        </div>
    );
};

export default Layout;
