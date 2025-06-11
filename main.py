import matplotlib.pyplot as plt
%matplotlib inline
from utils import risk,eval_str,get_data
from BreakoutStrategy import breakoutStrategy

data=get_data()
Returns=eval_str(data,assets,lookback,stop_loss, target)
print(f'Return over a peroid : {Returns}')

for asset, strategy in strategies.items():
  print(f'{asset}\n{strategy.positions["holdings"].value_counts()}')
  plt.figure(figsize=(20, 10))
  plt.plot(strategy.data['close'], color='black', label='Close Price')

  entry_points = strategy.positions[strategy.positions['holdings'] != 0]
  entry_data = strategy.data.loc[entry_points.index]

  plt.scatter(entry_data.index, entry_data["close"], c=entry_points["holdings"],
                cmap='bwr', label='Positions')  # BLUE : SHORT , RED : LONG
  plt.title(f"{asset} Breakout Strategy")
  plt.legend()
  plt.show()
