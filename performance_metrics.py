import matplotlib.pyplot as plt
import pandas as pd

class TradingAnalysis:
    def __init__(self, file_path):
        self.data = pd.read_csv(file_path)
        self.data['Date'] = pd.to_datetime(self.data['Date'], format='%m/%d/%Y')
        self.data = self.data.sort_values(by='Date').reset_index(drop=True)
        self.initial_equity = self.data['Net Transfer'].sum()
        self.calculate_metrics()
        
    def calculate_metrics(self):
        # Cumulative Return Calculation
        self.data['cumulative_return'] = (self.data['Account Equity'] - self.initial_equity) / self.initial_equity
        
        # Annualized Return Calculation
        days_in_data = (self.data['Date'].iloc[-1] - self.data['Date'].iloc[0]).days
        self.data['annualized_return'] = ((1 + self.data['cumulative_return']) ** (365/days_in_data)) - 1
        
        # Drawdown Calculation
        running_max = self.data['Account Equity'].cummax()
        self.data['drawdown'] = (self.data['Account Equity'] - running_max) / running_max
        
#     def plot_metric(self, metric_name, color, title, ylabel):
#         plt.figure(figsize=(10, 5))
#         plt.plot(self.data['Date'], self.data[metric_name], label=metric_name, color=color)
#         plt.title(f'{title} Over Time')
#         plt.ylabel(ylabel)
#         plt.xlabel('Date')
#         plt.grid(True)
#         # Show current value
#         current_value = self.data[metric_name].iloc[-1]
#         plt.annotate(f'{current_value:.2f}', 
#                      xy=(self.data['Date'].iloc[-1], current_value), 
#                      xytext=(self.data['Date'].iloc[-1], current_value),
#                      arrowprops=dict(facecolor=color, shrink=0.05),
#                      horizontalalignment='right', verticalalignment='top')
#         plt.show()
        
# # Initialize the analysis with the CSV file path
# analysis = TradingAnalysis('trading_data.csv')

# #display results
# results = analysis.calculate_metrics()

# print(results)


# Plot Cumulative Return
#analysis.plot_metric('cumulative_return', 'blue', 'Cumulative Return', 'Cumulative Return')

# # Plot Annualized Return
# analysis.plot_metric('annualized_return', 'green', 'Annualized Return', 'Annualized Return')

# # Plot Drawdown
# analysis.plot_metric('drawdown', 'red', 'Drawdown', 'Drawdown')
