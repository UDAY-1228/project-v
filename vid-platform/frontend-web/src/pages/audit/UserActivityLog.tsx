import React from 'react';
import DashboardLayout from '../../components/layout/DashboardLayout';

const UserActivityLog: React.FC = () => {
    return (
        <DashboardLayout role="Admin">
            <div className="p-6">
                <h1 className="text-3xl font-bold text-gray-800 dark:text-white mb-6">UserActivityLog</h1>
                <div className="bg-white dark:bg-gray-800 rounded-2xl shadow-xl p-8 border border-gray-100 dark:border-gray-700">
                    <p className="text-gray-600 dark:text-gray-400">
                        This is the UserActivityLog page. Implementation in progress...
                    </p>
                    <div className="mt-8 grid grid-cols-1 md:grid-cols-3 gap-6">
                        <div className="h-32 bg-blue-50 dark:bg-blue-900/20 rounded-xl animate-pulse"></div>
                        <div className="h-32 bg-purple-50 dark:bg-purple-900/20 rounded-xl animate-pulse shadow-inner"></div>
                        <div className="h-32 bg-indigo-50 dark:bg-indigo-900/20 rounded-xl animate-pulse"></div>
                    </div>
                </div>
            </div>
        </DashboardLayout>
    );
};

export default UserActivityLog;
