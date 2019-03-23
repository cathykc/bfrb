import * as React from 'react';

interface DashboardState {
  data: any[];
}

export default class Dashboard extends React.Component<{}, DashboardState> {
  constructor(props: any) {
    super(props);
    this.state = {
      data: [],
    };
  }

  componentDidMount() {
    const clientId = 'example_id'; // hardcode this to fetch dummy data for now!
    fetch(`/api/fetch_data?client_id=${clientId}`, {
      method: 'GET',
    }).then(fetchResponse => {
      if (fetchResponse.status !== 200) {
        // TO DO: handle group fetch error
        throw new Error('Fetch not successful.');
      }
      return fetchResponse.json();
    }).then(responseBody => {
      this.setState({ data: responseBody });
    });
  }

  public render(): JSX.Element {
    return(
      <div>
        <p>This is page for viewing aggregated client data.</p>
        <div>
          <p>Returned data</p>
          <pre>{JSON.stringify(this.state.data)}</pre>
        </div>
      </div>
    );
  }
}
