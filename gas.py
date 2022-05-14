import requests

def gas_bill():
    base_url = "https://myaccount.enbridgegas.com"
    history_url = "api/GasUse/GasUsageHistoryExport"
    item_id = "7B59DF9D0F-1B6A-4B07-A7FD-36DCAF0594A6%7D"
    account_id = "910035101990"
    url = base_url + history_url + "?" + item_id + "&type=EXCEL" + "&" + "month=0" + "&" + "contractAccountIds=" + account_id # TODO: construct this

    url = "https://myaccount.enbridgegas.com/api/GasUse/GasUsageHistoryExport?itemId={59DF9D0F-1B6A-4B07-A7FD-36DCAF0594A6}&type=Excel&month=0&contractAccountIds=910035101990"
    print(f"url = {url}")

    requests.get(url)

def gas_payment_schedule():
    pass