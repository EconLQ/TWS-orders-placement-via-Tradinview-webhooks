from ib_insync import Contract


def contract_type_check(ticker: str) -> Contract:
    contract = Contract()
    contract.symbol = ticker
    if ticker == "SPY":
        contract.secType = "STK"
        contract.currency = "USD"
        contract.exchange = "ARCA"
    elif ticker[0:3] == "ETH":
        contract.secType = "CRYPTO"
        contract.currency = "USD"
        contract.exchange = "PAXOS"
    elif ticker[0:3] == "EUR":
        contract.secType = "CASH"
        contract.currency = "USD"
        contract.exchange = "IDEALPRO"
    else:
        print(f"It seems there is no ticker {ticker} in TWS.\n"
              f"Please, check it one more time and modify the alert message")
    return contract
