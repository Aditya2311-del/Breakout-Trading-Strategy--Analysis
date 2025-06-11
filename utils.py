from tvDatafeed import TvDatafeed,Interval
from BreakoutStrategy import breakoutStrategy
import matplotlib.pyplot as plt
import pandas as pd
import pandas_ta as ta

def get_data(assets):
   tv=TvDatafeed()
   data_dict = {}
   for asset in assets:
      data = tv.get_hist(symbol=asset, exchange='NSE', interval=Interval.in_daily, n_bars=500)
      data_dict[asset] = data

   data=pd.concat(data_dict,axis=1, ignore_index=False)
   return data  

def risk(data):
      df=pd.DataFrame()
      df["returns"]= data["close"].pct_change()
      risk_=df["returns"].std()
      return risk_

def eval_str(data,assets,lookback,stop_loss, target):
 strategies = {}

 for asset in assets:
   strategy = breakoutStrategy(data[asset])
   strategy.run()
   strategies[asset] = strategy

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

   
 sharps=[abs(strategy.calculate_returns()/risk(data[asset])) for asset, strategy in strategies.items()]
 weigth_sharps=sharps/sum(sharps)

  
 
  
 return sum(strategy.calculate_returns()*abs(weigth_sharps[i]) for i ,(asset, strategy) in enumerate(strategies.items()))*100
   
 
