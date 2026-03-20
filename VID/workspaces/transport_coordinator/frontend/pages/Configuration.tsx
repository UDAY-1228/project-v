import React from 'react';
import Layout from '../../../../core/frontend/components/Layout';
import Card from '../../../../core/frontend/components/Card';

const Configuration: React.FC = () => {
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

    const settings = [
        { title: "Transport Fees", description: "Set monthly and annual transport fee structures based on zones and distance.", icon: "payments" },
        { title: "Notification Settings", description: "Configure automated SMS and email alerts for delays and schedule changes.", icon: "notifications" },
        { title: "Fuel Management", description: "Log and track fuel consumption and maintenance costs across the fleet.", icon: "local_gas_station" },
        { title: "Driver Profiles", description: "Update driver documentation, contact details, and license verification.", icon: "contact_emergency" },
        { title: "Route Planning Params", description: "Define maximum radius and pick-up time windows for automated planning.", icon: "auto_fix_high" },
        { title: "Security Settings", description: "Manage GPS tracking access and real-time location sharing permissions.", icon: "security" }
    ];

    return (
        <Layout sidebarItems={sidebarItems}>
            <div className="flex flex-col gap-10">
                <div className="flex items-center justify-between">
                    <div>
                        <h1 className="text-4xl font-black text-slate-800 tracking-tight">Configuration</h1>
                        <p className="text-slate-500 font-medium tracking-tight">General settings and transport module parameters</p>
                    </div>
                </div>

                <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
                    {settings.map((setting, idx) => (
                        <div key={idx} className="bg-white p-10 rounded-[3.5rem] border border-slate-100 shadow-xl shadow-slate-100/50 hover:bg-slate-50 transition-all duration-300 group">
                            <div className="w-14 h-14 bg-indigo-50 text-indigo-500 rounded-2xl flex items-center justify-center mb-8 group-hover:bg-indigo-500 group-hover:text-white transition-all transform group-hover:scale-110">
                                <span className="material-icons text-2xl font-black">{setting.icon}</span>
                            </div>
                            <h3 className="text-xl font-extrabold tracking-tight text-slate-800 mb-2">{setting.title}</h3>
                            <p className="text-sm text-slate-500 font-medium mb-10 leading-relaxed">{setting.description}</p>
                            
                            <button className="w-full py-4 bg-slate-50 rounded-2xl text-slate-400 font-black uppercase tracking-widest text-[10px] group-hover:bg-indigo-600 group-hover:text-white transition-all">
                                Configure
                            </button>
                        </div>
                    ))}
                </div>
            </div>
        </Layout>
    );
};

export default Configuration;
