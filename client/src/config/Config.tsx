import * as React from 'react';
import ConfigEditor from './ConfigEditor';

const INITIAL_CONFIG = [
  {
    prompt_key: 'site',
    prompt_text: 'Where are you picking?',
    response_type: 'choice',
    response_options: ['face', 'lip', 'hair'],
  },
  {
    prompt_key: 'another_example',
    prompt_text: 'Where are you?',
    prompt_type: 'text',
  },
];

interface ConfigProps {
  config: any;
  saveConfig: any;
}

export default class Config extends React.Component<ConfigProps> {
  handleAbtChange = abtConfig => {
    const { config, saveConfig } = this.props;
    config.config.abt_config = abtConfig;
    saveConfig(config);
  };

  public render(): JSX.Element {
    return (
      <div style={{ padding: 20 }}>
        <ConfigEditor
          initialConfig={INITIAL_CONFIG}
          onChange={newConfig => console.log(newConfig)}
        />
      </div>
    );
  }
}
