import React from 'react';
import { BrowserRouter as Router, Switch, Route, Routes } from "react-router-dom";
import Header from './components/Header';
import SearcHPage from './components/SearcHPage';
import { UserProvider } from './context/FormContext';
import './index.css';
import Home from './pages/Home';
import ProductPage from './pages/ProductPage';

function App() {
  return (
    <UserProvider>
      <Router>
        <Routes>
          <Route path='/' element={<Home />} />
          <Route path="/category/:category" element={<ProductPage />} />
          <Route path="/search/:query" element={<SearcHPage />} />
        </Routes>
      </Router>
    </UserProvider>
  );
}

export default App;
