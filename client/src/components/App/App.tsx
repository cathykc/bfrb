import * as React from 'react';
import { BrowserRouter as Router, Route } from 'react-router-dom';

import ConfigDashboard from '../../config/ConfigDashboard';
import Dashboard from '../dashboard/Dashboard';

import './App.css';

export default class App extends React.Component {
  public render(): JSX.Element {
    return (
      <Router>
        <div>
          <div className="content">
            <Route exact={true} path="/" component={Dashboard} />
            <Route
              path="/dashboard*"
              component={Dashboard}
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
