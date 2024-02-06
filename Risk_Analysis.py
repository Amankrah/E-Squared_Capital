import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

class RiskAnalysis:
    def __init__(self, file_path):
        self.data = pd.read_csv(file_path)
        self.data['Date'] = pd.to_datetime(self.data['Date'], format='%m/%d/%Y')
        self.data = self.data.sort_values(by='Date').reset_index(drop=True)
        self.data['daily_return'] = self.data['Daily PNL'] / self.data['Account Equity'].shift(1)
        self.calculate_metrics()
        
    def calculate_metrics(self):
        # Volatility (Standard Deviation)
        self.volatility = self.data['daily_return'].std()
        
        # Value at Risk (VaR) - Using the Historical Method (assuming normal distribution for simplicity)
        # For a 95% confidence level
        self.VaR_95 = self.data['daily_return'].quantile(0.05)
        
        # Conditional Value at Risk (CVaR) - Expected loss beyond the VaR threshold
        # For a 95% confidence level
        self.CVaR_95 = self.data[self.data['daily_return'] <= self.VaR_95]['daily_return'].mean()
        
#     def display_metrics(self):
#         print(f'Volatility (Standard Deviation): {self.volatility:.2f}')
#         print(f'Value at Risk (VaR) 95%: {self.VaR_95:.2f}')
#         print(f'Conditional Value at Risk (CVaR) 95%: {self.CVaR_95:.2f}')
        
#         # Plotting the histogram of daily returns
#         plt.figure(figsize=(10, 5))
#         plt.hist(self.data['daily_return'].dropna(), bins=50, alpha=0.75)
#         plt.axvline(self.VaR_95, color='r', linestyle='dashed', linewidth=2)
#         plt.axvline(self.CVaR_95, color='g', linestyle='dashed', linewidth=2)
#         plt.title('Histogram of Daily Returns')
#         plt.xlabel('Daily Return')
#         plt.ylabel('Frequency')
#         plt.grid(True)
#         plt.show()

# # Initialize the risk analysis with the CSV file path
# risk_analysis = RiskAnalysis('trading_data.csv')
# # Display the risk metrics
# risk_analysis.display_metrics()
