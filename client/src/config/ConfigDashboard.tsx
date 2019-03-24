import * as React from 'react';

import { find, map } from 'lodash';
import { Grid, Menu, Segment } from 'semantic-ui-react';

import Config from './Config';
import NewConfig from './NewConfig';

interface ConfigDashboardState {
  activeConfig: number;
  configs: any[];
}

export default class ConfigDashboard extends React.Component<{}, ConfigDashboardState> {
  constructor(props: any) {
    super(props);
    this.state = {
      activeConfig: 1,
      configs: [],
    };
  }

  componentDidMount() {
    fetch('/api/get_configs', {
      method: 'GET',
    }).then(fetchResponse => {
      if (fetchResponse.status !== 200) {
        // TO DO: handle group fetch error
        throw new Error('Fetch not successful.');
      }
      return fetchResponse.json();
    }).then(responseBody => {
      this.setState({ configs: responseBody });
    });
  }

  handleItemClick = (e, { data }) => {
    this.setState({ activeConfig: data });
  }

  handleNewItemClick = () => {
    this.setState({ activeConfig: -1 });
  }

  handleSaveConfig = (config) => {
    fetch('/api/update_config', {
      method: 'POST',
      body: JSON.stringify(config),
      headers: {
        'Content-Type': 'application/json'
      },
    }).then(fetchResponse => {
      if (fetchResponse.status !== 200) {
        // TO DO: handle config update error
        throw new Error('Config update not successful.');
      }
      return fetchResponse.json();
    }).then(responseBody => {
      console.log(responseBody);
    });
  }

  public render(): JSX.Element {
    const { activeConfig, configs } = this.state;

    return(
      <Grid>
        <Grid.Column width={3}>
          <Menu fluid={true} vertical={true} tabular={true}>
            {map(configs, config => {
              return (
                <Menu.Item
                  key={config.id}
                  data={config.id}
                  active={activeConfig === config.id}
                  onClick={this.handleItemClick}
                >
                  {config.name}
                </Menu.Item>
              );
            })}
            <Menu.Item
              active={activeConfig === -1}
              onClick={this.handleNewItemClick}
            >
              Create a new treatment
            </Menu.Item>
          </Menu>
        </Grid.Column>

        {activeConfig > -1 && <Grid.Column stretched={true} width={13}>
          <Segment>
            <Config config={find(configs, { 'id': activeConfig})} saveConfig={this.handleSaveConfig}/>
          </Segment>
        </Grid.Column>}
        {activeConfig === -1 && <Grid.Column stretched={true} width={13}>
          <Segment>
            <NewConfig createConfig={this.handleSaveConfig}/>
          </Segment>
        </Grid.Column>}
      </Grid>
    );
  }
}