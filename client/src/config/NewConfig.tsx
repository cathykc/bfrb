import * as React from 'react';

interface NewConfigProps {
  createConfig: any;
}

export default class Config extends React.Component<NewConfigProps> {
  public render(): JSX.Element {

    return (
      <div style={{ padding: 20 }}>
        ITSA ME - MARIO
      </div>
    );
  }
}
