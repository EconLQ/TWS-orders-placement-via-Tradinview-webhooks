## Placing orders to IB TWS via Tradingview alerts webhooks

Connect TradingView with Interactive Brokers to process automated signals
as entries and exits in an IB brokerage account.

#### Python version 3.10

### Configuring the alert Webhook and installing ngrock

You'll need to install `ngrock` (URL to the download
page- https://ngrok.com/download)
and at least Pro TradingView subscription for placing webhooks in alerts,
and redirect them to your localhost.

Please, do not forget to add Authtoken from ngrock

-   https://dashboard.ngrok.com/get-started/your-authtoken

After that you'll be able to run ngrock server:

```shell
$ ngrok http 5000
```

Copy the URL from `Forwarding` line and paste it into the alert Webhook line.

Add `/webhook` to the following URL. <b>Note: that webhooks are now available from Premium plan on TradingView<b>

Then, add the message to the `Message` field in the Alert navigation and click
Save:

```json
{
    "message": "YourMessage",
    "symbol": "{{ticker}}",
    "price": "{{close}}",
    "timeframe": "{{interval}}"
}
```

---

### Requirements

To run the application, please do not forget to install the following
requirements. You can do it in your terminal via the following command:

```shell
$ pip3 install --requirement requirements.txt
```

---

### Run app

To run the app via terminal do not forget to change the directory
to `src`.
After that you can simply type this command in your terminal:

```shell
$ python3 app.py
# or
$ chmod +x app.py
$ ./app.py
```
