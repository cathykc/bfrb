import * as React from 'react';
import { Link } from 'react-router-dom';

export default class Nav extends React.Component {
  public render(): JSX.Element {
    return (
      <div>
        <ul>
          <li>
            <Link to="/">Home</Link>
          </li>
          <li>
            <Link to="/dashboard">Dashboard</Link>
          </li>
          <li>
            <Link to="/config">Configuration</Link>
          </li>
        </ul>
      </div>
    );
  }
}
