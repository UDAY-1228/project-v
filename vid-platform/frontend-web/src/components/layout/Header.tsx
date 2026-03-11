import React from 'react';

interface HeaderProps {
    role: string;
}

const Header: React.FC<HeaderProps> = ({ role }) => {
    return (
        <header className="bg-white dark:bg-gray-800 border-b border-gray-200 dark:border-gray-700 h-16 flex items-center justify-between px-8 sticky top-0 z-20 transition-colors duration-300 shadow-sm">
            <div className="flex items-center space-x-4">
                <button className="md:hidden text-gray-600 dark:text-gray-300 focus:outline-none">
                    <svg className="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                        <path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M4 6h16M4 12h16M4 18h16" />
                    </svg>
                </button>
                <div className="text-xl font-semibold text-gray-800 dark:text-white">
                    Dashboard
                </div>
            </div>

            <div className="flex items-center space-x-6">
                <div className="hidden md:flex items-center bg-gray-100 dark:bg-gray-700 rounded-full px-4 py-1.5 border border-gray-200 dark:border-gray-600">
                    <span className="text-sm font-medium text-gray-600 dark:text-gray-300">Role:</span>
                    <span className="ml-2 text-sm font-bold text-indigo-600 dark:text-indigo-400">{role}</span>
                </div>

                {/* Notifications */}
                <button className="p-2 text-gray-400 hover:text-indigo-600 dark:hover:text-indigo-400 transition-colors">
                    <svg className="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                        <path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M15 17h5l-1.405-1.405A2.032 2.032 0 0118 14.158V11a6.002 6.002 0 00-4-5.659V5a2 2 0 10-4 0v.341C7.67 6.165 6 8.388 6 11v3.159c0 .538-.214 1.055-.595 1.436L4 17h5m6 0v1a3 3 0 11-6 0v-1m6 0H9" />
                    </svg>
                </button>

                {/* User Profile */}
                <div className="flex items-center space-x-3 border-l pl-6 border-gray-200 dark:border-gray-700">
                    <div className="text-right hidden sm:block">
                        <p className="text-sm font-bold text-gray-800 dark:text-white">John Doe</p>
                        <p className="text-xs text-gray-500 dark:text-gray-400">ID: VID-2024-001</p>
                    </div>
                    <div className="h-10 w-10 rounded-full bg-gradient-to-tr from-indigo-600 to-purple-600 flex items-center justify-center text-white font-bold text-lg shadow-lg border-2 border-white dark:border-gray-800">
                        JD
                    </div>
                </div>
            </div>
        </header>
    );
};

export default Header;
