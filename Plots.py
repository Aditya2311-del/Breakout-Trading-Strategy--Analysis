import matplotlib.pyplot as plt
%matplotlib inline
from utils import risk,assets,eval_str


for asset, strategy in strategies.items():
  print(f'{asset}\n{strategy.positions["holdings"].value_counts()}')
  plt.figure(figsize=(20, 10))
  plt.plot(strategy.data['close'], color='black', label='Close Price')

  entry_points = strategy.positions[strategy.positions['holdings'] != 0]
  entry_data = strategy.data.loc[entry_points.index]

  plt.scatter(entry_data.index, entry_data["close"], c=entry_points["holdings"],
                cmap='bwr', label='Positions')
  plt.title(f"{asset} Breakout Strategy")
  plt.legend()
  plt.show()
