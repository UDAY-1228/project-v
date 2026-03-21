import React, { useState, useEffect, useRef } from 'react';

const stats = [
  { label: 'Institutions Served', value: 200, suffix: '+', icon: 'business' },
  { label: 'Active Students', value: 50000, suffix: '+', icon: 'school' },
  { label: 'Faculty Members', value: 5000, suffix: '+', icon: 'people' },
  { label: 'Modules Available', value: 18, suffix: '', icon: 'apps' },
];

const institutionTypes = [
  {
    icon: 'account_balance',
    title: 'Universities',
    desc: 'Full-scale university management with multi-department support, research modules, and academic governance tools.',
    color: 'from-indigo-500 to-violet-600',
    shadow: 'shadow-indigo-200',
  },
  {
    icon: 'school',
    title: 'Colleges',
    desc: 'Comprehensive college portals for UG/PG programmes, examinations, faculty coordination, and fee management.',
    color: 'from-sky-500 to-cyan-500',
    shadow: 'shadow-sky-200',
  },
  {
    icon: 'local_library',
    title: 'Schools',
    desc: 'End-to-end school management covering admissions, timetables, student progress tracking, and parent portals.',
    color: 'from-emerald-500 to-teal-500',
    shadow: 'shadow-emerald-200',
  },
  {
    icon: 'workspace_premium',
    title: 'Coaching Institutes',
    desc: 'Tailored tools for coaching centres — batch management, performance analytics, and student communication.',
    color: 'from-rose-500 to-pink-500',
    shadow: 'shadow-rose-200',
  },
];

const features = [
  { icon: 'security', title: 'Role-Based Access', desc: 'Fine-grained permissions for every staff role across all modules.' },
  { icon: 'dashboard_customize', title: 'Modular Workspaces', desc: 'Plug-and-play modules — enable only what your institution needs.' },
  { icon: 'bar_chart', title: 'Real-Time Analytics', desc: 'Live dashboards with attendance, finance, and performance data.' },
  { icon: 'notifications_active', title: 'Smart Notices', desc: 'Automated announcements, notice boards and communication tools.' },
  { icon: 'payments', title: 'Fee Management', desc: 'Complete fee lifecycle — challans, concessions, payments, and reports.' },
  { icon: 'directions_bus', title: 'Transport & Hostel', desc: 'Route planning, boarding points, hostel occupancy and gate-pass systems.' },
];

function useCountUp(target: number, duration = 1800, start = false) {
  const [count, setCount] = useState(0);
  useEffect(() => {
    if (!start) return;
    let startTime: number | null = null;
    const step = (timestamp: number) => {
      if (!startTime) startTime = timestamp;
      const progress = Math.min((timestamp - startTime) / duration, 1);
      setCount(Math.floor(progress * target));
      if (progress < 1) requestAnimationFrame(step);
    };
    requestAnimationFrame(step);
  }, [target, duration, start]);
  return count;
}

function StatCard({ stat, animate }: { stat: typeof stats[0]; animate: boolean }) {
  const count = useCountUp(stat.value, 1600, animate);
  return (
    <div className="flex flex-col items-center gap-3 p-8 rounded-3xl bg-white/10 backdrop-blur-sm border border-white/20 hover:bg-white/20 transition-all duration-300">
      <span className="material-icons text-4xl text-white/80">{stat.icon}</span>
      <div className="text-4xl font-black text-white tracking-tight">
        {animate ? count.toLocaleString() : '0'}{stat.suffix}
      </div>
      <p className="text-white/60 font-bold uppercase tracking-widest text-[10px] text-center">{stat.label}</p>
    </div>
  );
}

