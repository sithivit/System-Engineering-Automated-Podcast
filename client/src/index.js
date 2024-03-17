import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import { App, Home, Create, Login, Episodes, ViewEpisode } from './App';
import { BrowserRouter, Routes, Route } from 'react-router-dom';

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <BrowserRouter>
    <Routes>
      <Route path="/" element={<App />} />
      <Route path="/home" element={<Home />} />
      <Route path="/episodes" element={<Episodes />} />
      <Route path="/create" element={<Create />} />
      <Route path="/login" element={<Login />} />
      <Route path="/episodes/view" element={<ViewEpisode />} />
    </Routes>
  </BrowserRouter>
);
