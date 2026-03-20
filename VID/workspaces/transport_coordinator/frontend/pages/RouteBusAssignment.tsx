import React from 'react';
import Layout from '../../../../core/frontend/components/Layout';
import Card from '../../../../core/frontend/components/Card';

const RouteBusAssignment: React.FC = () => {
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

    const assignments = [
        { id: 1, routeId: "R-101", routeName: "North Route", busId: "B-201", driver: "John Doe", morningShift: "07:30 AM", eveningShift: "03:30 PM" },
        { id: 2, routeId: "R-102", routeName: "East Route", busId: "B-205", driver: "Jane Smith", morningShift: "07:45 AM", eveningShift: "03:45 PM" },
        { id: 3, routeId: "R-103", routeName: "West Route", busId: "B-203", driver: "Bob Brown", morningShift: "07:15 AM", eveningShift: "03:15 PM" }
    ];

    return (
        <Layout sidebarItems={sidebarItems}>
            <div className="flex flex-col gap-10">
                <div className="flex items-center justify-between">
                    <div>
                        <h1 className="text-4xl font-black text-slate-800 tracking-tight">Route Bus Assignment</h1>
                        <p className="text-slate-500 font-medium tracking-tight">Associate buses to routes and schedule shifts</p>
                    </div>
                    <button className="px-6 py-3 bg-indigo-600 text-white rounded-2xl font-bold hover:bg-indigo-700 transition-all flex items-center gap-2">
                        <span className="material-icons text-xl">assignment</span>
                        New Assignment
                    </button>
                </div>

                <div className="bg-white p-12 rounded-[3.5rem] shadow-2xl shadow-indigo-100/20 border border-slate-100">
                    <h3 className="text-sm font-black text-slate-400 uppercase tracking-widest mb-10 px-2 flex items-center gap-3">
                        <span className="w-8 h-[1px] bg-slate-200"></span>
                        Route & Bus Pairing
                    </h3>
                    <div className="flex flex-col gap-6">
                        {assignments.map((asgn) => (
                            <div key={asgn.id} className="p-8 bg-slate-50/50 rounded-3xl border border-slate-100 hover:border-indigo-400 hover:bg-white hover:shadow-xl transition-all duration-300 group flex items-center justify-between">
                                <div className="flex items-center gap-8">
                                    <div className="flex items-center -space-x-4">
                                        <div className="w-14 h-14 bg-white rounded-2xl shadow-md flex items-center justify-center text-indigo-500 group-hover:bg-indigo-500 group-hover:text-white transition-all">
                                            <span className="material-icons text-2xl">map</span>
                                        </div>
                                        <div className="w-14 h-14 bg-indigo-50 rounded-2xl shadow-md flex items-center justify-center text-indigo-600 group-hover:bg-indigo-600 group-hover:text-white transition-all">
                                            <span className="material-icons text-2xl">directions_bus</span>
                                        </div>
                                    </div>
                                    <div>
                                        <h4 className="text-lg font-black text-slate-800">{asgn.routeName}</h4>
                                        <p className="text-xs font-bold text-slate-400 uppercase tracking-widest mt-1">Bus {asgn.busId} • {asgn.driver}</p>
                                    </div>
                                </div>
                                <div className="flex items-center gap-12">
                                    <div className="text-center">
                                        <p className="text-[10px] font-black text-slate-300 uppercase tracking-widest mb-1">Morning Shift</p>
                                        <p className="font-bold text-slate-600">{asgn.morningShift}</p>
                                    </div>
                                    <div className="text-center">
                                        <p className="text-[10px] font-black text-slate-300 uppercase tracking-widest mb-1">Evening Shift</p>
                                        <p className="font-bold text-slate-600">{asgn.eveningShift}</p>
                                    </div>
                                    <button className="p-3 text-slate-300 hover:text-indigo-600">
                                        <span className="material-icons">edit</span>
                                    </button>
                                </div>
                            </div>
                        ))}
                    </div>
                </div>
            </div>
        </Layout>
    );
};

export default RouteBusAssignment;
