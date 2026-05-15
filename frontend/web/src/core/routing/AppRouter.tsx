import React from 'react';
import { createBrowserRouter } from 'react-router-dom';
import { ROUTES } from './routes';

// Base Layout component (could be moved to @core/layouts later)
const AppLayout = ({ children }: { children: React.ReactNode }) => (
  <div className="app-layout">
    {/* Global Header/Navigation goes here */}
    <main>{children}</main>
  </div>
);

// Placeholder components for routing demonstrations
const Home = () => <div><h1>Welcome to the Application</h1></div>;
const Login = () => <div><h1>Login</h1></div>;
const StudentWorkspace = () => <div><h1>Student Workspace</h1></div>;
const NotFound = () => <div><h1>404 - Not Found</h1></div>;

export const router = createBrowserRouter([
  {
    path: ROUTES.HOME,
    element: (
      <AppLayout>
        <Home />
      </AppLayout>
    ),
  },
  {
    path: ROUTES.AUTH.LOGIN,
    element: <Login />,
  },
  {
    path: ROUTES.WORKSPACES.STUDENT,
    element: (
      <AppLayout>
        <StudentWorkspace />
      </AppLayout>
    ),
  },
  {
    path: ROUTES.NOT_FOUND,
    element: <NotFound />,
  },
]);
