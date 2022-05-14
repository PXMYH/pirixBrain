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
        "2022-05-19": "145.20",
        "2022-04-19": "132.47",
        "2022-03-21": "193.80",
        "2022-02-22": "201.98",
        "2022-01-20": "170.09",
        
        "2021-12-20": "124.37",
        "2021-11-18": "77.80",
        "2021-10-19": "65.53",
        "2021-09-20": "77.63",
        "2021-08-17": "71.44",
        "2021-07-19": "76.50",
        "2021-06-17": "81.69",
        "2021-05-19": "125.30",
        "2021-04-19": "112.72",
        "2021-03-22": "178.11",
        "2021-02-18": "160.41",
        "2021-01-20": "153.34",

        "2020-12-21": "104.93",
        "2020-11-19": "100.59",
        "2020-10-19": "66.85",
        "2020-09-21": "71.75",
        "2020-08-19": "64.57",
        "2020-07-20": "72.09",
        "2020-06-22": "90.21"
    }
    return schedule
