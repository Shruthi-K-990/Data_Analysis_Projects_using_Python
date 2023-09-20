# pip install yfinance to get stock data fom yahoo
import pandas as pd
import yfinance as yf
from datetime import datetime
import plotly.express as px

start_date = datetime.now()  - pd.DateOffset(months=3) #Analyzing stocks for past 3 months
end_date = datetime.now()

tickers = ['AAPL','MSFT','NFLX','GOOG']  #tickers - a type of stock symbol that describes information about the stock of a company
#AAPL - Apple, MSFT - Microsoft,NFLX - Netflix, GOOG - Google
df_list = []

#download last 3 month stocks to analyze
for ticker in tickers:
    data = yf.download(ticker,start=start_date,end=end_date)
    df_list.append(data)

df = pd.concat(df_list,keys=tickers,names=['Ticker','Date'])
#print(df.head())
df = df.reset_index()
fig = px.line(df, x='Date',y='Close',color='Ticker',title="Stock Market Performance for the Last 3 Months")
fig.show()

#analyzing using area chart,which makes easy to compare stocks
fig = px.area(df,x='Date',y='Close',color='Ticker',facet_col='Ticker',labels={'Date':'Date','Close':'Closing Price','Tiker':'Company'},title='Stock Prices for Apple, Microsoft, Netflix, and Google')
fig.show()

#Moving averages(MA) for last 10 and 20 days
#MA - averages of the closing prices of the last ten&20 trading days
df['MA10'] = df.groupby('Ticker')['Close'].rolling(window=10).mean().reset_index(0, drop=True)
df['MA20'] = df.groupby('Ticker')['Close'].rolling(window=20).mean().reset_index(0, drop=True)
for ticker, group in df.groupby('Ticker'):
    fig = px.line(group, x='Date', y=['Close', 'MA10', 'MA20'],title=f"{ticker} Moving Averages")
    fig.show()


# create a DataFrame with the stock prices of Apple and Microsoft
apple = df.loc[df['Ticker'] == 'AAPL', ['Date', 'Close']].rename(columns={'Close': 'AAPL'})
microsoft = df.loc[df['Ticker'] == 'MSFT', ['Date', 'Close']].rename(columns={'Close': 'MSFT'})
df_corr = pd.merge(apple, microsoft, on='Date')

# create a scatter plot to visualize the correlation
fig = px.scatter(df_corr, x='AAPL', y='MSFT', trendline='ols', title='Correlation between Apple and Microsoft')
fig.show()