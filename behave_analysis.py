import matplotlib.pyplot as plt
import pandas as pd

class BehavioralAnalysisUpdated:
    def __init__(self, file_path):
        self.data = pd.read_csv(file_path)
        self.data['Date'] = pd.to_datetime(self.data['Date'], format='%m/%d/%Y')
        self.data = self.data.sort_values(by='Date').reset_index(drop=True)
        self.data['Day'] = range(1, len(self.data) + 1)  # Day counter from the start of trading
        self.calculate_metrics()
        
    def calculate_metrics(self):
        # Calculate Drawdown
        running_max = self.data['Account Equity'].cummax()
        self.data['drawdown'] = (self.data['Account Equity'] - running_max) / running_max * 100  # Drawdown in percentage
        
        # Identify periods where the drawdown is happening
        self.data['is_drawdown'] = self.data['drawdown'] < 0
        
        # Calculate Drawdown Duration
        self.data['drawdown_duration'] = self.data['is_drawdown'].groupby((self.data['is_drawdown'] != self.data['is_drawdown'].shift()).cumsum()).cumsum()
        
#     def plot_drawdown_duration(self):
#         plt.figure(figsize=(10, 5))
        
#         # Plotting drawdown percentage
#         plt.subplot(2, 1, 1)
#         plt.plot(self.data['Day'], self.data['drawdown'], label='Drawdown (%)', color='purple')
#         plt.title('Drawdown Percentage Over Time')
#         plt.ylabel('Drawdown (%)')
#         plt.grid(True)
        
#         # Plotting drawdown duration
#         plt.subplot(2, 1, 2)
#         plt.plot(self.data['Day'], self.data['drawdown_duration'], label='Drawdown Duration', color='orange')
#         plt.title('Drawdown Duration Over Time')
#         plt.ylabel('Duration (Days)')
#         plt.xlabel('Day')
#         plt.grid(True)
        
#         plt.tight_layout()
#         plt.show()

# # Initialize the updated behavioral analysis with the CSV file path
# behavioral_analysis_updated = BehavioralAnalysisUpdated('trading_data.csv')
# # Plot the updated drawdown duration and percentage
# behavioral_analysis_updated.plot_drawdown_duration()
