import * as React from 'react';
import {
    XYPlot,
    XAxis,
    YAxis,
    VerticalGridLines,
    HorizontalGridLines,
    MarkSeries
} from 'react-vis';
import './ScatterPlotGraph.css';

interface Props {
    data: any[];
    chartTitle: string;
    emphasisText: string;
}

interface ScatterPlotGraphState {
    data: any[];
    drawMode: number;
    colorType: string;
    value: boolean;
}

const colorRanges = {
    typeA: ['#59E4EC', '#0D676C'],
    typeB: ['#EFC1E3', '#B52F93']
};

const dayRange = [
    'Sun', 'Mon', 'Tues', 'Wed', 'Thur', 'Fri', 'Sat'
];

const timeRange = [
    2, 4, 6, 8, 10, 12 , 14, 16, 18, 20, 22, 24
];

let randomData = [];
function getRandomData(day: number, hour: number, frequency: number) {
    randomData.push({
        x: hour,
        y: dayRange[day],
        label: dayRange[day],
        size: Math.random() * 10,
        color: Math.random() * 10,
        opacity: Math.random() * 0.5 + 0.5
    });
}

for (let hour of timeRange) {
    getRandomData(0, hour, 20);
    getRandomData(1, hour, 10);
    getRandomData(2, hour, 20);
    getRandomData(3, hour, 20);
    getRandomData(4, hour, 20);
    getRandomData(5, hour, 20);
    getRandomData(6, hour, 20);
}

export default class ScatterPlotGraph extends React.Component<Props, ScatterPlotGraphState> {
    static defaultProps: Props = {
        data: [],
        chartTitle: '',
        emphasisText: ''
    };

    constructor(props: any) {
        super(props);
        this.state = {
            data: randomData,
            drawMode: 0,
            colorType: 'typeA',
            value: false
        };
    }

    public render(): JSX.Element {
        const {data, colorType} = this.state;
        const {chartTitle, emphasisText} = this.props;
        const markSeriesProps = {
            animation: true,
            className: 'mark-series-example',
            sizeRange: [0, 15],
            seriesId: 'my-example-scatterplot',
            colorRange: colorRanges[colorType],
            opacityType: 'literal',
            data
        };
        const chartWidth = 320;
        const chartHeight = 300;

        return (
            <div className="scatterPlot">
                <span className="chartHeader">{chartTitle}
                    <strong>
                        {emphasisText}
                    </strong>
                </span>
                <div>
                    <XYPlot
                        xType="ordinal"
                        xDomain={timeRange}
                        yType="ordinal"
                        yDomain={dayRange}
                        onMouseLeave={() => this.setState({value: false})}
                        width={chartWidth}
                        height={chartHeight}
                        style={{
                            'font-weight': 'bold',
                            'font-family': 'sans-serif',
                            'font-size': '11px'
                        }}
                    >
                        <VerticalGridLines/>
                        <HorizontalGridLines/>
                        <XAxis/>
                        <YAxis
                            style={{
                                'margin-right': '10px'
                            }}
                        />
                        <MarkSeries {...markSeriesProps} />
                    </XYPlot>
                </div>
            </div>
        );
    }
}
