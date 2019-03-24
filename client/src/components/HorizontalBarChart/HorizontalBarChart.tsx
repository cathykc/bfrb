import * as React from 'react';
import { XYPlot, HorizontalBarSeries, XAxis, YAxis } from 'react-vis';
import './HorizontalBarChart.css';

interface Props {
    data: any[];
    chartTitle: string;
    emphasisText: string;
}

interface HorizontalBarChartState {
    data: any[];
}

const LOCATION = ['?', '🏠', '🖥', '🏫'];

const series1 = [
    {
        x: 20,
        y: '🏠',
        color: 'rgb(17, 109, 114)',
        opacity: 1
    },
    {
        x: 10,
        y: '🏫',
        color: 6,
        opacity: 0.7
    },
    {
        x: 14,
        y: '🖥',
        color: 8,
        opacity: 0.85
    },
    {
        x: 6,
        y: '?',
        color: 2,
        opacity: 0.6
    }
];

// function getRandomData() {
//     return new Array(4).fill(0).map(row => {
//         let day = Math.floor(Math.random() * (4));
//         return {
//             x: Math.floor((Math.random() * 24) / 2) * 2,
//             y: LOCATION[day],
//             color: Math.random() * 10,
//             opacity: Math.random() * 0.5 + 0.5
//         };
//     });
// }

export default class HorizontalBarChart extends React.Component<Props, HorizontalBarChartState> {
    static defaultProps: Props = {
        data: [],
        chartTitle: '',
        emphasisText: ''
    };
    
    constructor(props: any) {
        super(props);
        this.state = {
            data: series1,
        };
    }

    public render(): JSX.Element {
        let { chartTitle, emphasisText } = this.props;
        let { data } = this.state;
        const chartWidth = 320;
        const chartHeight = 250;
        return(
            <div className="horizontalBarChart">
                <span className="chartHeader">{chartTitle}
                    <strong>{emphasisText}</strong>
                </span>
                <XYPlot
                    yType="ordinal"
                    yDomain={LOCATION}
                    width={chartWidth}
                    height={chartHeight}
                    style={{
                        'font-weight': 'bold',
                        'font-family': 'sans-serif',
                        'font-size': '11px'
                    }}
                >
                    <XAxis />
                    <YAxis />
                    <HorizontalBarSeries
                        color="#59E4EC"
                        data={data}
                    />
                </XYPlot>
            </div>
        );
    }
}
