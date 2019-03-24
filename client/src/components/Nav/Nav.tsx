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
          <Menu.Item
            as={Link}
            name="home"
            active={activeItem === 'home'}
            onClick={this.handleItemClick}
            to="/"
          />
          <Menu.Item
            as={Link}
            name="dashboard"
            active={activeItem === 'dashboard'}
            onClick={this.handleItemClick}
            to="/dashboard"
          />
          <Menu.Item
            as={Link}
            name="config"
            active={activeItem === 'config'}
            onClick={this.handleItemClick}
            to="/config"
          >
            Configure CBTs
          </Menu.Item>
        </Menu>
      </div>
    );
  }
}
