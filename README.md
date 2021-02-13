# stonkr

This is a python application to display scrolling Stock information on an RGB matrix display usiong the GPIO pins on a Raspberry Pi.

The ticker will scroll through the sybol name, the current price and the percentage change from previous close. The percentage change is green for up, red for down. Then, most importantly of all, are they STONKS, or NOT STONKS?

Based on the awesome [`nigel-hall-codes/CryptoTicker`](https://github.com/nigel-hall-codes/CryptoTicker) and the library from [`hzeller/rpi-rgb-led-matrix`](https://github.com/hzeller/rpi-rgb-led-matrix/tree/master/bindings/python/samples).

![ticker](images/ticker.gif)

# instructions

Requires that you've set up python as per the instructions [in the library repository](https://github.com/hzeller/rpi-rgb-led-matrix/tree/master/bindings/python).

Requires a *free* API key from [Finnhub](https://finnhub.io).

Edit `dataAPI.py` and replace "APIKEYHERE" with your API key.

In `stonkr.py` add/update with the symbols you want to follow by changing the following line:

`self.stonks = ['MSFT', 'TSLA', 'GOOG']`

```
sudo python TickerLED.py &
```

Accpets all the options from the main library. For instance, specify a 32 row display:

```
sudo python TickerLED.py --led-rows=32 &
```
