import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as stats

class FinancialDataHandler:
    def __init__(self, start_date, end_date, tickers_list):
        self.start_date=start_date
        self.end_date=end_date
        self.tickers_list=tickers_list
        
        
        self.data=yf.download(self.tickers_list,start=self.start_date,end=self.end_date,auto_adjust=False)
        self.adj_close_data=self.data['Adj Close'].fillna(method='ffill')
        
        self.daily_returns=self.adj_close_data.pct_change().dropna()
        self.log_returns=np.log(self.adj_close_data/self.adj_close_data.shift(1)).dropna()

    
    def plotperformance(self):
        normalised_prices=(self.adj_close_data/self.adj_close_data.iloc[0])*100
        
        plt.plot(normalised_prices)
        plt.xlabel('Date')
        plt.ylabel('Normalised Price (Starts at 100)')
        plt.title('Performances of diverse stocks')
        plt.figure(figsize=(12, 5)
        
        plt.legend(normalised_prices.columns)

    
    def plotvolatility(self):

        rolling_volatility = self.daily_returns.rolling(window=30).std() * np.sqrt(252)

        plt.plot(rolling_volatility)
        plt.legend(rolling_volatility.columns)
        plt.xlabel('Date')
        plt.ylabel('30 Day Rolling Volatility')
        plt.title('Volatilities of diverse stocks')
        
    def correlationheatmap(self):
        correlation_matrix=self.daily_returns.corr()
        sns.heatmap(correlation_matrix, annot=True, cmap='RdYlGn' )

        plt.title('CORRELATION MATRIX OF STOCK RETURNS')
        
        
    
