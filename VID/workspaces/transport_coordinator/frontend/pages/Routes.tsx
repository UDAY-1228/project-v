import React from 'react';
import Layout from '../../../../core/frontend/components/Layout';
import Card from '../../../../core/frontend/components/Card';

const RoutesPage: React.FC = () => {
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

    const routes = [
        { id: "R-101", name: "North Route", stops: 12, distance: "15.4 km", time: "45 mins" },
        { id: "R-102", name: "East Route", stops: 8, distance: "10.2 km", time: "30 mins" },
        { id: "R-103", name: "West Route", stops: 15, distance: "18.1 km", time: "55 mins" }
    ];

    return (
        <Layout sidebarItems={sidebarItems}>
            <div className="flex flex-col gap-10">
                <div className="flex items-center justify-between">
                    <div>
                        <h1 className="text-4xl font-black text-slate-800 tracking-tight">Routes</h1>
                        <p className="text-slate-500 font-medium tracking-tight">Design and optimize school bus routes</p>
                    </div>
                    <button className="px-6 py-3 bg-indigo-600 text-white rounded-2xl font-bold hover:bg-indigo-700 transition-all flex items-center gap-2">
                        <span className="material-icons text-xl">map</span>
                        Create Route
                    </button>
                </div>

                <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
                    {routes.map((route) => (
                        <div key={route.id} className="bg-white p-10 rounded-[3.5rem] border border-slate-100 shadow-xl shadow-indigo-100/10 hover:shadow-2xl transition-all duration-300 group">
                            <div className="flex items-center gap-6 mb-8 underline underline-offset-8 decoration-indigo-400">
                                <span className="text-2xl font-black text-indigo-500 tracking-tighter">{route.id}</span>
                                <h3 className="text-2xl font-extrabold tracking-tight group-hover:text-indigo-600 transition-colors">{route.name}</h3>
                            </div>
                            
                            <div className="space-y-6">
                                <div className="flex items-center justify-between">
                                    <span className="text-xs font-black uppercase tracking-widest text-slate-400 group-hover:text-indigo-400">Total Stops</span>
                                    <span className="font-bold text-slate-700">{route.stops}</span>
                                </div>
                                <div className="flex items-center justify-between border-y border-slate-50 py-4">
                                    <span className="text-xs font-black uppercase tracking-widest text-slate-400 group-hover:text-indigo-400">Distance</span>
                                    <span className="font-bold text-slate-700">{route.distance}</span>
                                </div>
                                <div className="flex items-center justify-between">
                                    <span className="text-xs font-black uppercase tracking-widest text-slate-400 group-hover:text-indigo-400">Average Time</span>
                                    <span className="font-bold text-slate-700">{route.time}</span>
                                </div>
                            </div>
                            
                            <div className="mt-10 pt-6 flex items-center justify-between border-t border-slate-50">
                                <button className="text-indigo-600 font-bold text-sm tracking-tight flex items-center gap-2">
                                    <span className="material-icons text-lg">edit</span>
                                    Edit Route
                                </button>
                                <button className="px-4 py-2 bg-slate-50 rounded-xl text-slate-400 hover:bg-slate-100 transition-all flex items-center gap-2">
                                    <span className="material-icons text-lg">visibility</span>
                                    View Map
                                </button>
                            </div>
                        </div>
                    ))}
                </div>
            </div>
        </Layout>
    );
};

export default RoutesPage;
