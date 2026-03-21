import React, { useState, useEffect } from 'react';
import Layout from '../../../../core/frontend/components/Layout';
import { subjectColor } from '../../../../core/frontend/utils/timetableConstants';
import axios from 'axios';

const STUDENT_SIDEBAR = [
  { label: "Digital Notice Board", icon: "announcement", path: "/student/notice-board" },
  { label: "Dashboard", icon: "dashboard", path: "/student/dashboard" },
  { label: "Attendance", icon: "how_to_reg", path: "/student/attendance" },
  { label: "My Timetable", icon: "calendar_month", path: "/student/timetable" },
  { label: "Examinations", icon: "quiz", path: "/student/examinations" },
  { label: "Fees", icon: "payments", path: "/student/fees" },
  { label: "Learning Management", icon: "play_lesson", path: "/student/learning-management" },
  { label: "Course Tracking", icon: "track_changes", path: "/student/course-tracking" },
  { label: "Co-Curricular", icon: "sports", path: "/student/co-curricular-activities" },
  { label: "Chatbot", icon: "smart_toy", path: "/student/chatbot" },
  { label: "Profile", icon: "person", path: "/student/profile" },
];

// Hardcoded for demo — in production read from user session
const MY_CLASS = 'CSE-A';

const StudentTimetableView: React.FC = () => {
  const [timetable, setTimetable] = useState<any>(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    axios.get(`/api/timetable/${MY_CLASS}`)
      .then(r => { setTimetable(r.data); setLoading(false); })
      .catch(() => { setTimetable(null); setLoading(false); });
  }, []);

  const todayDay = new Date().toLocaleDateString('en-US', { weekday: 'long' });
  const todaySchedule = timetable?.schedule?.find((d: any) => d.day === todayDay);

  return (
    <Layout sidebarItems={STUDENT_SIDEBAR}>
      <div className="flex flex-col gap-8">
        <div className="flex items-center justify-between flex-wrap gap-4">
          <div>
            <h1 className="text-4xl font-black text-slate-900 tracking-tight">My Timetable</h1>
            <p className="text-slate-500 font-medium mt-1">Class: <strong>{MY_CLASS}</strong> · View-only</p>
          </div>
          <span className="px-3 py-1.5 bg-emerald-50 text-emerald-600 border border-emerald-200 rounded-xl text-xs font-black uppercase tracking-widest">View Only</span>
        </div>

        {loading && (
          <div className="bg-white rounded-3xl border border-slate-100 shadow-xl p-20 flex items-center justify-center">
            <span className="material-icons text-4xl text-indigo-400 animate-spin">refresh</span>
          </div>
        )}

        {/* Today's Schedule highlight */}
        {!loading && todaySchedule && (
          <div className="bg-gradient-to-r from-indigo-600 to-violet-700 rounded-3xl p-8 text-white shadow-2xl shadow-indigo-200">
            <div className="flex items-center gap-3 mb-5">
              <span className="material-icons text-2xl">today</span>
              <div>
                <h2 className="font-black text-xl">Today — {todayDay}</h2>
                <p className="text-indigo-200 text-sm font-medium">{todaySchedule.periods?.filter((p: any) => !p.isBreak).length} classes today</p>
              </div>
            </div>
            <div className="grid grid-cols-2 sm:grid-cols-3 lg:grid-cols-5 gap-3">
              {todaySchedule.periods?.map((p: any, i: number) => (
                <div key={i} className={`p-4 rounded-2xl text-center ${p.isBreak ? 'bg-white/10' : 'bg-white/20 hover:bg-white/30'} transition-all`}>
                  <p className="text-white/60 text-[10px] font-black uppercase tracking-widest mb-1">{p.time}</p>
                  <p className="font-black text-white">{p.isBreak ? '☕ Break' : p.subject}</p>
                  {p.substituteId && <p className="text-yellow-300 text-[10px] font-black mt-1">⚡ Substitute</p>}
                </div>
              ))}
            </div>
          </div>
        )}

        {/* Full Week timetable */}
        {!loading && timetable && (
          <div className="bg-white rounded-3xl border border-slate-100 shadow-xl overflow-hidden">
            <div className="px-8 py-6 border-b border-slate-100">
              <h2 className="text-xl font-black text-slate-900">Full Week Schedule</h2>
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
                    <tr key={di} className={`border-b border-slate-50 hover:bg-slate-50/50 ${dayObj.day === todayDay ? 'bg-indigo-50/30' : ''}`}>
                      <td className={`px-6 py-4 font-black ${dayObj.day === todayDay ? 'text-indigo-600' : 'text-slate-700'}`}>
                        {dayObj.day}
                        {dayObj.day === todayDay && <span className="ml-2 text-[9px] bg-indigo-600 text-white px-2 py-0.5 rounded-full font-black">TODAY</span>}
                      </td>
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
          </div>
        )}

        {!loading && !timetable && (
          <div className="bg-white rounded-3xl border-2 border-dashed border-slate-200 p-20 text-center">
            <span className="material-icons text-5xl text-slate-300 mb-4 block">calendar_month</span>
            <p className="text-slate-500 font-bold">No timetable available for your class yet.</p>
          </div>
        )}
      </div>
    </Layout>
  );
};

export default StudentTimetableView;
