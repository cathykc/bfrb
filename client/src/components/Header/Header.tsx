import * as React from 'react';
import './Header.css';

export default class Header extends React.Component  {
    public render(): JSX.Element {
        return (
            <div className="App-header">
                <div className="logo_container">
                    <img className="logo" src={require('./logo.png')} alt="logo" />
                </div>
            </div>
        );
    }
}