const Home: React.FC = () => {
  const [menuOpen, setMenuOpen] = useState(false);
  const [scrolled, setScrolled] = useState(false);
  const [statsVisible, setStatsVisible] = useState(false);
  const statsRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    const handleScroll = () => setScrolled(window.scrollY > 40);
    window.addEventListener('scroll', handleScroll);
    return () => window.removeEventListener('scroll', handleScroll);
  }, []);

  useEffect(() => {
    const observer = new IntersectionObserver(
      ([entry]) => { if (entry.isIntersecting) setStatsVisible(true); },
      { threshold: 0.3 }
    );
    if (statsRef.current) observer.observe(statsRef.current);
    return () => observer.disconnect();
  }, []);

  return (
    <div className="font-outfit bg-slate-50 text-slate-800 overflow-x-hidden">
      {/* ─── NAVBAR ─────────────────────────────────────── */}
      <header className={`fixed top-0 left-0 right-0 z-50 transition-all duration-300 ${scrolled ? 'bg-white/90 backdrop-blur-xl shadow-lg shadow-slate-200/60 border-b border-slate-100' : 'bg-transparent'}`}>
        <div className="max-w-7xl mx-auto px-6 lg:px-10 h-20 flex items-center justify-between">
          {/* Logo */}
          <a href="/" className="flex items-center gap-3 group">
            <div className="w-10 h-10 bg-gradient-to-br from-indigo-600 to-violet-700 rounded-2xl shadow-lg shadow-indigo-300 flex items-center justify-center transition-transform group-hover:scale-110">
              <span className="text-white font-black text-xl">V</span>
            </div>
            <div>
              <span className={`font-black text-lg tracking-tight transition-colors ${scrolled ? 'text-slate-900' : 'text-white'}`}>VID PLATFORM</span>
              <div className={`text-[9px] font-bold uppercase tracking-widest transition-colors ${scrolled ? 'text-slate-400' : 'text-white/50'}`}>Management System</div>
            </div>
          </a>

          {/* Desktop Nav */}
          <nav className="hidden md:flex items-center gap-8">
            {['Home', 'About', 'Features', 'Institutions'].map((item) => (
              <a
                key={item}
                href={`#${item.toLowerCase()}`}
                className={`font-bold text-sm tracking-wide transition-colors hover:text-indigo-500 ${scrolled ? 'text-slate-600' : 'text-white/80'}`}
              >
                {item}
              </a>
            ))}
            <a
              href="/login"
              id="nav-login-btn"
              className="ml-4 px-6 py-3 bg-gradient-to-r from-indigo-600 to-violet-600 text-white font-black text-sm rounded-2xl shadow-lg shadow-indigo-300 hover:shadow-indigo-400 hover:scale-105 transition-all"
            >
              Login →
            </a>
          </nav>

          {/* Mobile Menu Toggle */}
          <button
            className={`md:hidden transition-colors ${scrolled ? 'text-slate-700' : 'text-white'}`}
            onClick={() => setMenuOpen(!menuOpen)}
            aria-label="Toggle menu"
          >
            <span className="material-icons text-3xl">{menuOpen ? 'close' : 'menu'}</span>
          </button>
        </div>

        {/* Mobile Menu */}
        {menuOpen && (
          <div className="md:hidden bg-white/95 backdrop-blur-xl border-t border-slate-100 px-6 py-6 flex flex-col gap-4 shadow-xl">
            {['Home', 'About', 'Features', 'Institutions'].map((item) => (
              <a key={item} href={`#${item.toLowerCase()}`} onClick={() => setMenuOpen(false)} className="font-bold text-slate-700 hover:text-indigo-600 py-2 text-lg">
                {item}
              </a>
            ))}
            <a href="/login" className="mt-2 py-4 bg-gradient-to-r from-indigo-600 to-violet-600 text-white font-black text-center rounded-2xl shadow-lg">
              Login →
            </a>
          </div>
        )}
      </header>

      {/* ─── HERO ────────────────────────────────────────── */}
      <section id="home" className="relative min-h-screen flex items-center justify-center overflow-hidden bg-slate-900">
        {/* BG Blobs */}
        <div className="absolute inset-0 pointer-events-none">
          <div className="absolute top-1/4 left-1/4 w-[50rem] h-[50rem] bg-indigo-600/40 rounded-full blur-[120px] animate-pulse" />
          <div className="absolute bottom-1/4 right-1/4 w-[40rem] h-[40rem] bg-violet-600/40 rounded-full blur-[120px]" />
          <div className="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-[30rem] h-[30rem] bg-sky-600/20 rounded-full blur-[100px]" />
        </div>

        {/* Grid Pattern */}
        <div className="absolute inset-0 opacity-10"
          style={{ backgroundImage: 'linear-gradient(rgba(255,255,255,.08) 1px,transparent 1px),linear-gradient(90deg,rgba(255,255,255,.08) 1px,transparent 1px)', backgroundSize: '60px 60px' }}
        />

        <div className="relative z-10 max-w-6xl mx-auto px-6 lg:px-10 text-center pt-20">
          <div className="inline-flex items-center gap-2 px-5 py-2.5 rounded-full bg-white/10 border border-white/20 backdrop-blur-sm mb-10 text-white/80 text-xs font-bold uppercase tracking-widest hover:bg-white/20 transition-all cursor-default">
            <span className="material-icons text-sm text-indigo-400">verified</span>
            Next-Gen Campus Management Platform
          </div>

          <h1 className="text-5xl sm:text-6xl lg:text-8xl font-black text-white tracking-tight leading-[1.05] mb-8">
            One Platform.
            <br />
            <span className="bg-gradient-to-r from-indigo-400 via-violet-400 to-pink-400 bg-clip-text text-transparent">
              Every Institution.
            </span>
          </h1>

          <p className="text-slate-400 text-lg sm:text-xl max-w-3xl mx-auto font-medium leading-relaxed mb-12">
            VID Platform is a modular, role-based management system built for universities, colleges, schools, and coaching institutes — empowering every stakeholder with the right tools.
          </p>

          <div className="flex flex-col sm:flex-row gap-4 justify-center items-center">
            <a
              href="/login"
              id="hero-login-btn"
              className="px-10 py-5 bg-gradient-to-r from-indigo-600 to-violet-600 text-white font-black text-base rounded-2xl shadow-2xl shadow-indigo-500/30 hover:scale-105 hover:shadow-indigo-500/50 transition-all"
            >
              Get Started →
            </a>
            <a
              href="#about"
              className="px-10 py-5 bg-white/10 backdrop-blur-sm border border-white/20 text-white font-black text-base rounded-2xl hover:bg-white/20 transition-all"
            >
              Learn More
            </a>
          </div>

          {/* Floating scroll indicator */}
          <div className="mt-20 flex flex-col items-center gap-2 text-white/30 animate-bounce">
            <span className="text-xs font-bold uppercase tracking-widest">Scroll Down</span>
            <span className="material-icons">expand_more</span>
          </div>
        </div>
      </section>

      {/* ─── STATS ───────────────────────────────────────── */}
      <section ref={statsRef} className="bg-gradient-to-br from-indigo-700 via-violet-700 to-purple-800 py-20 px-6">
        <div className="max-w-6xl mx-auto grid grid-cols-2 lg:grid-cols-4 gap-6">
          {stats.map((stat) => (
            <StatCard key={stat.label} stat={stat} animate={statsVisible} />
          ))}
        </div>
      </section>

      {/* ─── ABOUT ───────────────────────────────────────── */}
      <section id="about" className="py-28 px-6 bg-white">
        <div className="max-w-7xl mx-auto grid lg:grid-cols-2 gap-20 items-center">
          {/* Text */}
          <div>
            <span className="inline-block px-4 py-1.5 bg-indigo-50 text-indigo-600 font-black text-xs uppercase tracking-widest rounded-full mb-6 border border-indigo-100">About VID</span>
            <h2 className="text-4xl lg:text-5xl font-black text-slate-900 tracking-tight leading-tight mb-8">
              Built for the Future of <span className="text-indigo-600">Education</span>
            </h2>
            <p className="text-slate-500 text-lg leading-relaxed mb-6 font-medium">
              VID Platform is a comprehensive, cloud-ready campus management solution designed to unify all institutional operations under a single roof — from admissions and academics to hostel, transport, sports, and finance.
            </p>
            <p className="text-slate-500 text-lg leading-relaxed mb-10 font-medium">
              With a modular workspace system and fine-grained role-based access control, each user sees only what's relevant to them — keeping workflows clean, secure, and efficient.
            </p>
            <div className="flex flex-wrap gap-4">
              {['Multi-Tenant', 'Cloud Ready', 'Secure', 'Scalable'].map(tag => (
                <span key={tag} className="px-4 py-2 bg-slate-100 text-slate-700 font-bold text-sm rounded-xl border border-slate-200">✓ {tag}</span>
              ))}
            </div>
          </div>

          {/* Visual card grid */}
          <div className="grid grid-cols-2 gap-5">
            {[
              { icon: 'admin_panel_settings', title: 'Super Admin', desc: 'Manages all institutions from one panel', color: 'bg-indigo-50 text-indigo-600 border-indigo-100' },
              { icon: 'manage_accounts', title: 'Inst. Admin', desc: 'Full control over users & workspaces', color: 'bg-violet-50 text-violet-600 border-violet-100' },
              { icon: 'groups', title: 'Staff & Faculty', desc: 'Role-specific tools and dashboards', color: 'bg-emerald-50 text-emerald-600 border-emerald-100' },
              { icon: 'person', title: 'Students', desc: 'Attendance, fees, LMS and more', color: 'bg-sky-50 text-sky-600 border-sky-100' },
            ].map(item => (
              <div key={item.title} className={`p-7 rounded-3xl border-2 ${item.color} hover:scale-[1.02] transition-transform`}>
                <span className="material-icons text-3xl mb-4 block">{item.icon}</span>
                <h4 className="font-black text-slate-900 mb-2">{item.title}</h4>
                <p className="text-slate-500 text-sm font-medium leading-relaxed">{item.desc}</p>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* ─── INSTITUTIONS ────────────────────────────────── */}
      <section id="institutions" className="py-28 px-6 bg-slate-50">
        <div className="max-w-7xl mx-auto">
          <div className="text-center mb-20">
            <span className="inline-block px-4 py-1.5 bg-violet-50 text-violet-600 font-black text-xs uppercase tracking-widest rounded-full mb-6 border border-violet-100">Institutions</span>
            <h2 className="text-4xl lg:text-5xl font-black text-slate-900 tracking-tight mb-6">Serving Every Type of Institution</h2>
            <p className="text-slate-500 text-lg max-w-2xl mx-auto font-medium leading-relaxed">
              Whether you run a large university or a small coaching centre, VID adapts to your workflow.
            </p>
          </div>

          <div className="grid sm:grid-cols-2 lg:grid-cols-4 gap-8">
            {institutionTypes.map((inst) => (
              <div key={inst.title} className={`group relative overflow-hidden p-8 rounded-[2.5rem] bg-white border border-slate-100 shadow-xl hover:shadow-2xl ${inst.shadow}/30 hover:-translate-y-2 transition-all duration-300`}>
                <div className={`w-16 h-16 rounded-2xl bg-gradient-to-br ${inst.color} flex items-center justify-center mb-6 shadow-lg group-hover:scale-110 transition-transform`}>
                  <span className="material-icons text-white text-3xl">{inst.icon}</span>
                </div>
                <h3 className="font-black text-slate-900 text-xl mb-3">{inst.title}</h3>
                <p className="text-slate-500 text-sm font-medium leading-relaxed">{inst.desc}</p>
                <div className={`absolute bottom-0 left-0 right-0 h-1 bg-gradient-to-r ${inst.color} opacity-0 group-hover:opacity-100 transition-opacity`} />
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* ─── FEATURES ────────────────────────────────────── */}
      <section id="features" className="py-28 px-6 bg-white">
        <div className="max-w-7xl mx-auto">
          <div className="text-center mb-20">
            <span className="inline-block px-4 py-1.5 bg-emerald-50 text-emerald-600 font-black text-xs uppercase tracking-widest rounded-full mb-6 border border-emerald-100">Features</span>
            <h2 className="text-4xl lg:text-5xl font-black text-slate-900 tracking-tight mb-6">Everything Your Institution Needs</h2>
            <p className="text-slate-500 text-lg max-w-2xl mx-auto font-medium leading-relaxed">
              Powerful modules designed to handle real-world institutional complexity with ease.
            </p>
          </div>

          <div className="grid sm:grid-cols-2 lg:grid-cols-3 gap-8">
            {features.map((f) => (
              <div key={f.title} className="group p-8 rounded-3xl border-2 border-slate-100 hover:border-indigo-200 bg-white hover:bg-indigo-50/30 transition-all duration-300 hover:-translate-y-1">
                <div className="w-14 h-14 rounded-2xl bg-indigo-100 group-hover:bg-indigo-600 flex items-center justify-center mb-6 transition-colors">
                  <span className="material-icons text-indigo-600 group-hover:text-white transition-colors text-2xl">{f.icon}</span>
                </div>
                <h3 className="font-black text-slate-900 text-lg mb-2">{f.title}</h3>
                <p className="text-slate-500 text-sm font-medium leading-relaxed">{f.desc}</p>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* ─── CTA BANNER ──────────────────────────────────── */}
      <section className="py-28 px-6 bg-gradient-to-br from-slate-900 via-indigo-950 to-violet-950 relative overflow-hidden">
        <div className="absolute inset-0 pointer-events-none">
          <div className="absolute top-0 right-0 w-[30rem] h-[30rem] bg-violet-600/20 rounded-full blur-[100px]" />
          <div className="absolute bottom-0 left-0 w-[30rem] h-[30rem] bg-indigo-600/20 rounded-full blur-[100px]" />
        </div>
        <div className="relative z-10 max-w-3xl mx-auto text-center">
          <h2 className="text-4xl lg:text-6xl font-black text-white tracking-tight mb-6 leading-tight">
            Ready to Transform Your Institution?
          </h2>
          <p className="text-slate-400 text-lg font-medium mb-12 leading-relaxed">
            Join hundreds of institutions already using VID Platform to streamline operations and deliver exceptional educational experiences.
          </p>
          <a
            href="/login"
            id="cta-login-btn"
            className="inline-flex items-center gap-3 px-12 py-6 bg-gradient-to-r from-indigo-500 to-violet-600 text-white font-black text-lg rounded-2xl shadow-2xl shadow-indigo-500/30 hover:scale-105 transition-all"
          >
            <span className="material-icons">login</span>
            Access Your Portal
          </a>
        </div>
      </section>

      {/* ─── FOOTER ──────────────────────────────────────── */}
      <footer className="bg-slate-950 text-slate-400 py-16 px-6">
        <div className="max-w-7xl mx-auto">
          <div className="grid sm:grid-cols-2 lg:grid-cols-4 gap-12 mb-16">
            {/* Brand */}
            <div className="lg:col-span-1">
              <div className="flex items-center gap-3 mb-5">
                <div className="w-10 h-10 bg-gradient-to-br from-indigo-600 to-violet-700 rounded-2xl flex items-center justify-center">
                  <span className="text-white font-black text-xl">V</span>
                </div>
                <span className="text-white font-black text-lg tracking-tight">VID PLATFORM</span>
              </div>
              <p className="text-sm leading-relaxed text-slate-500 font-medium">
                Modular campus management for the modern institution. Scalable, secure, and simple.
              </p>
            </div>

            {/* Links */}
            <div>
              <h5 className="text-white font-black mb-5 text-sm uppercase tracking-widest">Platform</h5>
              <ul className="space-y-3 text-sm font-medium">
                {['Features', 'Institutions', 'Security', 'Pricing'].map(l => (
                  <li key={l}><a href="#" className="hover:text-indigo-400 transition-colors">{l}</a></li>
                ))}
              </ul>
            </div>
            <div>
              <h5 className="text-white font-black mb-5 text-sm uppercase tracking-widest">Modules</h5>
              <ul className="space-y-3 text-sm font-medium">
                {['Academics', 'Finance', 'Hostel', 'Transport'].map(l => (
                  <li key={l}><a href="#" className="hover:text-indigo-400 transition-colors">{l}</a></li>
                ))}
              </ul>
            </div>
            <div>
              <h5 className="text-white font-black mb-5 text-sm uppercase tracking-widest">Company</h5>
              <ul className="space-y-3 text-sm font-medium">
                {['About Us', 'Contact', 'Privacy Policy', 'Terms of Service'].map(l => (
                  <li key={l}><a href="#" className="hover:text-indigo-400 transition-colors">{l}</a></li>
                ))}
              </ul>
            </div>
          </div>

          <div className="border-t border-slate-800 pt-8 flex flex-col sm:flex-row items-center justify-between gap-4 text-sm font-medium text-slate-600">
            <p>© 2026 VID Platform. All rights reserved.</p>
            <div className="flex items-center gap-2">
              <span className="w-2 h-2 rounded-full bg-emerald-500 animate-pulse" />
              <span className="text-emerald-400">All systems operational</span>
            </div>
          </div>
        </div>
      </footer>
    </div>
  );
};

export default Home;
