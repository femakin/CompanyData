import React from 'react';
import { BrowserRouter as Router, Switch, Route, Routes } from "react-router-dom";
import Header from './components/Header';
import './index.css';
import Home from './pages/Home';
import ProductPage from './pages/ProductPage';

function App() {
  return (
    <Router>
      <Routes>
        <Route path='/' element={<Home />} />
        <Route path="/category/:category" element={<ProductPage />} />
      </Routes>
    </Router>
  );
}

export default App;
