import React, { useState, useEffect } from 'react';
import Layout from '../../../../core/frontend/components/Layout';
import { subjectColor } from '../../../../core/frontend/utils/timetableConstants';
import axios from 'axios';

const FACULTY_SIDEBAR = [
  { label: "Digital Notice Board", icon: "announcement", path: "/faculty/notice-board" },
  { label: "Dashboard", icon: "dashboard", path: "/faculty/dashboard" },
  { label: "My Courses", icon: "menu_book", path: "/faculty/my-courses" },
  { label: "Class Timetable", icon: "calendar_month", path: "/faculty/class-timetable" },
  { label: "My Mentees", icon: "supervisor_account", path: "/faculty/my-mentees" },
  { label: "Question Banks", icon: "quiz", path: "/faculty/question-banks" },
  { label: "My Profile", icon: "person", path: "/faculty/my-profile" },
  { label: "Research Scholar", icon: "science", path: "/faculty/research-scholar" },
  { label: "LMS", icon: "play_lesson", path: "/faculty/lms" },
  { label: "Activities", icon: "local_activity", path: "/faculty/activities" },
];

const FacultyTimetableView: React.FC = () => {
  const [classes, setClasses] = useState<string[]>([]);
  const [selectedClass, setSelectedClass] = useState('');
  const [timetable, setTimetable] = useState<any>(null);
  const [loading, setLoading] = useState(false);

  useEffect(() => {
    axios.get('/api/timetable/classes')
      .then(r => { setClasses(r.data.classes); if (r.data.classes.length > 0) setSelectedClass(r.data.classes[0]); })
      .catch(() => setClasses([]));
  }, []);

  useEffect(() => {
    if (!selectedClass) return;
    setLoading(true);
    axios.get(`/api/timetable/${selectedClass}`)
      .then(r => { setTimetable(r.data); setLoading(false); })
      .catch(() => { setTimetable(null); setLoading(false); });
  }, [selectedClass]);

  return (
    <Layout sidebarItems={FACULTY_SIDEBAR}>
      <div className="flex flex-col gap-8">
        <div className="flex items-center justify-between flex-wrap gap-4">
          <div>
            <h1 className="text-4xl font-black text-slate-900 tracking-tight">Class Timetable</h1>
            <p className="text-slate-500 font-medium mt-1">View-only — managed by academic coordinator</p>
          </div>
          <div className="flex items-center gap-3">
            <span className="px-3 py-1.5 bg-sky-50 text-sky-600 border border-sky-200 rounded-xl text-xs font-black uppercase tracking-widest">View Only</span>
            <select
              className="border-2 border-slate-100 rounded-2xl py-2.5 px-4 font-bold text-slate-700 outline-none focus:border-indigo-500 bg-slate-50 text-sm"
              value={selectedClass}
              onChange={e => setSelectedClass(e.target.value)}
            >
              {classes.map(c => <option key={c} value={c}>{c}</option>)}
            </select>
          </div>
        </div>

        {loading && (
          <div className="bg-white rounded-3xl border border-slate-100 shadow-xl p-20 flex items-center justify-center">
            <span className="material-icons text-4xl text-indigo-400 animate-spin">refresh</span>
          </div>
        )}

        {!loading && timetable && (
          <div className="bg-white rounded-3xl border border-slate-100 shadow-xl overflow-hidden">
            <div className="px-8 py-6 border-b border-slate-100 bg-gradient-to-r from-sky-50 to-indigo-50">
              <h2 className="text-xl font-black text-slate-900">Class: {timetable.classId}</h2>
              <p className="text-slate-500 text-sm font-medium mt-0.5">{timetable.schedule?.length} days per week</p>
            </div>
            <div className="overflow-x-auto">
              <table className="w-full text-sm">
                <thead>
                  <tr className="bg-slate-50 border-b border-slate-100">
                    <th className="px-6 py-4 text-left font-black text-slate-500 uppercase tracking-widest text-[10px] w-28">Day</th>
                    {timetable.schedule?.[0]?.periods?.map((p: any, i: number) => (
                      <th key={i} className="px-4 py-4 text-center font-black text-slate-500 uppercase tracking-widest text-[10px]">{p.time}</th>
                    ))}
                  </tr>
                </thead>
                <tbody>
                  {timetable.schedule?.map((dayObj: any, di: number) => (
                    <tr key={di} className="border-b border-slate-50 hover:bg-slate-50/50">
                      <td className="px-6 py-4 font-black text-slate-700">{dayObj.day}</td>
                      {dayObj.periods?.map((period: any, pi: number) => (
                        <td key={pi} className="px-2 py-3 text-center">
                          {period.isBreak ? (
                            <div className="mx-auto max-w-[100px] px-3 py-2 rounded-xl bg-slate-100 text-slate-400 text-[10px] font-black uppercase">☕ Break</div>
                          ) : (
                            <div className={`mx-auto max-w-[120px] px-3 py-2 rounded-xl border text-xs font-black ${subjectColor(period.subject)}`}>
                              <div>{period.subject}</div>
                              {period.substituteId && <div className="text-[9px] mt-0.5 text-orange-600 font-black">⚡ SUB</div>}
                            </div>
                          )}
                        </td>
                      ))}
                    </tr>
                  ))}
                </tbody>
              </table>
            </div>
            <div className="px-8 py-5 border-t border-slate-100 flex flex-wrap gap-2 items-center">
              <span className="text-[10px] font-black uppercase tracking-widest text-slate-400 mr-2">Subjects:</span>
              {Array.from(new Set(timetable.schedule?.flatMap((d: any) => d.periods?.filter((p: any) => !p.isBreak).map((p: any) => p.subject)))).map((sub: any) => (
                <span key={sub} className={`px-3 py-1 rounded-lg text-[10px] font-black border ${subjectColor(sub)}`}>{sub}</span>
              ))}
            </div>
          </div>
        )}

        {!loading && !timetable && selectedClass && (
          <div className="bg-white rounded-3xl border-2 border-dashed border-slate-200 p-20 text-center">
            <span className="material-icons text-5xl text-slate-300 mb-4 block">calendar_month</span>
            <p className="text-slate-500 font-bold">No timetable available for {selectedClass} yet.</p>
            <p className="text-slate-400 text-sm mt-1">Please contact the academic coordinator.</p>
          </div>
        )}
      </div>
    </Layout>
  );
};

export default FacultyTimetableView;
