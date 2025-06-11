class breakoutStrategy():
    def __init__(self,data,stop_loss,target,lookback):
        self.data=data
        self.stop_loss=stop_loss
        self.target=target
        self.lookback=lookback
        self.positions=pd.DataFrame(index=data.index)
        if "holdings" not in self.positions.columns:
            self.positions["holdings"]=0

    def ATR_(self,data_):
        return ta.atr(high=data_["high"],low=data_["low"],close=data_["close"],length=14).iloc[-1]

    def highest_high(self,data_):
        return data_['high'].shift(1).rolling(self.lookback).max().iloc[-1]

    def lowest_low(self,data_):
        return data_['low'].shift(1).rolling(self.lookback).min().iloc[-1]

    def Stop_loss(self,data_):
        return data_["close"].iloc[-1]<((1-self.stop_loss)*data_["close"].iloc[-2])

    def Target(self,data_):
        return data_["close"].iloc[-1]>((1+self.target)*data_["close"].iloc[-2] + 0.5* self.ATR_(data_))

    def run(self):
       for day in range(self.lookback,data.shape[0]):
          df=self.data.iloc[:day]
          if self.Stop_loss(df):
            self.positions['holdings'][day]=-1
          elif self.Target(df):
            self.positions['holdings'][day]=-1
          else:
            if self.highest_high(df) + 0.5*self.ATR_(df) <df['close'].iloc[-1]:
              self.positions['holdings'][day]=1
            elif self.lowest_low(df)>df['close'].iloc[-1]:
              self.positions['holdings'][day]=-1
            else:
              self.positions['holdings'][day]=0

    def calculate_returns(self):
      self.data.loc[:,'returns'] = self.data['close'].pct_change()
      self.positions['strategy_returns'] = self.positions['holdings'].shift(1) * self.data['returns']
      self.positions['cumulative_returns'] = (1 + self.positions['strategy_returns'].fillna(0)).cumprod()
      final_return = self.positions['cumulative_returns'].iloc[-1] - 1
      return final_return
