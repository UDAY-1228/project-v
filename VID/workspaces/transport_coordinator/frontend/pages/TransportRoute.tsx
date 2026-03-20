import React from 'react';
import Layout from '../../../../core/frontend/components/Layout';
import Card from '../../../../core/frontend/components/Card';

const TransportRoute: React.FC = () => {
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

    return (
        <Layout sidebarItems={sidebarItems}>
            <div className="flex flex-col gap-10">
                <div className="flex items-center justify-between">
                    <div>
                        <h1 className="text-4xl font-black text-slate-800 tracking-tight">Transport Route</h1>
                        <p className="text-slate-500 font-medium tracking-tight">Real-time GPS tracking and route visualization</p>
                    </div>
                    <div className="flex items-center gap-4">
                        <span className="flex items-center gap-2 px-4 py-2 bg-green-50 text-green-600 rounded-full text-xs font-black uppercase tracking-widest">
                            <span className="w-2 h-2 bg-green-500 rounded-full animate-pulse" />
                            System Live
                        </span>
                    </div>
                </div>

                <div className="bg-slate-900 min-h-[600px] rounded-[4rem] relative overflow-hidden shadow-2xl flex items-center justify-center group border-[12px] border-white ring-1 ring-slate-100">
                    <div className="absolute inset-0 opacity-20 bg-[radial-gradient(#ffffff_1px,transparent_1px)] [background-size:20px_20px]" />
                    
                    <div className="relative text-center p-12">
                        <div className="w-24 h-24 bg-white/10 backdrop-blur-xl rounded-full flex items-center justify-center text-white mb-8 mx-auto group-hover:scale-110 transition-transform duration-500">
                            <span className="material-icons text-5xl">explore</span>
                        </div>
                        <h2 className="text-3xl font-black text-white tracking-tight mb-4">Interactive Map View</h2>
                        <p className="max-w-md text-slate-400 font-medium leading-relaxed mb-10">
                            Real-time GPS data for all active fleet buses. Monitor speed, location, and estimated arrival times for every stop on the North, East, and South routes.
                        </p>
                        <button className="px-10 py-4 bg-indigo-500 text-white rounded-2xl font-black uppercase tracking-widest text-[11px] shadow-2xl shadow-indigo-500/50 hover:bg-indigo-400 hover:-translate-y-1 transition-all">
                            Enable Tracking API
                        </button>
                    </div>
                </div>
            </div>
        </Layout>
    );
};

export default TransportRoute;
