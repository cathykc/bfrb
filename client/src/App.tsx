import * as React from 'react';
import { BrowserRouter as Router, Route } from 'react-router-dom';

import Config from './config/Config';
import Dashboard from './dashboard/Dashboard';
import Landing from './Landing';
import Nav from './Nav';

import './App.css';

export default class App extends React.Component {
  public render(): JSX.Element {
    return (
      <Router>
        <div>
          <Nav />
          <div className="content">
            <Route exact={true} path="/" component={Landing} />
            <Route
              path="/dashboard*"
              component={Dashboard}
            />
            <Route
              path="/config"
              component={Config}
            />
          </div>
        </div>
      </Router>
    );
  }
}
