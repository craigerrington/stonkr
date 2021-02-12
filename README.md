# stonkr

This is a python application to disaply strolling Stock information on an RGB matrix display.

The ticker will scroll through the sybol name, the current price and the percentage change from yesterday. The percentage change is green for up, red for down. (STONKS/NOT STONKS functionality coming soon)

Based on the example scripts in [`hzeller/rpi-rgb-led-matrix`](https://github.com/hzeller/rpi-rgb-led-matrix/tree/master/bindings/python/samples) and [`nigel-hall-codes/CryptoTicker`](https://github.com/nigel-hall-codes/CryptoTicker)

# instructions

Requires that you've set up python as per the instructions [in the library repository](https://github.com/hzeller/rpi-rgb-led-matrix/tree/master/bindings/python).

Requires a *free* API key from: https://www.alphavantage.co/

Edit `dataAPI.py` and replace "APIKEYHERE" with your API key.

In `stonkr.py` add/update with the symbols you want to follow by changing the following line:

`self.stonks = ['MSFT', 'TSLA', 'GOOG']`

Run with

```
sudo python TickerLED.py &
```

![ticker](images/ticker.gif)
