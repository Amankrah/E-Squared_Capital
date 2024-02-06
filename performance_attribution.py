import pandas as pd

class PerformanceAttribution:
    def __init__(self, file_path):
        self.data = pd.read_csv(file_path)
        self.calculate_metrics()
        
    def calculate_metrics(self):
        # Separate wins and losses
        wins = self.data[self.data['Daily PNL'] > 0]['Daily PNL']
        losses = self.data[self.data['Daily PNL'] < 0]['Daily PNL']
        
        # Calculate Win/Loss Ratio
        self.win_loss_ratio = len(wins) / len(losses) if len(losses) > 0 else float('inf')
        
        # Calculate Average Win and Average Loss
        self.average_win = wins.mean() if not wins.empty else 0
        self.average_loss = losses.mean() if not losses.empty else 0
        
        # Calculate Profit Factor
        self.profit_factor = wins.sum() / abs(losses.sum()) if not losses.empty else float('inf')
        
#     def display_metrics(self):
#         print(f'Win/Loss Ratio: {self.win_loss_ratio:.2f}')
#         print(f'Average Win: {self.average_win:.2f}')
#         print(f'Average Loss: {self.average_loss:.2f}')
#         print(f'Profit Factor: {self.profit_factor:.2f}')

# # Initialize the performance attribution analysis with the CSV file path
# performance_attribution = PerformanceAttribution('trading_data.csv')
# # Display the performance metrics
# # performance_attribution.display_metrics()
