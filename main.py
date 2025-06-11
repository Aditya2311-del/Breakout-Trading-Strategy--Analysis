import matplotlib.pyplot as plt
%matplotlib inline
from utils import risk, eval_str, get_data
from BreakoutStrategy import breakoutStrategy


assets = ['RELIANCE', 'TCS', 'HDFCBANK', 'ICICIBANK', 'BHARTIARTL']
lookback = 20
stop_loss = 0.05
target = 0.10

data = get_data(assets)

Returns = eval_str(data, assets, lookback, stop_loss, target)
print(f'Return over a period: {Returns}')
