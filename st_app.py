import pandas as pd
import streamlit as st
import plotly.express as px
from performance_metrics import TradingAnalysis
from Risk_Analysis import RiskAnalysis
from performance_attribution import PerformanceAttribution
from behave_analysis import BehavioralAnalysisUpdated

# Title of the dashboard
st.title('Trading Dashboard')

# Load data and ensure 'Date' is in datetime format
file_path = 'trading_data.csv'
analysis = TradingAnalysis(file_path)
risk = RiskAnalysis(file_path)
perf = PerformanceAttribution(file_path)
behavior = BehavioralAnalysisUpdated(file_path)

# Ensure 'Date' column is in datetime format for all DataFrames
analysis.data['Date'] = pd.to_datetime(analysis.data['Date'])
risk.data['Date'] = pd.to_datetime(risk.data['Date'])
perf.data['Date'] = pd.to_datetime(perf.data['Date'])
behavior.data['Date'] = pd.to_datetime(behavior.data['Date'])

# Sidebar for date range selection
st.sidebar.header('Filter Data')
date_range = st.sidebar.date_input(
    "Select Date Range",
    value=(analysis.data['Date'].min(), analysis.data['Date'].max()),
    min_value=analysis.data['Date'].min(),
    max_value=analysis.data['Date'].max()
)

# Unpack date range or handle single date selection
start_date, end_date = date_range if isinstance(date_range, tuple) else (date_range, date_range)

# Convert start_date and end_date to datetime64[ns]
start_date = pd.to_datetime(start_date)
end_date = pd.to_datetime(end_date)

# Filter data for each analysis based on selected date range
filtered_data = analysis.data[(analysis.data['Date'] >= start_date) & (analysis.data['Date'] <= end_date)]
filtered_risk_data = risk.data[(risk.data['Date'] >= start_date) & (risk.data['Date'] <= end_date)]
filtered_perf_data = perf.data[(perf.data['Date'] >= start_date) & (perf.data['Date'] <= end_date)]
filtered_behavior_data = behavior.data[(behavior.data['Date'] >= start_date) & (behavior.data['Date'] <= end_date)]

# Trading Analysis Section
st.header('Trading Analysis')
col1, col2, col3 = st.columns(3)
col1.metric('Cumulative Return', f"{filtered_data['cumulative_return'].iloc[-1]*100:.2f}%")
col2.metric('Annualized Return', f"{filtered_data['annualized_return'].iloc[-1]*100:.2f}%")
col3.metric('Max Drawdown', f"{filtered_data['drawdown'].min()*100:.2f}%")

cumulative_return_fig = px.line(filtered_data, x='Date', y='cumulative_return', title='Cumulative Return Over Time')
st.plotly_chart(cumulative_return_fig, use_container_width=True)

# Risk Analysis Section
st.header('Risk Analysis')
col1, col2, col3 = st.columns(3)
col1.metric('Volatility (Std Dev)', f"{risk.volatility*100:.2f}%")
col2.metric('Value at Risk (95%)', f"{risk.VaR_95*100:.2f}%")
col3.metric('Conditional VaR (95%)', f"{risk.CVaR_95*100:.2f}%")

risk_fig = px.histogram(filtered_risk_data, x='daily_return', title='Distribution of Daily Returns')
st.plotly_chart(risk_fig, use_container_width=True)

# Performance Attribution Section
st.header('Performance Attribution')
col1, col2, col3 = st.columns(3)
col1.metric('Win/Loss Ratio', f"{perf.win_loss_ratio:.2f}")
col2.metric('Average Win', f"${perf.average_win:.2f}")
col3.metric('Average Loss', f"${perf.average_loss:.2f}")
st.metric('Profit Factor', f"{perf.profit_factor:.2f}")

# Behavioral Analysis Section
st.header('Behavioral Analysis')
drawdown_fig = px.line(filtered_behavior_data, x='Day', y='drawdown', title='Drawdown Percentage Over Time')
st.plotly_chart(drawdown_fig, use_container_width=True)

drawdown_duration_fig = px.line(filtered_behavior_data, x='Day', y='drawdown_duration', title='Drawdown Duration Over Time')
st.plotly_chart(drawdown_duration_fig, use_container_width=True)
