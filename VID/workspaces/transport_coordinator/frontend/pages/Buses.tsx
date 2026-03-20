import React from 'react';
import Layout from '../../../../core/frontend/components/Layout';
import Card from '../../../../core/frontend/components/Card';

const Buses: React.FC = () => {
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

    const buses = [
        { id: "B-201", number: "KA-01-F-1234", capacity: 50, driver: "John Doe", status: "Active" },
        { id: "B-202", number: "KA-01-F-5678", capacity: 40, driver: "Jane Smith", status: "In Maintenance" },
        { id: "B-203", number: "KA-01-G-9012", capacity: 50, driver: "Bob Brown", status: "Active" }
    ];

    return (
        <Layout sidebarItems={sidebarItems}>
            <div className="flex flex-col gap-10">
                <div className="flex items-center justify-between">
                    <div>
                        <h1 className="text-4xl font-black text-slate-800 tracking-tight">Buses</h1>
                        <p className="text-slate-500 font-medium tracking-tight">Manage your fleet of school buses</p>
                    </div>
                    <button className="px-6 py-3 bg-indigo-600 text-white rounded-2xl font-bold hover:bg-indigo-700 transition-all flex items-center gap-2">
                        <span className="material-icons text-xl">add</span>
                        Add Bus
                    </button>
                </div>

                <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
                    {buses.map((bus) => (
                        <div key={bus.id} className="bg-white p-8 rounded-[3rem] border border-slate-100 shadow-xl shadow-slate-100/50 flex flex-col items-center text-center group">
                            <div className="w-20 h-20 bg-indigo-50 text-indigo-500 rounded-3xl flex items-center justify-center mb-6 group-hover:bg-indigo-500 group-hover:text-white transition-all transform group-hover:scale-110">
                                <span className="material-icons text-4xl">directions_bus</span>
                            </div>
                            <h3 className="text-2xl font-black text-slate-800 mb-2">{bus.id}</h3>
                            <p className="text-slate-400 font-bold uppercase tracking-widest text-[10px] mb-6">{bus.number}</p>
                            
                            <div className="grid grid-cols-2 gap-4 w-full mb-8">
                                <div className="bg-slate-50 p-4 rounded-2xl">
                                    <p className="text-[10px] font-black text-slate-300 uppercase tracking-widest mb-1">Capacity</p>
                                    <p className="font-bold text-slate-700">{bus.capacity}</p>
                                </div>
                                <div className="bg-slate-50 p-4 rounded-2xl">
                                    <p className="text-[10px] font-black text-slate-300 uppercase tracking-widest mb-1">Status</p>
                                    <p className={`font-bold ${bus.status === 'Active' ? 'text-green-500' : 'text-amber-500'}`}>{bus.status}</p>
                                </div>
                            </div>
                            
                            <div className="w-full h-[1px] bg-slate-50 mb-6" />
                            
                            <div className="flex items-center gap-4 w-full">
                                <div className="w-10 h-10 rounded-full bg-slate-100 flex items-center justify-center text-slate-400">
                                    <span className="material-icons text-xl">person</span>
                                </div>
                                <div className="text-left flex-1 text-sm font-bold text-slate-600">
                                    {bus.driver}
                                </div>
                                <button className="p-2 text-slate-300 hover:text-indigo-600">
                                    <span className="material-icons">more_vert</span>
                                </button>
                            </div>
                        </div>
                    ))}
                </div>
            </div>
        </Layout>
    );
};

export default Buses;
