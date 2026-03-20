import React from 'react';
import Layout from '../../../../core/frontend/components/Layout';
import Card from '../../../../core/frontend/components/Card';

const StudentPermissions: React.FC = () => {
    const sidebarItems = [
        { "label": "Digital Notice Board", "icon": "announcement", "path": "/payment-administrator/notice-board" },
        { "label": "Dashboard", "icon": "dashboard", "path": "/payment-administrator/dashboard" },
        { "label": "Academic Fees", "icon": "school", "path": "/payment-administrator/academic-fees" },
        { "label": "Student Permissions", "icon": "verified_user", "path": "/payment-administrator/student-permissions" },
        { "label": "Exam Fee Restrictions", "icon": "gavel", "path": "/payment-administrator/exam-fee-restrictions" },
        { "label": "Examination Fees", "icon": "grading", "path": "/payment-administrator/examination-fees" },
        { "label": "Open Payments", "icon": "account_balance", "path": "/payment-administrator/open-payments" },
        { "label": "Configuration", "icon": "settings", "path": "/payment-administrator/configuration" },
        { "label": "Reports", "icon": "analytics", "path": "/payment-administrator/reports" },
        { "label": "Concessions", "icon": "discount", "path": "/payment-administrator/concessions" },
        { "label": "Online Transactions", "icon": "payment", "path": "/payment-administrator/online-transactions" },
        { "label": "Challans", "icon": "receipt", "path": "/payment-administrator/challans" },
        { "label": "Statements", "icon": "description", "path": "/payment-administrator/statements" },
        { "label": "Scholarships", "icon": "military_tech", "path": "/payment-administrator/scholarships" },
        { "label": "Credit Memos", "icon": "credit_card", "path": "/payment-administrator/credit-memos" },
        { "label": "Student Fee Card", "icon": "account_box", "path": "/payment-administrator/student-fee-card" },
        { "label": "Transaction Card", "icon": "credit_score", "path": "/payment-administrator/transaction-card" }
    ];

    return (
        <Layout sidebarItems={sidebarItems}>
            <div className="flex flex-col gap-10">
                <div className="flex items-center justify-between">
                    <div>
                        <h1 className="text-4xl font-black text-slate-800 tracking-tight capitalize">Student Permissions</h1>
                        <p className="text-slate-500 font-medium tracking-tight">Manage and oversee operational activities</p>
                    </div>
                </div>

                <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-8">
                    <Card title="Total Records" value="1,240" icon="groups" color="indigo" />
                    <Card title="Active Status" value="94.2%" icon="check_circle" color="green" />
                    <Card title="Pending Review" value="34" icon="pending" color="yellow" />
                    <Card title="System Alerts" value="2" icon="error_outline" color="red" />
                </div>

                <div className="bg-white p-12 rounded-[3.5rem] shadow-2xl shadow-indigo-100/20 border border-slate-100">
                    <h3 className="text-sm font-black text-slate-400 uppercase tracking-widest mb-8 px-2 flex items-center gap-3">
                        <span className="w-8 h-[1px] bg-slate-200"></span>
                        Student Permissions Data Interface
                    </h3>
                    <div className="flex items-center justify-center p-20 bg-slate-50 border-2 border-dashed border-slate-200 rounded-[2.5rem]">
                        <p className="text-slate-400 font-bold uppercase tracking-widest text-xs">Module Implementation Area</p>
                    </div>
                </div>
            </div>
        </Layout>
    );
};

export default StudentPermissions;
