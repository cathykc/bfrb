import * as React from 'react';
import { Link } from 'react-router-dom';

import { Menu } from 'semantic-ui-react';

import './Nav.css';

interface NavState {
  activeItem: 'home' | 'dashboard' | 'config';
}

export default class Nav extends React.Component<{}, NavState> {
  constructor(props: any) {
    super(props);
    this.state = {
      activeItem: 'home',
    };
  }

  handleItemClick = (e, { name }) => this.setState({ activeItem: name });

  public render(): JSX.Element {
    const { activeItem } = this.state;

    return (
      <div className="nav-menu">
        <Menu secondary={true}>
          <Link to="/">
            <Menu.Item
              name="home"
              active={activeItem === 'home'}
              onClick={this.handleItemClick}
            />
          </Link>
          <Link to="/dashboard">
            <Menu.Item
              name="dashboard"
              active={activeItem === 'dashboard'}
              onClick={this.handleItemClick}
            />
          </Link>
          <Link to="/config">
            <Menu.Item
              name="config"
              active={activeItem === 'config'}
              onClick={this.handleItemClick}
            >
              Configure CBTs
            </Menu.Item>
          </Link>
        </Menu>
      </div>
    );
  }
}
