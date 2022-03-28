"""In each strategy, we will need to consult
with data about various stocks."""


class Data:

    def __init__(self, ticker = None, close_data = None, open_data = None, low_data = None, high_data = None, volume_data = None) -> None:
        self.ticker = ticker
        self.close_data = close_data
        self.high_data = high_data
        self.low_data = low_data
        self.open_data = open_data
        self.volume_data = volume_data
    
    def update_close(self, updated):
        self.close_data.append(updated)
    
    def get_last_traded_price(self):
        return self.close_data[-1]