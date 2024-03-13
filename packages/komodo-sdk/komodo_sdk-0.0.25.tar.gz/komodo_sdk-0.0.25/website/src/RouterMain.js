import React from 'react';
import { HashRouter as Router, Routes, Route, Navigate, Outlet } from 'react-router-dom';
import "./App.css";
import Login from "./auth/Login"
import Chat from "./components/chat/Chat"
import Details from "./components/chat/Details";
import ChatBot from './pages/chatBot';
import Profile from './pages/profile/Profile';
import Settings from './pages/settings/Settings';

function Authorization() {
    const user = JSON.parse(localStorage.getItem('komodoUser'))
    return user?.email !== null && user?.email !== undefined && user?.email !== "" ? <Outlet /> : <Navigate to={"/login"} />
}

function App() {
    return (
        <Router>
            <Routes>
                <Route path="/" strict >
                    <Route index element={<Login />} />
                    <Route path="/login" strict element={<Login />} />
                </Route>
                <Route element={<Authorization />}>
                    <Route path="/chat" element={<Chat />} />

                    <Route path="/chatbot" element={<ChatBot />} />
                    <Route path="/details/:id" element={<Details />} />
                    <Route path="/profile" element={<Profile />} />
                    <Route path="/settings" element={<Settings />} />

                </Route>
            </Routes>
        </Router>
    );
}

export default App;
