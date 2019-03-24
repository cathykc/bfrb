import * as React from 'react';
import { BrowserRouter as Router, Route } from 'react-router-dom';

import ConfigDashboard from '../../config/ConfigDashboard';
import Dashboard from '../Dashboard/Dashboard';
import Header from '../Header/Header';
import Landing from '../../Landing';

import './App.css';

export default class App extends React.Component {
  public render(): JSX.Element {
    return (
      <Router>
        <div>
          <Header/>
          <div className="content">
            <Route exact={true} path="/" component={Dashboard} />
            <Route
              path="/control"
              component={Landing}
            />
            <Route
              path="/config"
              component={ConfigDashboard}
            />
          </div>
        </div>
      </Router>
    );
  }
}
