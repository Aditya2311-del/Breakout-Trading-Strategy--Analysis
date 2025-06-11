assets = ['RELIANCE','TCS','HDFCBANK','ICICIBANK','BHARTIARTL'] # Can be added more for any other Stock

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
