import React, { useState, useEffect, useRef } from 'react';
import Layout from '../components/Layout';
import axios from 'axios';

// ─── Types ───────────────────────────────────────────────────────────────────
interface Notice {
  id: string;
  title: string;
  content: string;
  category: string;
  priority: 'high' | 'medium' | 'low';
  author: string;
  authorRole: string;
  postedAt: string;
  pinned: boolean;
  tags: string[];
}

const CATEGORIES = ['General', 'Academics', 'Facilities', 'Finance', 'Sports', 'Health', 'Events', 'Hostel', 'Transport'];
const PRIORITIES = ['high', 'medium', 'low'];

const PRIORITY_STYLES: Record<string, string> = {
  high: 'bg-rose-50 text-rose-600 border-rose-200',
  medium: 'bg-amber-50 text-amber-600 border-amber-200',
  low: 'bg-emerald-50 text-emerald-600 border-emerald-200',
};

const CATEGORY_STYLES: Record<string, string> = {
  General: 'bg-slate-100 text-slate-600',
  Academics: 'bg-indigo-50 text-indigo-600',
  Facilities: 'bg-cyan-50 text-cyan-700',
  Finance: 'bg-green-50 text-green-700',
  Sports: 'bg-orange-50 text-orange-600',
  Health: 'bg-pink-50 text-pink-600',
  Events: 'bg-violet-50 text-violet-600',
  Hostel: 'bg-teal-50 text-teal-600',
  Transport: 'bg-sky-50 text-sky-700',
};

function timeAgo(dateStr: string): string {
  const now = new Date();
  const posted = new Date(dateStr);
  const diffMs = now.getTime() - posted.getTime();
  const mins = Math.floor(diffMs / 60000);
  if (mins < 1) return 'Just now';
  if (mins < 60) return `${mins}m ago`;
  const hrs = Math.floor(mins / 60);
  if (hrs < 24) return `${hrs}h ago`;
  const days = Math.floor(hrs / 24);
  return `${days}d ago`;
}

