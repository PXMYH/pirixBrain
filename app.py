from flask import Flask
from gas import gas_payment_schedule
from internet import internet_payment_schedule
from garbage import garbage_collection_schedule
from hydro import hydro_payment_schedule
from utility import utility_payment_schedule
from propertyTax import property_tax_payment_schedule

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
        internet_body += f"<p>{date}: {amount}</p>"

    # hydro bill
    hydro_header = """
    <header>
        <h1>Hydro</h1>
    </header>
    """
    hydro_body = ""
    for date,amount in hydro.items():
        hydro_body += f"<p>{date}: {amount}</p>"

    # waste collection
    garbage_header = """
    <header>
        <h1>Garbage Collection</h1>
    </header>
    """
    garbage_body = ""
    for date,amount in garbage.items():
        garbage_body += f"<p>{date}: {amount}</p>"

    # utility
    utility_header = """
    <header>
        <h1>Utility</h1>
    </header>
    """
    utility_body = ""
    for date,amount in utility.items():
        utility_body += f"<p>{date}: {amount}</p>"

    # utility
    gas_header = """
    <header>
        <h1>Gas</h1>
    </header>
    """
    gas_body = ""
    for date,amount in gas.items():
        gas_body += f"<p>{date}: {amount}</p>"
    
    return date_html + \
        internet_header + internet_body + \
        hydro_header + hydro_body + \
        garbage_header + garbage_body + \
        utility_header + utility_body + \
        gas_header + gas_body
