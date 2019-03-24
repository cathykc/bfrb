import * as React from 'react';
import { XYPlot, VerticalBarSeries, XAxis, YAxis } from 'react-vis';
import './VerticalBarChart.css';

interface Props {
    data: any[];
    chartTitle: string;
    emphasisText: string;
}

interface VerticalBarChartState {
    data: any[];
}

const bodyLocation = ['Scalp', 'Brows', 'Lashes', 'Other'];
//
// function getRandomData() {
//     return new Array(50).fill(0).map(row => {
//         let day = Math.floor(Math.random() * (4));
//         return {
//             y: Math.floor((Math.random() * 24) / 2) * 2,
//             x: bodyLocation[day],
//             color: Math.random() * 10,
//             opacity: Math.random() * 0.5 + 0.5
//         };
//     });
// }
//
// const randomData = getRandomData();

const series1 = [
    {
        y: 20,
        x: 'Scalp',
        color: 'rgb(17, 109, 114)',
        opacity: 1
    },
    {
        y: 20,
        x: 'Lashes',
        color: 6,
        opacity: 0.7
    },
    {
        y: 20,
        x: 'Brows',
        color: 8,
        opacity: 0.85
    },
    {
        y: 20,
        x: 'Other',
        color: 2,
        opacity: 0.6
    }
];

const series2 = [
    {
        y: 20,
        x: 'Scalp',
        color: 'rgb(17, 109, 114)',
        opacity: 1
    },
    {
        y: 10,
        x: 'Lashes',
        color: 6,
        opacity: 0.7
    },
    {
        y: 14,
        x: 'Brows',
        color: 8,
        opacity: 0.85
    },
    {
        y: 6,
        x: 'Other',
        color: 2,
        opacity: 0.6
    }
];

export default class VerticalBarChart extends React.Component<Props, VerticalBarChartState> {
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

    componentDidMount() {
        setTimeout(() => {
                this.setState({ data: series2 });
            },
                   500);
    }

    public render(): JSX.Element {  
        let { chartTitle, emphasisText } = this.props;
        let { data } = this.state;
        const chartWidth = 320;
        const chartHeight = 250;
        return(
            <div className="verticalBarChart">
                <span className="verticalBarChart_header">{chartTitle}
                    <strong className="black">
                        {emphasisText}
                    </strong>
                </span>
                <XYPlot
                    xType="ordinal"
                    strokeWidth={5}
                    xDomain={bodyLocation}
                    width={chartWidth}
                    height={chartHeight}
                    animation={true}
                    style={{
                        'font-size': '12px',
                        'font-weight': '600',
                        'color': '#12939A',
                    }}
                >
                    <XAxis
                        style={{
                            line: {stroke: '#ADDDE1'},
                            ticks: {stroke: '#ADDDE1'},
                            text: {stroke: 'none', fill: '#6b6b76', fontSize: 13, fontWeight: 600},
                        }}
                    />
                    <YAxis
                        tickTotal={3}
                        tickValues={[0, 10, 20]}
                        style={{
                            line: {stroke: '#ADDDE1'},
                            ticks: {stroke: '#ADDDE1'},
                            text: {stroke: 'none', fill: '#6b6b76', fontWeight: 600},
                        }}
                    />
                    <VerticalBarSeries
                        color="#59E4EC"
                        data={data}
                    />
                </XYPlot>
            </div>
        );
    }
}
