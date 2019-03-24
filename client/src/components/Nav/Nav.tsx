import * as React from 'react';
import { Link } from 'react-router-dom';

import { Menu } from 'semantic-ui-react';

import './Nav.css';

interface NavState {
  activeItem: 'Awareness' | 'Control' | 'Config';
}

export default class Nav extends React.Component<{}, NavState> {
  constructor(props: any) {
    super(props);
    this.state = {
      activeItem: 'Awareness',
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
            name="Awareness"
            active={activeItem === 'Awareness'}
            onClick={this.handleItemClick}
            to="/"
          />
          <Menu.Item
            as={Link}
            name="control"
            active={activeItem === 'Control'}
            onClick={this.handleItemClick}
            to="/control"
          />
          <Menu.Item
            as={Link}
            name="config"
            active={activeItem === 'Config'}
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
