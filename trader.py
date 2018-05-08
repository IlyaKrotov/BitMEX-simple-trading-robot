class Trader():
    def __init__(self, client, strategy, money_to_trade=100, leverage=5):
        self.client = client
        self.strategy = strategy

        self.money_to_trade = money_to_trade
        self.leverage = leverage

    def execute_trade(self):
        prediction = self.strategy.predict()

        print(f"Last prediction: {prediction}")

        try:
            if prediction == -1:
                response = self.client.Order.Order_new(
                    symbol="XBTUSD",
                    side="Sell",
                    orderQty=self.money_to_trade * self.leverage,
                ).result()
            if prediction == 1:
                response = self.client.Order.Order_new(
                    symbol="XBTUSD",
                    side="Buy",
                    orderQty=self.money_to_trade * self.leverage,
                ).result()
        except Exception:
            print("Something goes wrong!")

        return