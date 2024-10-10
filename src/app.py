#!/usr/bin/env python3

"""
Routes and views for the flask application.
"""
import os
import sys
from logger import LOGGER as log
from ib_insync import MarketOrder, Stock, IB
from sanic import Sanic
from sanic import response

# Create Sanicobject called app.
app = Sanic(__name__)
# IB constants
HOST: str = "127.0.0.1"
DEMO_PORT: int = 7497
LIVE_PORT: int = 7496

# Create root to easily let us know its on/working.
@app.route('/')
async def root(request):
    return response.text('online')


# Check every minute if we need to reconnect to IB
async def check_if_reconnect() -> None:
    log.info("Checking if we need to reconnect...")
    # Reconnect if needed
    if not app_ib.isConnected() or not app_ib.client.isConnected():
        try:
            log.info("Reconnecting...")
            app_ib.disconnect()
            app_ib_reconnect = IB()
            app_ib_reconnect.connect(HOST, DEMO_PORT, clientId=1)
            app_ib_reconnect.errorEvent += check_on_ib_error
            log.info("Successfully reconnected to TWS")
        except Exception as e:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            file_name = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            log.info(exc_type, file_name, exc_tb.tb_lineno)
            log.warn(f"Make sure TWS or Gateway is open with the correct port: {str(e)}")


@app.route('/webhook', methods=['POST'])
async def webhook(request) -> response.HTTPResponse:
    print(request)
    if request.method == 'POST':
        # Check if we need to reconnect with IB
        await check_if_reconnect()
        # Parse the string data from tradingview into a python dict
        data = request.json
        ticker = str(data['symbol'])
        # Buying stock
        order = MarketOrder("BUY", 1, account=app_ib.wrapper.accounts[0])
        contract = Stock(ticker, 'SMART', 'USD')
        # contract = contract_type_check(ticker=ticker)
        log.info("Buying: " + ticker)
        # Placing order
        app_ib.placeOrder(contract, order)
    return response.json({})


# On IB Error
def check_on_ib_error(reqId, error_code, error_string, contract):
    log.error(f"Error code: {str(error_code)}. Message: {str(error_string)}")


if __name__ == '__main__':
    # Connect to IB on init
    app_ib = IB()
    log.info("Connecting to IB...")
    app_ib.connect(HOST, DEMO_PORT, clientId=1)
    log.info("Successfully Connected to IB")

    app_ib.errorEvent += check_on_ib_error
    app.run(port=5000)
