import secrets


def internet_payment_schedule():
    # billing date is always 23rd of each month, need to figure out when bill due date is calculated
    schedule = {
        "2022-03-22": "161.79",
        "2022-04-19": "51.97",
        "2022-05-20": "96.04"
    }
    return schedule
