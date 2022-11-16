import React from 'react';
import { BrowserRouter as Router, Switch, Route } from "react-router-dom";
import Header from './components/Header';
import './index.css';
import Home from './pages/Home';

function App() {
  return (
    <Router>
      <Home />
    </Router>
  );
}

export default App;
