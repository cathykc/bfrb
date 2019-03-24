import * as React from 'react';
import logo from './logo.svg';
import './Header.css';

export default class Header extends React.Component  {
    public render(): JSX.Element {
        return (
            <div className="App-header">
                <div className="App-logo">
                    <img src={logo} alt="logo" />
                </div>
            </div>
        );
    }
}
