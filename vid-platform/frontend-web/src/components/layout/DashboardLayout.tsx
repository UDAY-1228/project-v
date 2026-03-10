import React, { useState } from 'react';
import Sidebar from './Sidebar';
import Header from './Header';

interface LayoutProps {
    children: React.ReactNode;
    role: 'Student' | 'Teacher' | 'Admin' | 'SuperAdmin';
}

const DashboardLayout: React.FC<LayoutProps> = ({ children, role }) => {
    const [isSidebarOpen, setSidebarOpen] = useState(true);

    return (
        <div className="flex h-screen bg-gray-100 dark:bg-gray-900 transition-colors duration-300">
            {/* Sidebar Navigation */}
            <Sidebar isOpen={isSidebarOpen} setOpen={setSidebarOpen} role={role} />

            <div className="flex-1 flex flex-col overflow-hidden">
                {/* Top Header */}
                <Header role={role} />

                {/* Main Content Area */}
                <main className="flex-1 overflow-x-hidden overflow-y-auto p-4 md:p-8">
                    <div className="container mx-auto">
                        {children}
                    </div>
                </main>
            </div>
        </div>
    );
};

export default DashboardLayout;
