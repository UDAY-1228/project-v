import React, { Suspense, lazy } from 'react';
import { BrowserRouter as Router, Routes, Route, Navigate } from 'react-router-dom';
import { AuthProvider, useAuth } from './core/services/AuthContext';
import DashboardShell from './core/layouts/DashboardShell';
import Login from './core/login/Login';
import Homepage from './core/homepage/Homepage';

const ProtectedRoute: React.FC<{ children: React.ReactNode }> = ({ children }) => {
  const { user, loading } = useAuth();
  if (loading) return <div className="h-screen w-screen flex items-center justify-center font-bold text-gray-400">LOADING VID...</div>;
  if (!user) return <Navigate to="/login" replace />;
  return <>{children}</>;
};

// Application entry point

const App: React.FC = () => {
  return (
    <Router>
      <AuthProvider>
        <Routes>
          <Route path="/login" element={<Login />} />
          <Route 
            path="/" 
            element={
              <ProtectedRoute>
                <DashboardShell />
              </ProtectedRoute>
            }
          >
            <Route path="dashboard" element={<Homepage />} />
            <Route path="super-admin/institutions" element={<div>Institutions Component</div>} />
            <Route path="admin/users" element={<div>Users Component</div>} />
            

            <Route index element={<Navigate to="/dashboard" replace />} />
          </Route>
        </Routes>
      </AuthProvider>
    </Router>
  );
};

export default App;
