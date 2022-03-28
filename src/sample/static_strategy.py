import Strategy
import Data

fake_data = {
    "close": [100, 150, 200, 195],
    "ticker": "AAPL"
}

fake_data2 = {
    "close": [50, 60, 70, 50],
    "ticker": "GOOGL"
}

# if apple is < 196, then buy

dat = Data.Data(ticker = fake_data["ticker"], close_data = fake_data["close"])
dat2 = Data.Data(ticker = fake_data2["ticker"], close_data = fake_data2["close"])
strat = Strategy.Strategy(data = [dat, dat2])

if strat.data_list[0].get_last_traded_price() < 196:
    print("Buy")