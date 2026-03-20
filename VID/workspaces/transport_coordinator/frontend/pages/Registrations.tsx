import React from 'react';
import Layout from '../../../../core/frontend/components/Layout';
import Card from '../../../../core/frontend/components/Card';

const Registrations: React.FC = () => {
    const sidebarItems = [
        { label: "Digital Notice Board", icon: "announcement", path: "/transport-coordinator/notice-board" },
        { label: "Transport Analytics", icon: "bar_chart", path: "/transport-coordinator/analytics" },
        { label: "Transport Registrations", icon: "app_registration", path: "/transport-coordinator/registrations" },
        { label: "Buses", icon: "directions_bus", path: "/transport-coordinator/buses" },
        { label: "Boarding Points", icon: "place", path: "/transport-coordinator/boarding" },
        { label: "Routes", icon: "map", path: "/transport-coordinator/routes" },
        { label: "Route Bus Assignment", icon: "assignment", path: "/transport-coordinator/assignment" },
        { label: "Configuration", icon: "settings", path: "/transport-coordinator/config" },
        { label: "Transport Route", icon: "alt_route", path: "/transport-coordinator/transport-route" }
    ];

    const records = [
        { id: 1, studentId: "S-1042", name: "Alice Johnson", route: "North Route", boardingPoint: "Point A", status: "Approved" },
        { id: 2, studentId: "S-1123", name: "Bob Williams", route: "East Route", boardingPoint: "Point B", status: "Pending" },
        { id: 3, studentId: "S-1205", name: "Carol Davis", route: "South Route", boardingPoint: "Point C", status: "Approved" }
    ];

    return (
        <Layout sidebarItems={sidebarItems}>
            <div className="flex flex-col gap-10">
                <div className="flex items-center justify-between">
                    <div>
                        <h1 className="text-4xl font-black text-slate-800 tracking-tight">Transport Registrations</h1>
                        <p className="text-slate-500 font-medium tracking-tight">Manage student bus registrations and applications</p>
                    </div>
                    <button className="px-6 py-3 bg-indigo-600 text-white rounded-2xl font-bold hover:bg-indigo-700 transition-all flex items-center gap-2">
                        <span className="material-icons text-xl">add</span>
                        New Registration
                    </button>
                </div>

                <div className="bg-white p-12 rounded-[3.5rem] shadow-2xl shadow-indigo-100/20 border border-slate-100 overflow-hidden">
                    <h3 className="text-sm font-black text-slate-400 uppercase tracking-widest mb-10 px-2 flex items-center gap-3">
                        <span className="w-8 h-[1px] bg-slate-200"></span>
                        Recent Registrations
                    </h3>
                    <div className="overflow-x-auto">
                        <table className="w-full">
                            <thead>
                                <tr className="border-b border-slate-50">
                                    <th className="px-6 py-4 text-left text-xs font-black uppercase text-slate-400 tracking-widest">Student ID</th>
                                    <th className="px-6 py-4 text-left text-xs font-black uppercase text-slate-400 tracking-widest">Name</th>
                                    <th className="px-6 py-4 text-left text-xs font-black uppercase text-slate-400 tracking-widest">Route</th>
                                    <th className="px-6 py-4 text-left text-xs font-black uppercase text-slate-400 tracking-widest">Boarding Point</th>
                                    <th className="px-6 py-4 text-left text-xs font-black uppercase text-slate-400 tracking-widest">Status</th>
                                </tr>
                            </thead>
                            <tbody>
                                {records.map((record) => (
                                    <tr key={record.id} className="hover:bg-slate-50 transition-colors">
                                        <td className="px-6 py-4 font-bold text-slate-600">{record.studentId}</td>
                                        <td className="px-6 py-4 font-bold text-slate-800">{record.name}</td>
                                        <td className="px-6 py-4 font-medium text-slate-500">{record.route}</td>
                                        <td className="px-6 py-4 font-medium text-slate-500">{record.boardingPoint}</td>
                                        <td className="px-6 py-4">
                                            <span className={`px-4 py-1.5 rounded-full text-[10px] font-black tracking-widest uppercase ${record.status === 'Approved' ? 'bg-green-100 text-green-600' : 'bg-amber-100 text-amber-600'}`}>
                                                {record.status}
                                            </span>
                                        </td>
                                    </tr>
                                ))}
                            </tbody>
                        </table>
                    </div>
                </div>
            </div>
        </Layout>
    );
};

export default Registrations;
