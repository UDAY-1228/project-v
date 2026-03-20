import React from 'react';
import Layout from '../../../../core/frontend/components/Layout';
import Card from '../../../../core/frontend/components/Card';

const BoardingPoints: React.FC = () => {
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

    const points = [
        { id: 1, name: "City Center Mall", coordinates: "12.9716, 77.5946", area: "Central", students: 45 },
        { id: 2, name: "Library Square", coordinates: "12.9720, 77.5950", area: "West", students: 30 },
        { id: 3, name: "Sunset Park", coordinates: "12.9800, 77.6000", area: "North", students: 55 }
    ];

    return (
        <Layout sidebarItems={sidebarItems}>
            <div className="flex flex-col gap-10">
                <div className="flex items-center justify-between">
                    <div>
                        <h1 className="text-4xl font-black text-slate-800 tracking-tight">Boarding Points</h1>
                        <p className="text-slate-500 font-medium tracking-tight">Define and manage bus stops and collection points</p>
                    </div>
                </div>

                <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
                    {points.map((point) => (
                        <div key={point.id} className="bg-white p-10 rounded-[3.5rem] border border-slate-100 shadow-xl shadow-slate-100/50 hover:bg-indigo-600 hover:text-white transition-all duration-300 group">
                            <div className="flex items-center gap-6 mb-8 underline underline-offset-8 decoration-slate-200 group-hover:decoration-indigo-400">
                                <div className="w-12 h-12 bg-indigo-50 text-indigo-500 rounded-2xl flex items-center justify-center group-hover:bg-white/20 group-hover:text-white">
                                    <span className="material-icons text-xl font-black">place</span>
                                </div>
                                <h3 className="text-xl font-extrabold tracking-tight">{point.name}</h3>
                            </div>
                            
                            <div className="space-y-6">
                                <div className="flex items-center justify-between">
                                    <span className="text-xs font-black uppercase tracking-widest text-slate-400 group-hover:text-white/60">Area</span>
                                    <span className="font-bold">{point.area}</span>
                                </div>
                                <div className="flex items-center justify-between">
                                    <span className="text-xs font-black uppercase tracking-widest text-slate-400 group-hover:text-white/60">Students</span>
                                    <span className="font-bold">{point.students}</span>
                                </div>
                                <div className="flex items-center justify-between">
                                    <span className="text-xs font-black uppercase tracking-widest text-slate-400 group-hover:text-white/60">Coords</span>
                                    <span className="font-bold text-[10px] tracking-widest group-hover:text-white/80">{point.coordinates}</span>
                                </div>
                            </div>
                        </div>
                    ))}
                </div>
            </div>
        </Layout>
    );
};

export default BoardingPoints;
