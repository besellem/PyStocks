# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    finance.py                                         :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: besellem <besellem@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2021/08/13 18:54:16 by besellem          #+#    #+#              #
#    Updated: 2021/08/13 19:52:04 by besellem         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

### initial code https://gist.github.com/SajidLhessani/69515feb77849ce1456867a924dc74e2

# Raw Package
import yfinance as yf
import plotly.graph_objs as plt
import pandas as pd
import numpy as np
from time import sleep


TICKER='AAPL'

# Get data
data = yf.download(tickers=TICKER, period='1d', interval='1m')

# Save data in a csv file
data.to_csv(f"{TICKER}.csv")

# print(data)


# Plot data
figure = plt.Figure()

# Candle sticks
figure.add_trace(
	plt.Candlestick(
		x=data.index,
		open=data["Open"],
		high=data["High"],
		low=data["Low"],
		close=data["Close"],
		name="Market"
	)
)

# Add titles
figure.update_layout(
    title=f'{TICKER} live share price evolution',
    yaxis_title='Stock Price (USD per Shares)')

# X-Axes
figure.update_xaxes(
    rangeslider_visible=True,
    rangeselector=dict(
        buttons=list([
            dict(count=15, label="15m", step="minute", stepmode="backward"),
            dict(count=45, label="45m", step="minute", stepmode="backward"),
            dict(count=1, label="HTD", step="hour", stepmode="todate"),
            dict(count=3, label="3h", step="hour", stepmode="backward"),
            dict(step="all")
        ])
    )
)

figure.show()
