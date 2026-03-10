import React from 'react';

interface SidebarProps {
    isOpen: boolean;
    setOpen: (open: boolean) => void;
    role: string;
}

const Sidebar: React.FC<SidebarProps> = ({ isOpen, role }) => {
    const menuItems = {
        SuperAdmin: ['Institutions', 'Licenses', 'Global Analytics', 'Settings'],
        Admin: ['Users', 'Attendance Policy', 'Timetable', 'Finance'],
        Teacher: ['My Classes', 'Attendance Marking', 'Grading', 'LMS'],
        Student: ['Dashboard', 'My Courses', 'Fees', 'Virtual ID'],
    };

    const currentItems = menuItems[role as keyof typeof menuItems] || [];

    return (
        <aside className={`bg-indigo-700 text-white w-64 min-h-screen transition-transform transform ${isOpen ? 'translate-x-0' : '-translate-x-full'} md:translate-x-0 md:static fixed z-30`}>
            <div className="p-6">
                <h1 className="text-2xl font-bold">VID PLATFORM</h1>
                <p className="text-xs text-indigo-200 mt-1 uppercase tracking-widest">{role} Portal</p>
            </div>

            <nav className="mt-6 px-4">
                {currentItems.map((item) => (
                    <a
                        key={item}
                        href={`/${item.toLowerCase().replace(' ', '-')}`}
                        className="block py-2.5 px-4 rounded transition duration-200 hover:bg-indigo-900 hover:text-white mb-2"
                    >
                        {item}
                    </a>
                ))}
            </nav>
        </aside>
    );
};

export default Sidebar;
