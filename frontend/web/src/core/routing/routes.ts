/**
 * Centralized Route Definitions
 * Define your routes here to avoid hardcoded strings across the application.
 */

export const ROUTES = {
  HOME: '/',
  AUTH: {
    LOGIN: '/login',
    REGISTER: '/register',
    FORGOT_PASSWORD: '/forgot-password',
  },
  WORKSPACES: {
    STUDENT: '/student',
    ACADEMIC_ADMIN: '/academic-admin',
    EXAMINATION: '/examination',
    FACULTY: '/faculty',
  },
  NOT_FOUND: '*',
} as const;
