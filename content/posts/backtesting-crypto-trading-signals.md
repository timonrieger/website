
---
date: '2024-06-21T00:00:00'
draft: False
tags: ['crypto', 'backtest']
title: 'Backtesting Crypto Trading Signals'
summary: 'Evaluating the Performance of a Telegram Crypto Signals Channel with Python'
---
In the world of cryptocurrency trading, reliable signals can make a significant difference in trading outcomes. To assess the profitability of these signals, I backtested a Telegram Crypto Signals Channel I subscribed to lately. The results were surprising and insightful. Let’s dive into the backtest. You can view all the code used in this study on [Github](github.com/timonrieger/brain-snippets-npoint/tree/main/static/assets/code/backtesting-crypto-trading-signals).


Disclaimer
The script and analysis presented in this post have not been verified by external parties. The results of my analysis may be inaccurate, as there might be factors I did not consider in my calculations. There may also be a significant tracking error compared to the "index" (the signals). You should conduct your own research, and please note that this is not financial advice.

About the Signals
-----------------


The signals of the Telegram Channel I analyzed usually look like this: 


`📩 #ARUSDT`


`Long | Entry: 28.658`


`Strategy name: #ARUSDT ARUSDT15-15USDTPERP - Binance Futures | 15 min timeframe`


`— 📤 Signal details —`


`Target 1 : 29.23 probability 100%`


`Target 2 : 29.80 probability 92%`


`Target 3 : 30.38 probability 86%`


`Target 4 : 32.10 probability 72%`


`⛔ Stop-Loss: 25.79 or opposite signal 🔀 or add more at the dip 🔽`


`🏦 Leverage: 10x cross`


 


If you're new to cryptocurrency, here is a brief explanation of the terms used in the trading signals:


* Trading Pair: AR/USDT (trading Arweave against USD Tether coin)
* Trading Direction: Long (profiting from an increase in value)
* Entry: 28\.658 (the entry price for the trade)
* Targets/Take Profits (TP): 29\.23, 29\.80, 30\.38, 32\.10 (prices at which to close the trade and secure profits)
* Stop\-Loss (further SL): 25\.79 (price at which to close the trade to limit your loss)
* Leverage: 10 (if you invest $100 with a leverage of 10, your position is $1000\)



Procedure for the Backtest
--------------------------


 


### Data Preparation:


1. Export Telegram Channel Data: Extract the data from the Telegram channel.
2. Filter Relevant Messages: Identify and filter messages that contain trading signals.
3. Extract Trade Information: Parse each relevant message to extract trade details.
4. Organize Trade Information: Store the extracted trade details in a JSON file.


### Trade Simulation:


1. Enter the Trade: Simulate entering the trade based on the entry price.
2. Check for SL and TPs: Monitor the trade to determine if it hits the stop\-loss or any of the profit targets.
3. Calculate ROI: Compute the return on investment (profit or loss) for each trade.
4. Record Results: Add the ROI along with the trade's closing date to a CSV file.


### Data Analysis:


1. Group ROI by Date: Aggregate the ROI data by date to calculate the average profit or loss per day.
2. Plot Average ROI: Create a plot of the average daily ROI and include the mean value to indicate overall profitability (excluding trading fees).
3. Set Trading Parameters: Define trading parameters such as fees, margin, etc.
4. Calculate Portfolio Balance: Compute the day\-over\-day portfolio balance applying the defined parameters.
5. Calculate Risk Parameters: Evaluate risk metrics like volatility and Sharpe ratio.
6. Plot Account Balance: Visualize the account balance over time for each trade to assess strategy performance in a practical environment, including trading fees.


 


Results of the Backtest
-----------------------


![](/images11.png)


Set parameters such as taker fee, maker fee, funding fee, margin, and leverage. The Taker fee, typically between 0\.04% and 0\.06% of the position size, is charged when entering a trade. The Maker fee, about half the size of the taker fee, is charged upon trade closure. For simplicity, I've assumed a conservative total taker fee of 0\.1%. The funding fee and average funding cycles per trade occur every 8 hours, transferring payments between Short Traders and Long Traders, based on trade duration. With an average trade open for one day, this equates to approximately 3 funding cycles (24h / 8h). Margin represents the percentage of the account balance used for trading (e.g., 0\.02 for 2%). Leverage multiplies fees based on the position size, not the initial investment margin.


`INITIAL = 1000  

MARGIN = 0.02 # 2% adapt as you want  

TAKER_FEE = 0.001  # 0.1%  

FUNDING_FEE = 0.0002  # 0.02%  

LEVERAGE = 10   

AVG_FUNDING_CYCLES_PER_TRADE = 3  # 24h Avg. Trade Length`


![](/images12.png)


As seen above, this strategy proves to be profitable. Before factoring in fees and trade parameters, it achieves an average daily ROI of 2\.85%. Applying these parameters, starting with a $1000 initial investment on May 1, 2023, would yield $2500 by June 18, 2024\. While this timeframe is relatively short in finance, it demonstrates the potential for significant profit with over 2000 trades annually.


The strategy involves 4 Take Profit Targets that decrease exponentially as positions are closed. Additionally, it employs a trailing stop mechanism, which continuously adjusts the stop loss to the latest reached target. When the first profit target is achieved, the stop is moved to breakeven; upon reaching the second target, it adjusts to the first target price, and so forth.


Conclusion
----------


I hope you found that study interesting! Please remain skeptical and don't rely entirely on this study, as errors may have occurred. However, it does highlight that not every Telegram Crypto Signals Group is ineffective. The key is to choose wisely! It's important to note that this strategy could outperform simply buying and holding Bitcoin over the same timeframe by 23% (achieving 150%\+ returns compared to 127%).



                