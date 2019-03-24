import * as React from 'react';

import { Button } from 'semantic-ui-react';

import ConfigEditor from './ConfigEditor';

import './ConfigDashboard.css';

interface ConfigProps {
  config: any;
  saveConfig: any;
  deleteConfig: any;
}

export default class Config extends React.Component<ConfigProps> {
  handleAbtChange = abtConfig => {
    const { config, saveConfig } = this.props;
    config.config.abt_config = abtConfig;
    saveConfig(config);
  }

  handleDelete = () => {
    this.props.deleteConfig(this.props.config.id);
  }

  public render(): JSX.Element {
    // I'm sorry mom
    if (!this.props.config || !this.props.config.config) {
      return <div />;
    }
    return (
      <div style={{ padding: 20 }}>
        <Button
          className="delete-btn"
          negative={true}
          onClick={this.handleDelete}
        >
          Delete
        </Button>
        <ConfigEditor
          initialConfig={this.props.config.config.abt_config}
          onChange={this.handleAbtChange}
        />
      </div>
    );
  }
}
