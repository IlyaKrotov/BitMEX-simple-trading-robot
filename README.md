# BitMEX simple trading robot.

### Overview
This is a sample trading bot for use with BitMEX. It is free to use and modify for your own strategies.

**Disclaimer: All persons who using this code do so at their own risk.**

**Develop on Testnet first!** \
Testnet trading is completely free and is identical to the live market.

---
### Getting started

Main information that one have to change is hidden in configuration.py.
1. If you want to start from testnet.bitmex.com, then set **TEST_EXCHANGE** to True and put your credentials to 
**API_KEY** and **API_SECRET**. 
2. Then put amount of contracts that you want to trade in each trading execution (**AMOUNT_MONEY_TO_TRADE**) 
and choose preferred leverage (**LEVERAGE**).
3. Then set preferred timeframe for strategy (**TIMEFRAME**). Available variants are: 1m, 5m, 1h, 1d.
4. If you want change parameters of the strategy, go to strategy.py and set different parameters in this place:
```python
macd, signal, hist = talib.MACD(ohlcv_candles.close.values,
                                fastperiod=8, slowperiod=28, signalperiod=9)
```

---

### For advanced users

If you want to change work logic of bot, you have to change 2 main things:

1. Logic of prediction in strategy.py (look at method **predict**)
2. Logic of trade execution in trader.py (look at method **execute_trade**)


---
#### Notes
This code was written for my publication in Habr - https://habr.com/post/358398/.

Also you can look at publication in Medium - https://medium.com/@ilia.krotov/margin-trading-robot-on-the-bitmex-exchange-d94dd46f82c5.

Here my affiliate link for your registration on BitMEX.

https://www.bitmex.com/register/dduBF7

Users who have signed up with a valid affiliate link will receive a **10% fee discount for 6 months.**

#### Issues

Lots of people find this code not easy to run because of some dependencies. Here you can find libraries which are **essential** for succesful run:

1. talib (https://github.com/mrjbq7/ta-lib)
2. bitmex (https://github.com/BitMEX/api-connectors/tree/master/official-http/python-swaggerpy)
And finally, your python must be at least 3.6 version for using f-strings (ex: f"Last prediction: {prediction}")
Then you can successfully run the code.

If you have problems, feel free to open new issue.
