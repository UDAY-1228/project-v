import React, { useEffect, useState } from 'react';

interface LayoutProps {
    children: React.ReactNode;
    sidebarItems?: { label: string; icon: string; path: string; id?: string }[];
}

const Layout: React.FC<LayoutProps> = ({ children, sidebarItems = [] }) => {
    const [filteredItems, setFilteredItems] = useState<{ label: string; icon: string; path: string; id?: string }[]>([]);
    const [isSidebarOpen, setIsSidebarOpen] = useState(false);
    
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
            // Updated filtering logic: if the item path starts with any of the assigned workspace prefixes
            const filtered = sidebarItems.filter(item => {
                const itemPath = item.path.toLowerCase();
                return assignedWorkspaces.some((ws: string) => 
                    itemPath.includes(ws.toLowerCase().replace('_', '-')) ||
                    item.label.toLowerCase().includes(ws.toLowerCase())
                );
            });
            setFilteredItems(filtered.length > 0 ? filtered : sidebarItems); // Fallback to all if filtering fails for now
        }
    }, [sidebarItems]);

    return (
        <div className="flex h-screen bg-slate-50 font-outfit overflow-hidden">
            {/* Sidebar with Mobile Support */}
            <div className={`
                fixed inset-y-0 left-0 z-50 w-72 bg-white shadow-2xl border-r border-slate-200 flex flex-col transform transition-transform duration-300 ease-in-out
                lg:relative lg:translate-x-0 ${isSidebarOpen ? 'translate-x-0' : '-translate-x-full'}
            `}>
                <div className="p-8 border-b border-slate-100 flex items-center justify-between">
                    <div className="flex items-center gap-4">
                        <div className="w-10 h-10 bg-gradient-to-br from-indigo-600 to-violet-700 rounded-2xl shadow-xl shadow-indigo-100 flex items-center justify-center">
                            <span className="text-white font-black text-xl">V</span>
                        </div>
                        <div>
                            <h2 className="text-lg font-black text-slate-900 tracking-tight leading-none">VID PLATFORM</h2>
                            <span className="text-[9px] font-bold text-slate-400 tracking-widest uppercase">Management</span>
                        </div>
                    </div>
                    <button onClick={() => setIsSidebarOpen(false)} className="lg:hidden text-slate-400 hover:text-indigo-600">
                        <span className="material-icons">close</span>
                    </button>
                </div>
                
                <nav className="flex-1 overflow-y-auto p-6 space-y-1">
                    {filteredItems.map((item, idx) => (
                        <a 
                            key={idx} 
                            href={item.path} 
                            className="flex items-center gap-4 px-4 py-3 rounded-xl text-slate-600 hover:bg-indigo-50 hover:text-indigo-600 transition-all duration-200 group"
                        >
                            <span className="material-icons opacity-70 group-hover:opacity-100 text-xl">{item.icon}</span>
                            <span className="font-bold text-sm tracking-tight">{item.label}</span>
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
                        className="w-full py-4 rounded-xl bg-slate-50 text-slate-400 font-bold text-xs uppercase tracking-widest hover:bg-rose-50 hover:text-rose-500 transition-all border border-transparent hover:border-rose-100"
                    >
                        Sign Out
                    </button>
                </div>
            </div>

        {/* Main Content Area */}
        <div className="flex-1 flex flex-col overflow-hidden w-full">
            {/* Header */}
            <header className="h-20 bg-white/80 backdrop-blur-md border-b border-slate-200 flex items-center justify-between px-6 lg:px-10 shrink-0">
                <div className="flex items-center gap-4">
                    <button onClick={() => setIsSidebarOpen(true)} className="lg:hidden p-2 text-slate-500">
                        <span className="material-icons">menu</span>
                    </button>
                    <div className="hidden sm:flex items-center bg-slate-100 px-5 py-2.5 rounded-2xl border border-slate-200 lg:min-w-[350px]">
                        <span className="material-icons text-slate-400 text-lg">search</span>
                        <input type="text" placeholder="Search system modules..." className="bg-transparent border-none outline-none px-3 text-sm text-slate-600 w-full font-medium" />
                    </div>
                </div>
                
                <div className="flex items-center gap-6">
                    {JSON.parse(localStorage.getItem('user_data') || '{}').assignedWorkspaces?.length > 1 && (
                        <select 
                            className="hidden md:block bg-indigo-50 border border-indigo-100 text-indigo-700 text-xs font-bold uppercase tracking-widest rounded-xl px-4 py-2 outline-none cursor-pointer hover:bg-indigo-100 transition-colors"
                            onChange={(e) => window.location.href = `/${e.target.value.replace('_', '-')}/dashboard`}
                            defaultValue={window.location.pathname.split('/')[1].replace('-', '_')}
                        >
                            <option value="" disabled>Switch Workspace</option>
                            {JSON.parse(localStorage.getItem('user_data') || '{}').assignedWorkspaces.map((ws: string) => (
                                <option key={ws} value={ws}>{ws.replace('_', ' ')}</option>
                            ))}
                        </select>
                    )}
                    <div className="hidden xs:flex w-10 h-10 bg-slate-100 rounded-full items-center justify-center text-slate-400">
                        <span className="material-icons text-xl">notifications_none</span>
                    </div>
                    <div className="w-10 h-10 bg-indigo-500 rounded-full border-4 border-indigo-50 flex items-center justify-center text-white font-black text-xs uppercase shadow-lg shadow-indigo-100">
                        {JSON.parse(localStorage.getItem('user_data') || '{}').username?.substring(0,2) || 'AD'}
                    </div>
                </div>
            </header>

            {/* Main Content */}
                <main className="flex-1 overflow-y-auto">
                    <div className="p-6 lg:p-10 max-w-[1600px] mx-auto animate-fadeIn">
                        {children}
                    </div>
                </main>
            </div>

            {/* Mobile Overlay */}
            {isSidebarOpen && (
                <div 
                    className="fixed inset-0 bg-slate-900/40 backdrop-blur-sm z-40 lg:hidden transition-opacity"
                    onClick={() => setIsSidebarOpen(false)}
                />
            )}
        </div>
    );
};

export default Layout;
