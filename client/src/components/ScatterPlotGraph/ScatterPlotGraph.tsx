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
    6, 8, 10, 12 , 14, 16, 18, 20, 22
];

let randomData = [];
function getRandomData(day: number, hour: number, frequency: number) {
    if (day === 3) {
        frequency = hour * frequency;
    }
    randomData.push({
        x: hour,
        y: dayRange[day],
        label: dayRange[day],
        size: Math.floor(Math.random() * frequency),
        color: Math.random() * 10,
        opacity: Math.random() * 0.5 + 0.5
    });
}

for (let hour of timeRange) {
    getRandomData(0, hour, 8);
    getRandomData(1, hour, 11);
    getRandomData(2, hour, 7);
    getRandomData(3, hour, 1);
    getRandomData(4, hour, 9);
    getRandomData(5, hour, 1);
    getRandomData(6, hour, 6);
}

randomData.push({
    x: 4,
    y: 1,
    label: dayRange[4],
    size: 0,
    color: Math.random() * 10,
    opacity: Math.random() * 0.5 + 0.5
});

randomData.push({
    x: 4,
    y: 24,
    label: dayRange[6],
    size: 0,
    color: Math.random() * 10,
    opacity: Math.random() * 0.5 + 0.5
});

function myFormatter(t: number) {
    return (
        <tspan>
            <tspan x="0" dy="1em">{`${t}:00`}</tspan>
        </tspan>
    );
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
                    <strong className="black">
                        {emphasisText}
                    </strong>
                </span>
                <div>
                    <XYPlot
                        yType="ordinal"
                        yDomain={dayRange}
                        onMouseLeave={() => this.setState({value: false})}
                        width={chartWidth}
                        height={chartHeight}
                        animation={{duration: 3}}
                        style={{
                            'font-weight': 'bold',
                            'font-family': 'sans-serif',
                            'font-size': '11px'
                        }}
                    >
                        <VerticalGridLines/>
                        <HorizontalGridLines
                            style={{
                                text: {stroke: 'none', fill: '#6b6b76', fontWeight: 600},
                            }}
                        />
                        <XAxis
                            style={{
                                line: {stroke: '#ADDDE1'},
                                ticks: {stroke: '#ADDDE1'},
                                text: {stroke: 'none', fill: '#6b6b76', fontWeight: 600},
                            }}
                            tickTotal={6}
                            tickValues={[0, 4, 8, 12, 16, 20]}
                            tickFormat={myFormatter}
                        />
                        <YAxis
                            style={{
                                'margin-right': '10px'
                            }}
                        />
                        <MarkSeries {...markSeriesProps}/>
                    </XYPlot>
                </div>
            </div>
        );
    }
}
