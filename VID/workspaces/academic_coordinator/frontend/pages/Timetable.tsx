import React, { useState, useEffect } from 'react';
import Layout from '../../../../core/frontend/components/Layout';
import { TIMETABLE_SIDEBAR_ACADEMIC, subjectColor } from '../../../../core/frontend/utils/timetableConstants';
import axios from 'axios';

const DAYS_ALL = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'];
const PERIODS_ALL = [3, 4, 5, 6, 7];
const BREAK_TIMES = ['10:00-11:00', '11:00-12:00', '12:00-1:00', '1:00-2:00'];
const DAY_MAP: Record<string, string> = { Mon: 'Monday', Tue: 'Tuesday', Wed: 'Wednesday', Thu: 'Thursday', Fri: 'Friday', Sat: 'Saturday' };

const TimetablePage: React.FC = () => {
  const [classes, setClasses] = useState<string[]>([]);
  const [selectedClass, setSelectedClass] = useState('');
  const [workingDays, setWorkingDays] = useState(['Mon', 'Tue', 'Wed', 'Thu', 'Fri']);
  const [periodsPerDay, setPeriodsPerDay] = useState(5);
  const [breakTime, setBreakTime] = useState('12:00-1:00');
  const [timetable, setTimetable] = useState<any>(null);
  const [loading, setLoading] = useState(false);
  const [generating, setGenerating] = useState(false);
  const [editMode, setEditMode] = useState(false);
  const [toast, setToast] = useState('');
  const [course, setCourse] = useState<any>(null);

  const showToast = (msg: string) => { setToast(msg); setTimeout(() => setToast(''), 3000); };

  useEffect(() => {
    axios.get('/api/timetable/classes').then(r => setClasses(r.data.classes)).catch(() => setClasses(['CSE-A', 'CSE-B', 'ECE-A']));
  }, []);

  useEffect(() => {
    if (!selectedClass) return;
    // Load existing timetable
    setLoading(true);
    axios.get(`/api/timetable/${selectedClass}`)
      .then(r => { setTimetable(r.data); setLoading(false); })
      .catch(() => { setTimetable(null); setLoading(false); });
    // Load course
    axios.get(`/api/timetable/courses/${selectedClass}`)
      .then(r => setCourse(r.data)).catch(() => setCourse(null));
  }, [selectedClass]);

  const toggleDay = (d: string) => {
    setWorkingDays(prev => prev.includes(d) ? prev.filter(x => x !== d) : [...prev, d]);
  };

  const generate = async () => {
    if (!selectedClass) { showToast('Please select a class first.'); return; }
    setGenerating(true);
    try {
      const ordered = DAYS_ALL.filter(d => workingDays.includes(d)).map(d => DAY_MAP[d]);
      const r = await axios.post('/api/timetable/generate', {
        classId: selectedClass, workingDays: ordered, periodsPerDay, breakTime
      });
      setTimetable(r.data.timetable);
      showToast('✅ Timetable generated successfully!');
    } catch (e: any) {
      showToast('❌ ' + (e.response?.data?.detail || 'Generation failed'));
    } finally { setGenerating(false); }
  };

  const save = async () => {
    if (!timetable) return;
    try {
      await axios.put(`/api/timetable/${timetable.classId}`, { schedule: timetable.schedule });
      showToast('✅ Timetable saved!');
      setEditMode(false);
    } catch { showToast('❌ Save failed'); }
  };

  const updateCell = (dayIdx: number, periodIdx: number, field: string, value: string) => {
    setTimetable((prev: any) => {
      const next = JSON.parse(JSON.stringify(prev));
      next.schedule[dayIdx].periods[periodIdx][field] = value;
      return next;
    });
  };

  return (
    <Layout sidebarItems={TIMETABLE_SIDEBAR_ACADEMIC}>
      <div className="flex flex-col gap-8">
        {/* Toast */}
        {toast && (
          <div className="fixed top-6 right-6 z-50 px-6 py-4 bg-slate-900 text-white rounded-2xl shadow-2xl font-bold text-sm animate-in fade-in slide-in-from-top-4">
            {toast}
          </div>
        )}

        {/* Header */}
        <div className="flex items-center justify-between flex-wrap gap-4">
          <div>
            <h1 className="text-4xl font-black text-slate-900 tracking-tight">Timetable Management</h1>
            <p className="text-slate-500 font-medium mt-1">Generate, view, and edit class timetables</p>
          </div>
          {timetable && (
            <div className="flex gap-3">
              {editMode ? (
                <>
                  <button onClick={save} className="px-5 py-2.5 bg-emerald-600 text-white font-black text-sm rounded-xl hover:bg-emerald-700 transition-all">Save Changes</button>
                  <button onClick={() => setEditMode(false)} className="px-5 py-2.5 bg-slate-200 text-slate-700 font-black text-sm rounded-xl hover:bg-slate-300 transition-all">Cancel</button>
                </>
              ) : (
                <button onClick={() => setEditMode(true)} className="px-5 py-2.5 bg-indigo-600 text-white font-black text-sm rounded-xl hover:bg-indigo-700 transition-all flex items-center gap-2">
                  <span className="material-icons text-sm">edit</span> Edit Timetable
                </button>
              )}
            </div>
          )}
        </div>

        {/* Controls */}
        <div className="bg-white rounded-3xl border border-slate-100 shadow-xl p-8 grid md:grid-cols-2 lg:grid-cols-4 gap-6">
          {/* Class Selector */}
          <div className="space-y-2">
            <label className="text-[10px] font-black uppercase tracking-widest text-slate-400">Select Class</label>
            <select
              className="w-full border-2 border-slate-100 rounded-2xl py-3 px-4 font-bold text-slate-700 outline-none focus:border-indigo-500 transition-all bg-slate-50"
              value={selectedClass}
              onChange={e => setSelectedClass(e.target.value)}
            >
              <option value="">-- Choose Class --</option>
              {classes.map(c => <option key={c} value={c}>{c}</option>)}
            </select>
          </div>

          {/* Periods per day */}
          <div className="space-y-2">
            <label className="text-[10px] font-black uppercase tracking-widest text-slate-400">Periods Per Day</label>
            <select
              className="w-full border-2 border-slate-100 rounded-2xl py-3 px-4 font-bold text-slate-700 outline-none focus:border-indigo-500 bg-slate-50"
              value={periodsPerDay}
              onChange={e => setPeriodsPerDay(+e.target.value)}
            >
              {PERIODS_ALL.map(p => <option key={p} value={p}>{p} Periods</option>)}
            </select>
          </div>

          {/* Break time */}
          <div className="space-y-2">
            <label className="text-[10px] font-black uppercase tracking-widest text-slate-400">Break Time</label>
            <select
              className="w-full border-2 border-slate-100 rounded-2xl py-3 px-4 font-bold text-slate-700 outline-none focus:border-indigo-500 bg-slate-50"
              value={breakTime}
              onChange={e => setBreakTime(e.target.value)}
            >
              {BREAK_TIMES.map(b => <option key={b} value={b}>{b}</option>)}
            </select>
          </div>

          {/* Working Days */}
          <div className="space-y-2">
            <label className="text-[10px] font-black uppercase tracking-widest text-slate-400">Working Days</label>
            <div className="flex flex-wrap gap-2">
              {DAYS_ALL.map(d => (
                <button
                  key={d}
                  onClick={() => toggleDay(d)}
                  className={`px-3 py-1.5 rounded-xl text-xs font-black border-2 transition-all ${workingDays.includes(d) ? 'bg-indigo-600 text-white border-indigo-600' : 'bg-slate-50 text-slate-500 border-slate-100 hover:border-indigo-300'}`}
                >
                  {d}
                </button>
              ))}
            </div>
          </div>

          {/* Course preview */}
          {course && (
            <div className="md:col-span-2 lg:col-span-3 space-y-2">
              <label className="text-[10px] font-black uppercase tracking-widest text-slate-400">Course Subjects</label>
              <div className="flex flex-wrap gap-2">
                {course.subjects?.map((s: any) => (
                  <span key={s.subject} className={`px-3 py-1 rounded-lg text-xs font-black border ${subjectColor(s.subject)}`}>
                    {s.subject}
                  </span>
                ))}
              </div>
            </div>
          )}

          {/* Generate button */}
          <div className="flex items-end">
            <button
              onClick={generate}
              disabled={generating || !selectedClass}
              className="w-full py-3 bg-gradient-to-r from-indigo-600 to-violet-600 text-white font-black rounded-2xl shadow-lg shadow-indigo-200 hover:scale-[1.02] transition-all disabled:opacity-50 disabled:cursor-not-allowed flex items-center justify-center gap-2 text-sm"
            >
              {generating ? (
                <><span className="material-icons text-sm animate-spin">refresh</span> Generating...</>
              ) : (
                <><span className="material-icons text-sm">auto_awesome</span> Generate Timetable</>
              )}
            </button>
          </div>
        </div>

        {/* Timetable Grid */}
        {loading && (
          <div className="bg-white rounded-3xl border border-slate-100 shadow-xl p-20 flex items-center justify-center">
            <span className="material-icons text-4xl text-indigo-400 animate-spin">refresh</span>
          </div>
        )}

        {!loading && timetable && (
          <div className="bg-white rounded-3xl border border-slate-100 shadow-xl overflow-hidden">
            <div className="px-8 py-6 border-b border-slate-100 flex items-center justify-between">
              <div>
                <h2 className="text-xl font-black text-slate-900">Class: {timetable.classId}</h2>
                <p className="text-slate-400 text-sm font-medium mt-0.5">{timetable.schedule?.length} working days • {editMode ? '✏️ Edit mode active' : '👁 View mode'}</p>
              </div>
            </div>

            {/* Scrollable grid */}
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
                    <tr key={di} className="border-b border-slate-50 hover:bg-slate-50/50 transition-colors">
                      <td className="px-6 py-4 font-black text-slate-700">{dayObj.day}</td>
                      {dayObj.periods?.map((period: any, pi: number) => (
                        <td key={pi} className="px-2 py-3 text-center">
                          {period.isBreak ? (
                            <div className="mx-auto max-w-[100px] px-3 py-2 rounded-xl bg-slate-100 text-slate-400 text-[10px] font-black uppercase tracking-widest border border-slate-200">
                              ☕ Break
                            </div>
                          ) : editMode ? (
                            <input
                              className={`w-full text-center text-xs font-bold px-2 py-2 rounded-xl border-2 outline-none ${subjectColor(period.subject)}`}
                              value={period.subject}
                              onChange={e => updateCell(di, pi, 'subject', e.target.value)}
                            />
                          ) : (
                            <div className={`mx-auto max-w-[120px] px-3 py-2 rounded-xl border text-xs font-black ${subjectColor(period.subject)}`}>
                              <div>{period.subject}</div>
                              {period.substituteId && (
                                <div className="text-[9px] mt-0.5 text-orange-600 font-black">⚡ SUB</div>
                              )}
                            </div>
                          )}
                        </td>
                      ))}
                    </tr>
                  ))}
                </tbody>
              </table>
            </div>

            {/* Legend */}
            <div className="px-8 py-5 border-t border-slate-100 flex flex-wrap gap-2 items-center">
              <span className="text-[10px] font-black uppercase tracking-widest text-slate-400 mr-2">Legend:</span>
              {Array.from(new Set(
                timetable.schedule?.flatMap((d: any) => d.periods?.filter((p: any) => !p.isBreak).map((p: any) => p.subject))
              )).map((sub: any) => (
                <span key={sub} className={`px-3 py-1 rounded-lg text-[10px] font-black border ${subjectColor(sub)}`}>{sub}</span>
              ))}
              <span className="px-3 py-1 rounded-lg text-[10px] font-black border bg-orange-50 text-orange-600 border-orange-200">⚡ SUB = Substitute</span>
            </div>
          </div>
        )}

        {!loading && !timetable && selectedClass && (
          <div className="bg-white rounded-3xl border-2 border-dashed border-slate-200 p-20 text-center">
            <span className="material-icons text-5xl text-slate-300 mb-4 block">calendar_month</span>
            <p className="text-slate-500 font-bold">No timetable found for <strong>{selectedClass}</strong>.</p>
            <p className="text-slate-400 text-sm mt-1">Click "Generate Timetable" above to create one.</p>
          </div>
        )}

        {!selectedClass && (
          <div className="bg-white rounded-3xl border-2 border-dashed border-slate-200 p-20 text-center">
            <span className="material-icons text-5xl text-slate-300 mb-4 block">school</span>
            <p className="text-slate-500 font-bold">Select a class to get started.</p>
          </div>
        )}
      </div>
    </Layout>
  );
};

export default TimetablePage;
