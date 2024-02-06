import dash
from dash import dcc, html, Input, Output
import plotly.graph_objs as go
import pandas as pd
import numpy as np

from performance_metrics import TradingAnalysis
from Risk_Analysis import RiskAnalysis
from performance_attribution import PerformanceAttribution



file_path = 'trading_data.csv'  # Path to your CSV file

# Instantiate classes
trading_analysis = TradingAnalysis(file_path)
risk_analysis = RiskAnalysis(file_path)
performance_attribution = PerformanceAttribution(file_path)

# Initialize the Dash app
app = dash.Dash(__name__)

# Define the layout of the app
app.layout = html.Div(children=[
    html.H1(children='Trading Portfolio Dashboard'),
    
    # Trading Analysis Metrics
    html.Div(children=[
        html.H2(children='Trading Analysis'),
        dcc.Graph(
            id='cumulative-return-graph',
            figure={
                'data': [
                    go.Scatter(
                        x=trading_analysis.data['Date'],
                        y=trading_analysis.data['cumulative_return'],
                        mode='lines',
                        name='Cumulative Return'
                    )
                ],
                'layout': go.Layout(
                    title='Cumulative Return Over Time',
                    xaxis={'title': 'Date'},
                    yaxis={'title': 'Cumulative Return'},
                    margin={'l': 40, 'b': 40, 't': 40, 'r': 10},
                    legend={'x': 0, 'y': 1},
                    hovermode='closest'
                )
            }
        ),
    
        # Annualized Return Graph
        dcc.Graph(
            id='annualized-return-graph',
            figure={
                'data': [
                    go.Scatter(
                        x=trading_analysis.data['Date'],
                        y=trading_analysis.data['annualized_return'],
                        mode='lines',
                        name='Annualized Return'
                    )
                ],
                'layout': go.Layout(
                    title='Annualized Return Over Time',
                    xaxis={'title': 'Date'},
                    yaxis={'title': 'Annualized Return (%)'},
                    margin={'l': 40, 'b': 40, 't': 40, 'r': 10},
                    legend={'x': 0, 'y': 1},
                    hovermode='closest'
                )
            }
        ),
        
        # Drawdown Graph
        dcc.Graph(
            id='drawdown-graph',
            figure={
                'data': [
                    go.Scatter(
                        x=trading_analysis.data['Date'],
                        y=trading_analysis.data['drawdown'],
                        mode='lines',
                        name='Drawdown'
                    )
                ],
                'layout': go.Layout(
                    title='Drawdown Over Time',
                    xaxis={'title': 'Date'},
                    yaxis={'title': 'Drawdown (%)'},
                    margin={'l': 40, 'b': 40, 't': 40, 'r': 10},
                    legend={'x': 0, 'y': 1},
                    hovermode='closest'
                )
            }
        ),
        
        

    ]),
    
    # Risk Analysis Metrics
    html.Div(children=[
        html.H2(children='Risk Analysis'),
        html.P(f'Volatility: {risk_analysis.volatility:.2%}'),
        html.P(f'Value at Risk (95%): {risk_analysis.VaR_95:.2%}'),
        html.P(f'Conditional Value at Risk (95%): {risk_analysis.CVaR_95:.2%}'),
        
    ]),
    
    # Performance Attribution Metrics
    html.Div(children=[
        html.H2(children='Performance Attribution'),
        html.P(f'Win/Loss Ratio: {performance_attribution.win_loss_ratio:.2f}'),
        html.P(f'Average Win: {performance_attribution.average_win:.2f}'),
        html.P(f'Average Loss: {performance_attribution.average_loss:.2f}'),
        html.P(f'Profit Factor: {performance_attribution.profit_factor:.2f}'),
        
    ]),
    
    # Text indicators for latest Annualized Return and Maximum Drawdown
    html.Div(children=[
        html.P(f'Latest Annualized Return: {trading_analysis.data["annualized_return"].iloc[-1]:.2%}'),
        html.P(f'Maximum Drawdown: {trading_analysis.data["drawdown"].min():.2%}'),
    ]),
    
])

# Run the server
if __name__ == '__main__':
    app.run_server(debug=True)
