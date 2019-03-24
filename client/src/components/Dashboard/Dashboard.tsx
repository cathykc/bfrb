import * as React from 'react';
import HorizontalBarChart from '../HorizontalBarChart/HorizontalBarChart';
import ScatterPlotGraph from '../ScatterPlotGraph/ScatterPlotGraph';
import VerticalBarChart from '../VerticalBarChart/VerticalBarChart';

import './dashboard.css';

interface DashboardState {
  data: any[];
}

const LOCATION_TO_UNICODE = {
    'HOME': '&#x2660;',
    'WORK': '&#127964',
    'SCHOOL': '&#127965',
    'OTHER': '&#127969'
};

export default class Dashboard extends React.Component<{}, DashboardState> {
  constructor(props: any) {
    super(props);
    this.state = {
      data: [],
    };
  }

  componentDidMount() {
    // const clientId = 'example_id'; // hardcode this to fetch dummy data for now!
    // fetch(`/api/fetch_data?client_id=${clientId}`, {
    //   method: 'GET',
    // }).then(fetchResponse => {
    //   if (fetchResponse.status !== 200) {
    //     // TO DO: handle group fetch error
    //     throw new Error('Fetch not successful.');
    //   }
    //   return fetchResponse.json();
    // }).then(responseBody => {
    //   this.setState({ data: responseBody.data });
    // });
  }
    
  filterLocationData(data: any[]) {
    let locationList = [];
    let locationMap = {};
  
    data.filter(item => (
        item.key === 'context'
    )).forEach((item) => {
        if (locationMap[item.answer]) {
            locationMap[item.answer]++;
        } else {
            locationMap[item.answer] = 1;
        }
    });
  
    for (let key of Object.keys(locationMap)) {
        
        locationList.push({
            x: LOCATION_TO_UNICODE[key] || 'U+1F3E0',
            y: locationMap[key]
        });
    }
  
    return locationList;
  }

  public render(): JSX.Element {
    let locationData = this.filterLocationData(this.state.data);
    
    return(
      <div className="dashboard">
        <HorizontalBarChart 
            chartTitle={'We noticed that you spend the most time pulling at: '}
            emphasisText={'Home 🏠'}
            data={locationData}
        />
        <ScatterPlotGraph 
            data={locationData}
            chartTitle={'You tend to pull on: '}
            emphasisText={'Wednesday nights'}
        />
        <VerticalBarChart 
            chartTitle={'You tend to pull your: '}
            data={locationData}
            emphasisText={'Brows and Scalp'}
        />
      </div>
    );
  }
}
