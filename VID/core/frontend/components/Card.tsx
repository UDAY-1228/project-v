import React from 'react';

interface CardProps {
    title: string;
    value: string | number;
    icon: string;
    color: 'blue' | 'green' | 'yellow' | 'red' | 'indigo';
}

const Card: React.FC<CardProps> = ({ title, value, icon, color }) => {
    const colorClasses = {
        blue: 'bg-blue-50 text-blue-600',
        green: 'bg-emerald-50 text-emerald-600',
        yellow: 'bg-amber-50 text-amber-600',
        red: 'bg-rose-50 text-rose-600',
        indigo: 'bg-indigo-50 text-indigo-600'
    };

    return (
        <div className="bg-white p-10 rounded-[3rem] shadow-2xl shadow-slate-200/50 border border-slate-100 flex flex-col gap-8 hover:scale-[1.02] transition-all duration-300">
            <div className={`w-16 h-16 rounded-3xl flex items-center justify-center ${colorClasses[color]}`}>
                <span className="material-icons text-3xl font-black">{icon}</span>
            </div>
            <div>
                <p className="text-[10px] font-black text-slate-400 uppercase tracking-[0.2em] mb-2">{title}</p>
                <p className="text-4xl font-black text-slate-800 tracking-tight">{value}</p>
            </div>
            <div className="pt-6 border-t border-slate-50 flex items-center justify-between">
                <span className="text-[10px] font-bold text-slate-300 uppercase tracking-widest">Real-time status</span>
                <span className="w-2 h-2 rounded-full bg-emerald-400 animate-pulse"></span>
            </div>
        </div>
    );
};

export default Card;
