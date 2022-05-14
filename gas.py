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
    # billing date is always end of each month, need to figure out when bill due date is calculated
    schedule = {
        "2022-05-13": "92.37",
        "2022-04-08": "78.53",
        "2022-03-11": "78.93",
        "2022-02-10": "92.62",
        "2022-01-08": "30.53",
        "2021-12-11": "-47.95",
        "2021-11-11": "224.67",
        "2021-10-10": "129.71",
        "2021-09-10": "111.36",
        "2021-08-09": "108.32",
        "2021-07-09": "91.16",
        "2021-06-10": "82.99",
        "2021-05-10": "169.9",
        "2021-04-08": "79.52",
        "2021-03-08": "67.89",
        "2021-02-11": "71.3",
        "2021-01-08": "156.2",
        "2020-12-11": "82.65",
        "2020-11-07": "-4",
        "2020-10-10": "89.57",
        "2020-09-10": "101.31",
        "2020-08-13": "127.28",
        "2020-07-10": "82",
        "2020-06-22": "90.21"
    }
    return schedule
