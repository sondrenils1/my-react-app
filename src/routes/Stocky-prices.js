import React from 'react';
import Plot from 'react-plotly.js';
import "./StockPrices.css"

class StockPrice extends React.Component {

    
  constructor(props) {
    super(props);
    this.state = {
      stockChartXValues: [],
      stockChartYValues: []
    }
  }

  componentDidMount() {
    this.fetchStock();
  }

  fetchStock() {
    const pointerToThis = this;
    console.log(pointerToThis);
    const API_KEY = 'J3JJH0V6FN771XOU';
    let StockSymbol = 'IBM';
    let API_Call = `https://www.alphavantage.co/query?function=TIME_SERIES_MONTHLY&symbol=${StockSymbol}&apikey=${API_KEY}`;
    let stockChartXValuesFunction = [];
    let stockChartYValuesFunction = []; 

    fetch(API_Call)
      .then(
        function(response) {
          return response.json();
        }
      )
      .then(
        function(data) {
          console.log(data);

          for (var key in data['Monthly Time Series']) {
            stockChartXValuesFunction.push(key);
            stockChartYValuesFunction.push(data['Monthly Time Series'][key]['1. open']);
          }

          // console.log(stockChartXValuesFunction);
          pointerToThis.setState({
            stockChartXValues: stockChartXValuesFunction,
            stockChartYValues: stockChartYValuesFunction
          });
        }
      )
  }

  render() {
    return (
      <div className='StockPrice'>
        <h1>Stock Market Price (serachbar coming soon)</h1>
        <Plot className='plot'
          data={[
            {
              x: this.state.stockChartXValues,
              y: this.state.stockChartYValues,
              type: 'scatter',
              mode: 'lines+text',
              marker: {color: 'red'},
              bgcolor: "black",
            }
          ]}
          layout={{width: 720, height: 440, title: `IBM Stock Price`}}
        />
      </div>
    )
  }
}

export default StockPrice;