// ─── Main Component ───────────────────────────────────────────────────────────
const SharedNoticeBoard: React.FC<{ sidebarItems: any[]; canPost?: boolean }> = ({
  sidebarItems,
  canPost = true,   // default: can post (student workspaces pass canPost={false})
}) => {
  const [notices, setNotices] = useState<Notice[]>([]);
  const [loading, setLoading] = useState(true);
  const [showForm, setShowForm] = useState(false);
  const [filterCategory, setFilterCategory] = useState('All');
  const [filterPriority, setFilterPriority] = useState('All');
  const [searchQ, setSearchQ] = useState('');
  const [expandedId, setExpandedId] = useState<string | null>(null);
  const [toast, setToast] = useState('');
  const [form, setForm] = useState({
    title: '', content: '', category: 'General', priority: 'medium', author: '', authorRole: '', pinned: false, tags: '',
  });
  const [submitting, setSubmitting] = useState(false);
  const formRef = useRef<HTMLDivElement>(null);

  const showToast = (msg: string) => { setToast(msg); setTimeout(() => setToast(''), 3200); };

  const load = () => {
    setLoading(true);
    axios.get('/api/notices')
      .then(r => { setNotices(r.data.notices || []); setLoading(false); })
      .catch(() => {
        // Fallback static data when API not reachable
        setNotices([]);
        setLoading(false);
      });
  };

  useEffect(() => { load(); }, []);

  // Close form on outside click
  useEffect(() => {
    const handler = (e: MouseEvent) => {
      if (formRef.current && !formRef.current.contains(e.target as Node)) setShowForm(false);
    };
    if (showForm) document.addEventListener('mousedown', handler);
    return () => document.removeEventListener('mousedown', handler);
  }, [showForm]);

  const handlePost = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!form.title.trim() || !form.content.trim()) { showToast('Title and content are required.'); return; }
    setSubmitting(true);
    try {
      await axios.post('/api/notices', {
        ...form,
        tags: form.tags.split(',').map(t => t.trim()).filter(Boolean),
      });
      showToast('✅ Notice posted successfully!');
      setShowForm(false);
      setForm({ title: '', content: '', category: 'General', priority: 'medium', author: '', authorRole: '', pinned: false, tags: '' });
      load();
    } catch { showToast('❌ Failed to post notice.'); }
    finally { setSubmitting(false); }
  };

  const handleDelete = async (id: string) => {
    if (!confirm('Delete this notice?')) return;
    try {
      await axios.delete(`/api/notices/${id}`);
      showToast('🗑 Notice deleted.');
      load();
    } catch { showToast('❌ Delete failed.'); }
  };

  const handlePin = async (id: string) => {
    try {
      const r = await axios.put(`/api/notices/${id}/pin`);
      showToast(r.data.pinned ? '📌 Notice pinned.' : '📌 Notice unpinned.');
      load();
    } catch { showToast('❌ Pin failed.'); }
  };

  // Filtering
  const filtered = notices.filter(n => {
    if (filterCategory !== 'All' && n.category !== filterCategory) return false;
    if (filterPriority !== 'All' && n.priority !== filterPriority) return false;
    if (searchQ && !n.title.toLowerCase().includes(searchQ.toLowerCase()) && !n.content.toLowerCase().includes(searchQ.toLowerCase())) return false;
    return true;
  });

  const pinnedNotices = filtered.filter(n => n.pinned);
  const regularNotices = filtered.filter(n => !n.pinned);

  return (
    <Layout sidebarItems={sidebarItems}>
      <div className="flex flex-col gap-8">
        {/* Toast */}
        {toast && (
          <div className="fixed top-6 right-6 z-[100] px-6 py-4 bg-slate-900 text-white rounded-2xl shadow-2xl font-bold text-sm animate-bounce">
            {toast}
          </div>
        )}

        {/* Header */}
        <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-4">
          <div>
            <h1 className="text-3xl sm:text-4xl font-black text-slate-900 tracking-tight flex items-center gap-3">
              <span className="material-icons text-indigo-500 text-4xl">campaign</span>
              Digital Notice Board
            </h1>
            <p className="text-slate-500 font-medium mt-1 text-sm">
              {canPost ? 'Post and manage institutional announcements' : 'View announcements from your institution'}
            </p>
          </div>
          {canPost && (
            <button
              id="post-notice-btn"
              onClick={() => setShowForm(true)}
              className="flex items-center gap-2 px-6 py-3.5 bg-gradient-to-r from-indigo-600 to-violet-600 text-white font-black rounded-2xl shadow-lg shadow-indigo-200 hover:scale-105 hover:shadow-indigo-300 transition-all text-sm whitespace-nowrap"
            >
              <span className="material-icons text-lg">add</span>
              Post Notice
            </button>
          )}
        </div>

        {/* Stats bar */}
        <div className="grid grid-cols-2 sm:grid-cols-4 gap-4">
          {[
            { label: 'Total Notices', value: notices.length, icon: 'article', color: 'text-indigo-600 bg-indigo-50' },
            { label: 'Pinned', value: notices.filter(n => n.pinned).length, icon: 'push_pin', color: 'text-amber-600 bg-amber-50' },
            { label: 'High Priority', value: notices.filter(n => n.priority === 'high').length, icon: 'priority_high', color: 'text-rose-600 bg-rose-50' },
            { label: 'Categories', value: [...new Set(notices.map(n => n.category))].length, icon: 'category', color: 'text-emerald-600 bg-emerald-50' },
          ].map(s => (
            <div key={s.label} className="bg-white rounded-2xl border border-slate-100 shadow-md p-5 flex items-center gap-4">
              <div className={`w-11 h-11 rounded-xl flex items-center justify-center ${s.color}`}>
                <span className="material-icons text-xl">{s.icon}</span>
              </div>
              <div>
                <p className="text-2xl font-black text-slate-900">{s.value}</p>
                <p className="text-[10px] font-black uppercase tracking-widest text-slate-400">{s.label}</p>
              </div>
            </div>
          ))}
        </div>

        {/* Search + Filters */}
        <div className="bg-white rounded-2xl border border-slate-100 shadow-md p-5 flex flex-col sm:flex-row gap-4">
          <div className="relative flex-1">
            <span className="absolute left-4 top-1/2 -translate-y-1/2 material-icons text-slate-400 text-xl">search</span>
            <input
              type="text"
              placeholder="Search notices..."
              className="w-full pl-12 pr-4 py-3 rounded-xl bg-slate-50 border-2 border-slate-100 focus:border-indigo-400 outline-none font-medium text-slate-700 transition-all"
              value={searchQ}
              onChange={e => setSearchQ(e.target.value)}
            />
          </div>
          <select
            className="border-2 border-slate-100 rounded-xl py-3 px-4 font-bold text-slate-600 outline-none focus:border-indigo-400 bg-slate-50 text-sm"
            value={filterCategory}
            onChange={e => setFilterCategory(e.target.value)}
          >
            <option value="All">All Categories</option>
            {CATEGORIES.map(c => <option key={c} value={c}>{c}</option>)}
          </select>
          <select
            className="border-2 border-slate-100 rounded-xl py-3 px-4 font-bold text-slate-600 outline-none focus:border-indigo-400 bg-slate-50 text-sm"
            value={filterPriority}
            onChange={e => setFilterPriority(e.target.value)}
          >
            <option value="All">All Priorities</option>
            <option value="high">High</option>
            <option value="medium">Medium</option>
            <option value="low">Low</option>
          </select>
        </div>

        {/* Pinned */}
        {pinnedNotices.length > 0 && (
          <div>
            <div className="flex items-center gap-3 mb-4">
              <span className="material-icons text-amber-500">push_pin</span>
              <span className="text-xs font-black uppercase tracking-widest text-amber-600">Pinned Notices</span>
            </div>
            <div className="grid grid-cols-1 md:grid-cols-2 xl:grid-cols-3 gap-5">
              {pinnedNotices.map(n => (
                <NoticeCard
                  key={n.id}
                  notice={n}
                  canPost={canPost}
                  expanded={expandedId === n.id}
                  onToggle={() => setExpandedId(prev => prev === n.id ? null : n.id)}
                  onDelete={handleDelete}
                  onPin={handlePin}
                  pinned
                />
              ))}
            </div>
          </div>
        )}

        {/* All Notices */}
        {loading ? (
          <div className="bg-white rounded-3xl border border-slate-100 shadow-xl p-20 flex flex-col items-center justify-center gap-4">
            <span className="material-icons text-5xl text-indigo-400 animate-spin">refresh</span>
            <p className="text-slate-400 font-bold">Loading notices...</p>
          </div>
        ) : regularNotices.length === 0 && pinnedNotices.length === 0 ? (
          <div className="bg-white rounded-3xl border-2 border-dashed border-slate-200 p-20 text-center">
            <span className="material-icons text-5xl text-slate-300 mb-4 block">campaign</span>
            <p className="text-slate-500 font-bold text-lg">No notices found</p>
            <p className="text-slate-400 text-sm mt-1">{canPost ? 'Click "Post Notice" to create the first announcement.' : 'No announcements at this time.'}</p>
          </div>
        ) : (
          <div>
            {regularNotices.length > 0 && (
              <>
                {pinnedNotices.length > 0 && (
                  <div className="flex items-center gap-3 mb-4">
                    <span className="material-icons text-slate-400">article</span>
                    <span className="text-xs font-black uppercase tracking-widest text-slate-500">All Announcements</span>
                  </div>
                )}
                <div className="grid grid-cols-1 md:grid-cols-2 xl:grid-cols-3 gap-5">
                  {regularNotices.map(n => (
                    <NoticeCard
                      key={n.id}
                      notice={n}
                      canPost={canPost}
                      expanded={expandedId === n.id}
                      onToggle={() => setExpandedId(prev => prev === n.id ? null : n.id)}
                      onDelete={handleDelete}
                      onPin={handlePin}
                    />
                  ))}
                </div>
              </>
            )}
          </div>
        )}
      </div>

      {/* Post Notice Modal */}
      {showForm && canPost && (
        <div className="fixed inset-0 z-50 flex items-center justify-center p-4 bg-slate-900/60 backdrop-blur-sm">
          <div ref={formRef} className="w-full max-w-xl bg-white rounded-[2.5rem] shadow-2xl p-8 sm:p-10 max-h-[90vh] overflow-y-auto">
            <div className="flex items-center justify-between mb-8">
              <div>
                <h2 className="text-2xl font-black text-slate-900">Post a Notice</h2>
                <p className="text-slate-400 text-sm font-medium mt-0.5">It will be visible to all workspace users</p>
              </div>
              <button onClick={() => setShowForm(false)} className="w-10 h-10 rounded-2xl bg-slate-100 hover:bg-slate-200 flex items-center justify-center transition-all">
                <span className="material-icons text-slate-500">close</span>
              </button>
            </div>

            <form onSubmit={handlePost} className="space-y-5">
              <div className="space-y-1.5">
                <label className="text-[10px] font-black uppercase tracking-widest text-slate-400">Title *</label>
                <input
                  className="w-full border-2 border-slate-100 focus:border-indigo-500 rounded-2xl py-3.5 px-5 font-bold text-slate-800 outline-none transition-all bg-slate-50 placeholder:text-slate-300"
                  placeholder="Notice title..."
                  value={form.title}
                  onChange={e => setForm(f => ({ ...f, title: e.target.value }))}
                  required
                />
              </div>

              <div className="space-y-1.5">
                <label className="text-[10px] font-black uppercase tracking-widest text-slate-400">Content *</label>
                <textarea
                  rows={4}
                  className="w-full border-2 border-slate-100 focus:border-indigo-500 rounded-2xl py-3.5 px-5 font-medium text-slate-700 outline-none transition-all bg-slate-50 resize-none placeholder:text-slate-300"
                  placeholder="Describe the announcement in detail..."
                  value={form.content}
                  onChange={e => setForm(f => ({ ...f, content: e.target.value }))}
                  required
                />
              </div>

              <div className="grid grid-cols-2 gap-4">
                <div className="space-y-1.5">
                  <label className="text-[10px] font-black uppercase tracking-widest text-slate-400">Category</label>
                  <select
                    className="w-full border-2 border-slate-100 focus:border-indigo-500 rounded-2xl py-3.5 px-4 font-bold text-slate-700 outline-none bg-slate-50"
                    value={form.category}
                    onChange={e => setForm(f => ({ ...f, category: e.target.value }))}
                  >
                    {CATEGORIES.map(c => <option key={c} value={c}>{c}</option>)}
                  </select>
                </div>
                <div className="space-y-1.5">
                  <label className="text-[10px] font-black uppercase tracking-widest text-slate-400">Priority</label>
                  <select
                    className="w-full border-2 border-slate-100 focus:border-indigo-500 rounded-2xl py-3.5 px-4 font-bold text-slate-700 outline-none bg-slate-50"
                    value={form.priority}
                    onChange={e => setForm(f => ({ ...f, priority: e.target.value }))}
                  >
                    {PRIORITIES.map(p => <option key={p} value={p}>{p.charAt(0).toUpperCase() + p.slice(1)}</option>)}
                  </select>
                </div>
              </div>

              <div className="grid grid-cols-2 gap-4">
                <div className="space-y-1.5">
                  <label className="text-[10px] font-black uppercase tracking-widest text-slate-400">Posted By</label>
                  <input
                    className="w-full border-2 border-slate-100 focus:border-indigo-500 rounded-2xl py-3.5 px-5 font-bold text-slate-700 outline-none bg-slate-50 placeholder:text-slate-300"
                    placeholder="Your name"
                    value={form.author}
                    onChange={e => setForm(f => ({ ...f, author: e.target.value }))}
                  />
                </div>
                <div className="space-y-1.5">
                  <label className="text-[10px] font-black uppercase tracking-widest text-slate-400">Role / Dept</label>
                  <input
                    className="w-full border-2 border-slate-100 focus:border-indigo-500 rounded-2xl py-3.5 px-5 font-bold text-slate-700 outline-none bg-slate-50 placeholder:text-slate-300"
                    placeholder="e.g. HOD / Admin"
                    value={form.authorRole}
                    onChange={e => setForm(f => ({ ...f, authorRole: e.target.value }))}
                  />
                </div>
              </div>

              <div className="space-y-1.5">
                <label className="text-[10px] font-black uppercase tracking-widest text-slate-400">Tags (comma separated)</label>
                <input
                  className="w-full border-2 border-slate-100 focus:border-indigo-500 rounded-2xl py-3.5 px-5 font-medium text-slate-700 outline-none bg-slate-50 placeholder:text-slate-300"
                  placeholder="exam, schedule, important"
                  value={form.tags}
                  onChange={e => setForm(f => ({ ...f, tags: e.target.value }))}
                />
              </div>

              <label className="flex items-center gap-3 cursor-pointer select-none">
                <div
                  onClick={() => setForm(f => ({ ...f, pinned: !f.pinned }))}
                  className={`w-12 h-6 rounded-full transition-all ${form.pinned ? 'bg-indigo-600' : 'bg-slate-200'} relative`}
                >
                  <div className={`w-5 h-5 bg-white rounded-full absolute top-0.5 transition-all shadow-md ${form.pinned ? 'left-6' : 'left-0.5'}`} />
                </div>
                <span className="font-bold text-slate-600 text-sm">Pin this notice (shows at top)</span>
              </label>

              <div className="flex gap-3 pt-2">
                <button
                  type="button"
                  onClick={() => setShowForm(false)}
                  className="flex-1 py-4 bg-slate-100 text-slate-600 font-black rounded-2xl hover:bg-slate-200 transition-all"
                >
                  Cancel
                </button>
                <button
                  type="submit"
                  disabled={submitting}
                  className="flex-1 py-4 bg-gradient-to-r from-indigo-600 to-violet-600 text-white font-black rounded-2xl shadow-lg shadow-indigo-200 hover:scale-[1.02] transition-all disabled:opacity-50 flex items-center justify-center gap-2"
                >
                  {submitting ? (
                    <><span className="material-icons text-sm animate-spin">refresh</span> Posting...</>
                  ) : (
                    <><span className="material-icons text-sm">send</span> Post Notice</>
                  )}
                </button>
              </div>
            </form>
          </div>
        </div>
      )}
    </Layout>
  );
};


