# stonkr

A python application to display scrolling Stock information on an RGB matrix display usiong the GPIO pins on a Raspberry Pi.

The ticker will scroll through the symbol name, the current price and the percentage change from previous close. The percentage change is green for up, red for down. Then, most importantly of all, STONKS, or NOT STONKS (also red/green).

An API migration of the awesome [`nigel-hall-codes/CryptoTicker`](https://github.com/nigel-hall-codes/CryptoTicker) based on the library example scripts from [`hzeller/rpi-rgb-led-matrix`](https://github.com/hzeller/rpi-rgb-led-matrix/tree/master/bindings/python/samples).

![ticker](images/ticker.gif)

# Instructions

Requires that you've set up Python as per the instructions [in the library repository](https://github.com/hzeller/rpi-rgb-led-matrix/tree/master/bindings/python). Once you can run the examples, you should be good to go.

Requires a *free* API key from [Finnhub](https://finnhub.io).

Edit `dataAPI.py` and replace "APIKEYHERE" with your API key.

In `stonkr.py` add/update with the symbols you want to follow by changing the following line:

`self.stonks = ['MSFT', 'TSLA', 'GOOG']`

```
sudo python stonkr.py
```

Accepts all the options from the main library. For instance, specify a 32 row display:

```
sudo python stonkr.py --led-rows=32
```
