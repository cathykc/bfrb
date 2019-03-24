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
}

interface ScatterPlotGraphState {
    data: any[];
    drawMode: number;
    colorType: string;
    value: boolean;
}

const dayRange = [
    'Sun', 'Mon', 'Tues', 'Wed', 'Thur', 'Fri', 'Sat'
];

function getRandomData() {
    return new Array(50).fill(0).map(row => {
        let day = Math.floor(Math.random() * (7));
        return {
            x: Math.floor((Math.random() * 24) / 2) * 2,
            y: dayRange[day],
            label: dayRange[day],
            size: Math.random() * 15,
            color: Math.random() * 10,
            opacity: Math.random() * 0.5 + 0.5
        };
    });
}
const colorRanges = {
    typeA: ['#59E4EC', '#0D676C'],
    typeB: ['#EFC1E3', '#B52F93']
};

const timeRange = [
    2, 4, 6, 8, 10, 12 , 14, 16, 18, 20, 22, 24
];

const randomData = getRandomData();

export default class ScatterPlotGraph extends React.Component<Props, ScatterPlotGraphState> {
    static defaultProps: Props = {
        data: [],
        chartTitle: ''
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
        const {chartTitle} = this.props;
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
                <h3 className="chartHeader">{chartTitle}</h3>
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
                            'font-size': '12px'
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
