from flask import Flask
from gas import gas_payment_schedule
from internet import internet_payment_schedule
from garbage import garbage_collection_schedule
from hydro import hydro_payment_schedule
from utility import utility_payment_schedule

app = Flask(__name__)

@app.route("/")
def schedules():
    gas = gas_payment_schedule()
    internet = internet_payment_schedule()
    waste_collection = garbage_collection_schedule()
    hydro = hydro_payment_schedule()
    utility = utility_payment_schedule()
    garbage = garbage_collection_schedule()

    # internet bill   
    internet_header = """
    <header>
        <h1>Internet</h1>
    </header>
    """
    print(f"internet = {internet}")
    internet_body = ""
    for date,amount in internet.items():
        internet_body += f"<p>{date}: {amount}</p>"

    # hydro bill
    hydro_header = """
    <header>
        <h1>Hydro</h1>
    </header>
    """
    print(f"hydro = {hydro}")
    hydro_body = ""
    for date,amount in hydro.items():
        hydro_body += f"<p>{date}: {amount}</p>"

    # waste collection
    garbage_header = """
    <header>
        <h1>Garbage Collection</h1>
    </header>
    """
    print(f"garbage = {garbage}")
    garbage_body = ""
    for date,amount in garbage.items():
        garbage_body += f"<p>{date}: {amount}</p>"    
    
    return internet_header + internet_body + hydro_header + hydro_body + garbage_header + garbage_body
