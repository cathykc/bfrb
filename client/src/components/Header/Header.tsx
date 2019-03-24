import * as React from 'react';
import { withRouter } from 'react-router-dom';

import './Header.css';

class Header extends React.Component<any>  {
    public render(): JSX.Element {
        const { location } = this.props;
        const path = location.pathname.split('/')[1];
        return (
            <div className="App-header">
                {path === 'config' ?
                  <div className="patient_container">
                    <img className="patient" src={require('./patient.jpg')} alt="patient" />
                    <h3 className="centered">Benjamin Hsu</h3>
                  </div>
                  : <div className="logo_container">
                    <img className="logo" src={require('./logo.png')} alt="logo" />
                  </div>
                }
            </div>
        );
    }
}

export default withRouter(Header);