// ─── Notice Card ─────────────────────────────────────────────────────────────
const NoticeCard: React.FC<{
  notice: Notice;
  canPost: boolean;
  expanded: boolean;
  pinned?: boolean;
  onToggle: () => void;
  onDelete: (id: string) => void;
  onPin: (id: string) => void;
}> = ({ notice, canPost, expanded, pinned, onToggle, onDelete, onPin }) => {
  const catStyle = CATEGORY_STYLES[notice.category] || 'bg-slate-100 text-slate-600';
  const prioStyle = PRIORITY_STYLES[notice.priority] || 'bg-slate-100 text-slate-600 border-slate-200';

  return (
    <div className={`group bg-white rounded-3xl border-2 shadow-lg hover:shadow-xl transition-all duration-300 hover:-translate-y-0.5 overflow-hidden ${pinned ? 'border-amber-200' : 'border-slate-100'}`}>
      {/* Priority bar */}
      <div className={`h-1.5 w-full ${notice.priority === 'high' ? 'bg-gradient-to-r from-rose-400 to-pink-500' : notice.priority === 'medium' ? 'bg-gradient-to-r from-amber-400 to-orange-400' : 'bg-gradient-to-r from-emerald-400 to-teal-400'}`} />

      <div className="p-6">
        {/* Top row: category + pin badge + time */}
        <div className="flex items-center justify-between mb-4 flex-wrap gap-2">
          <div className="flex items-center gap-2 flex-wrap">
            <span className={`px-3 py-1 rounded-lg text-[10px] font-black uppercase tracking-widest ${catStyle}`}>
              {notice.category}
            </span>
            <span className={`px-3 py-1 rounded-lg text-[10px] font-black uppercase tracking-widest border ${prioStyle}`}>
              {notice.priority}
            </span>
            {notice.pinned && (
              <span className="flex items-center gap-1 text-amber-500 text-[10px] font-black uppercase tracking-widest">
                <span className="material-icons text-sm">push_pin</span>Pinned
              </span>
            )}
          </div>
          <span className="text-slate-400 text-[10px] font-bold whitespace-nowrap">{timeAgo(notice.postedAt)}</span>
        </div>

        {/* Title */}
        <h3 className="font-black text-slate-900 text-lg leading-tight mb-3 group-hover:text-indigo-700 transition-colors line-clamp-2">
          {notice.title}
        </h3>

        {/* Content */}
        <p className={`text-slate-500 text-sm font-medium leading-relaxed transition-all ${expanded ? '' : 'line-clamp-3'}`}>
          {notice.content}
        </p>

        {notice.content.length > 120 && (
          <button
            onClick={onToggle}
            className="mt-2 text-indigo-500 text-xs font-black hover:text-indigo-700 transition-colors flex items-center gap-1"
          >
            {expanded ? 'Show less' : 'Read more'}
            <span className="material-icons text-sm">{expanded ? 'expand_less' : 'expand_more'}</span>
          </button>
        )}

        {/* Tags */}
        {notice.tags?.length > 0 && (
          <div className="flex flex-wrap gap-1.5 mt-4">
            {notice.tags.map(tag => (
              <span key={tag} className="px-2 py-0.5 bg-slate-100 text-slate-500 text-[9px] font-black rounded-lg uppercase tracking-wider">
                #{tag}
              </span>
            ))}
          </div>
        )}

        {/* Footer */}
        <div className="mt-5 pt-4 border-t border-slate-50 flex items-center justify-between">
          <div className="flex items-center gap-2">
            <div className="w-7 h-7 rounded-xl bg-indigo-100 flex items-center justify-center">
              <span className="material-icons text-indigo-500 text-sm">person</span>
            </div>
            <div>
              <p className="text-xs font-black text-slate-700 leading-none">{notice.author || 'Administration'}</p>
              <p className="text-[9px] text-slate-400 font-bold mt-0.5">{notice.authorRole}</p>
            </div>
          </div>

          {/* Action buttons (only for non-students) */}
          {canPost && (
            <div className="flex items-center gap-1 opacity-0 group-hover:opacity-100 transition-opacity">
              <button
                onClick={() => onPin(notice.id)}
                title={notice.pinned ? 'Unpin' : 'Pin'}
                className="w-8 h-8 rounded-xl bg-amber-50 hover:bg-amber-100 flex items-center justify-center transition-all"
              >
                <span className="material-icons text-amber-500 text-sm">{notice.pinned ? 'push_pin' : 'push_pin'}</span>
              </button>
              <button
                onClick={() => onDelete(notice.id)}
                title="Delete"
                className="w-8 h-8 rounded-xl bg-rose-50 hover:bg-rose-100 flex items-center justify-center transition-all"
              >
                <span className="material-icons text-rose-500 text-sm">delete</span>
              </button>
            </div>
          )}
        </div>
      </div>
    </div>
  );
};

export default SharedNoticeBoard;
