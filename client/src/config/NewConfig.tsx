import * as React from 'react';

import { Input } from 'semantic-ui-react';

import ConfigEditor from './ConfigEditor';

interface NewConfigProps {
  createConfig: any;
}

interface NewConfigState {
  name: string;
  config: any;
}

export default class NewConfig extends React.Component<NewConfigProps, NewConfigState> {
  constructor(props: NewConfigProps) {
    super(props);
    this.state = {
      name: null,
      config: { abt_config: [] },
    };
  }

  handleNameChange = (e, { value }) => this.setState({ name: value });

  handleAbtChange = (abtConfig) => {
    this.state.config.abt_config = abtConfig;
    if (this.state.name) {
      this.props.createConfig({ name: this.state.name, config: this.state.config, id: null });
    } else {
      alert('You need to input a name to save this config.');
    }
  }

  public render(): JSX.Element {
    return (
      <div>
        <Input label="Config name" placeholder="e.g. Trichotillomania" onChange={this.handleNameChange}/>
        <hr />
        <ConfigEditor initialConfig={this.state.config.abt_config} onChange={this.handleAbtChange}/>
      </div>
    );
  }
}
