import React from 'react';

const Button: React.FC<{
    children: React.ReactNode;
    onClick?: () => void;
    type?: 'button' | 'submit' | 'reset';
    className?: string;
    variant?: 'primary' | 'secondary' | 'danger';
}> = ({ children, onClick, type = 'button', className, variant = 'primary' }) => {
    const baseClasses = "px-6 py-2.5 rounded-lg font-semibold transition-all duration-200 active:scale-95 shadow-sm";
    const variantClasses = {
        primary: "bg-indigo-600 hover:bg-indigo-700 text-white shadow-indigo-100",
        secondary: "bg-gray-100 hover:bg-gray-200 text-gray-700 shadow-gray-100",
        danger: "bg-rose-500 hover:bg-rose-600 text-white shadow-rose-100"
    };

    return (
        <button
            type={type}
            onClick={onClick}
            className={`${baseClasses} ${variantClasses[variant]} ${className}`}
        >
            {children}
        </button>
    );
};

export default Button;
