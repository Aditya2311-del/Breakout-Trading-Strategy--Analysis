from tvDatafeed import TvDatafeed,Interval
import pandas as pd
import pandas_ta as ta

def get_data():
   tv=TvDatafeed()
   assets=['RELIANCE','TCS','HDFCBANK','ICICIBANK','BHARTIARTL']
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

  sharps=[abs(strategy.calculate_returns()/risk(data[asset])) for asset, strategy in strategies.items()]
  weigth_sharps=sharps/sum(sharps)
  print(weigth_sharps)
  
  return sum(strategy.calculate_returns()*abs(weigth_sharps[i]) for i ,(asset, strategy) in enumerate(strategies.items()))*100
