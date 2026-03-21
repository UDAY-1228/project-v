import React, { useState, useEffect } from 'react';
import Layout from '../../../../core/frontend/components/Layout';
import { TIMETABLE_SIDEBAR_ACADEMIC, subjectColor } from '../../../../core/frontend/utils/timetableConstants';
import axios from 'axios';

const FacultyAbsencePage: React.FC = () => {
  const [faculty, setFaculty] = useState<any[]>([]);
  const [absences, setAbsences] = useState<any[]>([]);
  const [classes, setClasses] = useState<string[]>([]);
  const [selectedFaculty, setSelectedFaculty] = useState('');
  const [absenceDate, setAbsenceDate] = useState('');
  const [affected, setAffected] = useState<any[]>([]);
  const [suggestions, setSuggestions] = useState<any[]>([]);
  const [toast, setToast] = useState('');
  const [loading, setLoading] = useState(false);
  // Substitute state
  const [subTarget, setSubTarget] = useState<any>(null);
  const [subSelected, setSubSelected] = useState('');

  const showToast = (msg: string) => { setToast(msg); setTimeout(() => setToast(''), 3500); };

  useEffect(() => {
    axios.get('/api/timetable/faculty').then(r => setFaculty(r.data.faculty)).catch(() => setFaculty([]));
    axios.get('/api/timetable/classes').then(r => setClasses(r.data.classes)).catch(() => setClasses([]));
    loadAbsences();
  }, []);

  const loadAbsences = () => {
    axios.get('/api/timetable/absence/all').then(r => setAbsences(r.data.absences || [])).catch(() => setAbsences([]));
  };

  const markAbsent = async () => {
    if (!selectedFaculty || !absenceDate) { showToast('Select faculty and date.'); return; }
    setLoading(true);
    try {
      const r = await axios.post('/api/timetable/absence/mark', { facultyId: selectedFaculty, date: absenceDate });
      setAffected(r.data.affectedPeriods || []);
      showToast('✅ Faculty marked absent');
      loadAbsences();
      // Get suggestions from first affected period
      if (r.data.affectedPeriods?.length > 0) {
        const subj = r.data.affectedPeriods[0].subject;
        const sr = await axios.get(`/api/timetable/substitute/${selectedFaculty}/${subj}`);
        setSuggestions(sr.data.suggestions || []);
      }
    } catch (e: any) {
      showToast('❌ ' + (e.response?.data?.detail || 'Error'));
    } finally { setLoading(false); }
  };

  const assignSub = async (period: any) => {
    if (!subSelected) { showToast('Select a substitute faculty first.'); return; }
    try {
      await axios.post('/api/timetable/substitute/assign', {
        classId: period.classId, day: period.day, timeSlot: period.time, substituteFacultyId: subSelected
      });
      showToast('✅ Substitute assigned for ' + period.time + ' (' + period.classId + ')');
    } catch { showToast('❌ Assignment failed'); }
  };

  const facultyName = (id: string) => faculty.find(f => f.facultyId === id)?.name || id;

  return (
    <Layout sidebarItems={TIMETABLE_SIDEBAR_ACADEMIC}>
      <div className="flex flex-col gap-8">
        {toast && (
          <div className="fixed top-6 right-6 z-50 px-6 py-4 bg-slate-900 text-white rounded-2xl shadow-2xl font-bold text-sm">
            {toast}
          </div>
        )}

        {/* Header */}
        <div>
          <h1 className="text-4xl font-black text-slate-900 tracking-tight">Faculty Absence Manager</h1>
          <p className="text-slate-500 font-medium mt-1">Mark faculty absent, view affected periods & assign substitutes</p>
        </div>

        <div className="grid lg:grid-cols-3 gap-8">
          {/* Mark Absent Panel */}
          <div className="lg:col-span-1 space-y-6">
            <div className="bg-white rounded-3xl border border-slate-100 shadow-xl p-8 space-y-6">
              <h2 className="font-black text-slate-800 text-lg flex items-center gap-3">
                <span className="w-2 h-7 bg-rose-500 rounded-full" />
                Mark Faculty Absent
              </h2>

              <div className="space-y-2">
                <label className="text-[10px] font-black uppercase tracking-widest text-slate-400">Select Faculty</label>
                <select
                  className="w-full border-2 border-slate-100 rounded-2xl py-3 px-4 font-bold text-slate-700 outline-none focus:border-rose-400 bg-slate-50"
                  value={selectedFaculty}
                  onChange={e => { setSelectedFaculty(e.target.value); setAffected([]); setSuggestions([]); }}
                >
                  <option value="">-- Select --</option>
                  {faculty.map(f => <option key={f.facultyId} value={f.facultyId}>{f.name}</option>)}
                </select>
              </div>

              <div className="space-y-2">
                <label className="text-[10px] font-black uppercase tracking-widest text-slate-400">Absence Date</label>
                <input
                  type="date"
                  className="w-full border-2 border-slate-100 rounded-2xl py-3 px-4 font-bold text-slate-700 outline-none focus:border-rose-400 bg-slate-50"
                  value={absenceDate}
                  onChange={e => setAbsenceDate(e.target.value)}
                />
              </div>

              <button
                onClick={markAbsent}
                disabled={loading}
                className="w-full py-3 bg-gradient-to-r from-rose-500 to-pink-600 text-white font-black rounded-2xl shadow-lg shadow-rose-200 hover:scale-[1.02] transition-all disabled:opacity-50 flex items-center justify-center gap-2 text-sm"
              >
                <span className="material-icons text-sm">person_off</span>
                {loading ? 'Processing...' : 'Mark Absent'}
              </button>
            </div>

            {/* Absence History */}
            <div className="bg-white rounded-3xl border border-slate-100 shadow-xl p-8">
              <h3 className="font-black text-slate-800 mb-5 text-base flex items-center gap-2">
                <span className="material-icons text-lg text-slate-400">history</span>
                Absence History
              </h3>
              {absences.length === 0 ? (
                <p className="text-slate-400 text-sm font-medium text-center py-6">No absences recorded</p>
              ) : (
                <div className="space-y-3 max-h-60 overflow-y-auto pr-1">
                  {absences.slice().reverse().map((a: any) => (
                    <div key={a.absenceId} className="flex items-center justify-between p-3 bg-rose-50 rounded-2xl border border-rose-100">
                      <div>
                        <p className="font-black text-rose-700 text-sm">{facultyName(a.facultyId)}</p>
                        <p className="text-rose-400 text-[10px] font-bold uppercase">{a.date}</p>
                      </div>
                      <span className="material-icons text-rose-300">event_busy</span>
                    </div>
                  ))}
                </div>
              )}
            </div>
          </div>

          {/* Affected Periods + Substitute */}
          <div className="lg:col-span-2 space-y-6">
            {affected.length > 0 ? (
              <>
                <div className="bg-white rounded-3xl border border-slate-100 shadow-xl p-8">
                  <h2 className="font-black text-slate-800 text-lg flex items-center gap-3 mb-6">
                    <span className="w-2 h-7 bg-orange-400 rounded-full" />
                    Affected Periods ({affected.length})
                  </h2>

                  {/* Substitute selector */}
                  {suggestions.length > 0 && (
                    <div className="mb-6 p-5 bg-indigo-50 rounded-2xl border border-indigo-100">
                      <p className="text-xs font-black uppercase tracking-widest text-indigo-500 mb-3">Auto-Suggested Substitutes</p>
                      <div className="flex flex-wrap gap-2 mb-3">
                        {suggestions.map((s: any) => (
                          <button
                            key={s.facultyId}
                            onClick={() => setSubSelected(s.facultyId)}
                            className={`px-4 py-2 rounded-xl text-sm font-black border-2 transition-all ${subSelected === s.facultyId ? 'bg-indigo-600 text-white border-indigo-600' : 'bg-white text-indigo-700 border-indigo-200 hover:border-indigo-400'}`}
                          >
                            {s.name}
                            <span className="text-[10px] ml-1 opacity-60">({s.subjects?.join(', ')})</span>
                          </button>
                        ))}
                      </div>
                    </div>
                  )}

                  <div className="space-y-3">
                    {affected.map((p: any, i: number) => (
                      <div key={i} className="flex items-center justify-between p-4 bg-orange-50 rounded-2xl border border-orange-100 group">
                        <div className="flex items-center gap-4">
                          <div className="w-12 h-12 bg-orange-100 rounded-2xl flex items-center justify-center">
                            <span className="material-icons text-orange-500">schedule</span>
                          </div>
                          <div>
                            <p className="font-black text-slate-800">{p.classId} — {p.day}</p>
                            <p className="text-sm text-slate-500 font-medium">{p.time} · <span className={`px-2 py-0.5 rounded-lg text-xs font-black border ${subjectColor(p.subject)}`}>{p.subject}</span></p>
                          </div>
                        </div>
                        <button
                          onClick={() => assignSub(p)}
                          disabled={!subSelected}
                          className="px-4 py-2 bg-indigo-600 text-white font-black text-xs rounded-xl hover:bg-indigo-700 transition-all disabled:opacity-40 disabled:cursor-not-allowed"
                        >
                          Assign Sub
                        </button>
                      </div>
                    ))}
                  </div>
                </div>
              </>
            ) : (
              <div className="bg-white rounded-3xl border-2 border-dashed border-slate-200 p-20 text-center h-full flex flex-col items-center justify-center">
                <span className="material-icons text-5xl text-slate-300 mb-4">person_search</span>
                <p className="text-slate-500 font-bold">Mark a faculty absent to see affected periods</p>
                <p className="text-slate-400 text-sm mt-1">The system will auto-detect clashes and suggest substitutes.</p>
              </div>
            )}
          </div>
        </div>
      </div>
    </Layout>
  );
};

export default FacultyAbsencePage;
