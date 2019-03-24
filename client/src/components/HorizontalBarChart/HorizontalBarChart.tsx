import * as React from 'react';
import { XYPlot, HorizontalBarSeries, XAxis, YAxis } from 'react-vis';
import './HorizontalBarChart.css';

interface Props {
    data: any[];
    chartTitle: string;
}

interface HorizontalBarChartState {
    data: any[];
}

const LOCATION = ['🏠', '🏫', '💻', '?'];

function getRandomData() {
    return new Array(50).fill(0).map(row => {
        let day = Math.floor(Math.random() * (4));
        return {
            x: Math.floor((Math.random() * 24) / 2) * 2,
            y: LOCATION[day],
            color: Math.random() * 10,
            opacity: Math.random() * 0.5 + 0.5
        };
    });
}

const randomData = getRandomData();

export default class HorizontalBarChart extends React.Component<Props, HorizontalBarChartState> {
    static defaultProps: Props = {
        data: [],
        chartTitle: ''
    };
    
    constructor(props: any) {
        super(props);
        this.state = {
            data: randomData,
        };
    }

    public render(): JSX.Element {
        let { chartTitle } = this.props;
        let { data } = this.state;
        const chartWidth = 320;
        const chartHeight = 250;
        return(
            <div className="horizontalBarChart">
                <h3 className="chartHeader">{chartTitle}</h3>
                <XYPlot
                    yType="ordinal"
                    strokeWidth={5}
                    yDomain={LOCATION}
                    width={chartWidth}
                    height={chartHeight}
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
