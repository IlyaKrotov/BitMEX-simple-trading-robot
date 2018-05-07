{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "import talib\n",
    "import pandas as pd\n",
    "import bitmex\n",
    "import time"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "class Strategy():\n",
    "    def __init__(self, client, timeframe='5m'):\n",
    "        self.client = client\n",
    "        self.timeframe = timeframe\n",
    "        \n",
    "    def predict(self):\n",
    "        ohlcv_candles = pd.DataFrame(self.client.Trade.Trade_getBucketed(\n",
    "            binSize=self.timeframe,\n",
    "            symbol='XBTUSD',\n",
    "            count=100,\n",
    "            reverse=True\n",
    "        ).result()[0])\n",
    "\n",
    "        ohlcv_candles.set_index(['timestamp'], inplace=True)\n",
    "\n",
    "        macd, signal, hist = talib.MACD(ohlcv_candles.close.values, \n",
    "                                        fastperiod = 8, slowperiod = 28, signalperiod = 9)\n",
    "        \n",
    "        #sell\n",
    "        if hist[-2] > 0 and hist[-1] < 0:\n",
    "            return -1\n",
    "        #buy\n",
    "        if hist[-2] < 0 and hist[-1] > 0:\n",
    "            return 1\n",
    "        #do nothing\n",
    "        else:\n",
    "            return 0"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "class Trader():\n",
    "    def __init__(self, client, strategy, money_to_trade=100, leverage=5):\n",
    "        self.client = client\n",
    "        self.strategy = strategy\n",
    "        \n",
    "        self.money_to_trade = money_to_trade\n",
    "        self.leverage = leverage\n",
    "        \n",
    "    def execute_trade(self):\n",
    "        prediction = self.strategy.predict()\n",
    "        \n",
    "        print(f\"Last prediction: {prediction}\")\n",
    "        \n",
    "        try:\n",
    "            if prediction == -1:\n",
    "                response = self.client.Order.Order_new(\n",
    "                    symbol=\"XBTUSD\",\n",
    "                    side=\"Sell\",\n",
    "                    orderQty=self.money_to_trade * self.leverage,\n",
    "                ).result()\n",
    "            if prediction == 1:\n",
    "                response = self.client.Order.Order_new(\n",
    "                    symbol=\"XBTUSD\",\n",
    "                    side=\"Buy\",\n",
    "                    orderQty=self.money_to_trade * self.leverage,\n",
    "                ).result()\n",
    "        except Exception:\n",
    "            print(\"Something goes wrong!\")\n",
    "        \n",
    "        return"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "scrolled": false
   },
   "outputs": [],
   "source": [
    "client = bitmex.bitmex(\n",
    "    test=True,\n",
    "    api_key=\"\",\n",
    "    api_secret=\"\"\n",
    ")\n",
    "\n",
    "time_to_wait_new_trade = 60*60\n",
    "\n",
    "strategy = Strategy(client, timeframe='1h')\n",
    "trader = Trader(client, strategy)\n",
    "\n",
    "while True:\n",
    "    if round(time.time()) % time_to_wait_new_trade == 0:\n",
    "        trader.execute_trade()\n",
    "        time.sleep(1)"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.6.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
