from flask import Flask, request
from binance.client import Client
from binance.enums import *

app = Flask(__name__)

API_KEY = 'PASTE_YOUR_BINANCE_API_KEY'
API_SECRET = 'PASTE_YOUR_BINANCE_SECRET'
client = Client(API_KEY, API_SECRET)

@app.route('/alok-bot', methods=['POST'])
def webhook():
    data = request.json
    symbol = data['symbol']
    side = data['side']
    quantity = 0.001

    try:
        order = client.futures_create_order(
            symbol=symbol,
            side=SIDE_BUY if side == 'buy' else SIDE_SELL,
            type=ORDER_TYPE_MARKET,
            quantity=quantity
        )
        return {"status": "success"}
    except Exception as e:
        return {"status": "error", "message": str(e)}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
