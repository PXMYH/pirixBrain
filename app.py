from flask import Flask
from gas import gas_payment_schedule
from internet import internet_payment_schedule
from garbage import garbage_collection_schedule
from hydro import hydro_payment_schedule
from utility import utility_payment_schedule
from propertyTax import property_tax_payment_schedule
from notification import send_sms
from utils import is_later_than_today

app = Flask(__name__)

@app.route("/")
def schedules():
    gas = gas_payment_schedule()
    internet = internet_payment_schedule()
    hydro = hydro_payment_schedule()
    utility = utility_payment_schedule()
    garbage = garbage_collection_schedule()
    property_tax = property_tax_payment_schedule()

    # today's date
    from datetime import date
    today = date.today()
    date_html = f"Today's date: {today}"

    # internet bill
    internet_header = """
    <header>
        <h1>Internet</h1>
    </header>
    """
    internet_body = ""
    for date,amount in internet.items():
        if is_later_than_today(date, today): send_sms(f"internet bill is due at {date}, amount {amount}")
        internet_body += f"<p>{date}: {amount}</p>"

    # hydro bill
    hydro_header = """
    <header>
        <h1>Hydro</h1>
    </header>
    """
    hydro_body = ""
    for date,amount in hydro.items():
        if is_later_than_today(date, today): send_sms(f"hydro bill is due at {date}, amount {amount}")
        hydro_body += f"<p>{date}: {amount}</p>"

    # waste collection
    garbage_header = """
    <header>
        <h1>Garbage Collection</h1>
    </header>
    """
    garbage_body = ""
    for date,amount in garbage.items():
        if is_later_than_today(date, today): send_sms(f"garbage collection is due at {date}, amount {amount}")
        garbage_body += f"<p>{date}: {amount}</p>"

    # utility
    utility_header = """
    <header>
        <h1>Utility</h1>
    </header>
    """
    utility_body = ""
    for date,amount in utility.items():
        if is_later_than_today(date, today): send_sms(f"utility bill is due at {date}, amount {amount}")
        utility_body += f"<p>{date}: {amount}</p>"

    # gas
    gas_header = """
    <header>
        <h1>Gas</h1>
    </header>
    """
    gas_body = ""
    for date,amount in gas.items():
        if is_later_than_today(date, today): send_sms(f"gas bill is due at {date}, amount {amount}")
        gas_body += f"<p>{date}: {amount}</p>"
    
    return date_html + \
        internet_header + internet_body + \
        hydro_header + hydro_body + \
        garbage_header + garbage_body + \
        utility_header + utility_body + \
        gas_header + gas_body
