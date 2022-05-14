from flask import Flask
from gas import gas_payment_schedule
from internet import internet_payment_schedule
from garbage import garbage_collection_schedule

app = Flask(__name__)

@app.route("/")
def schedules():
    gas = gas_payment_schedule()
    internet = internet_payment_schedule()
    waste_collection = garbage_collection_schedule()
    
    
    response_header = """
    <header>
        <h1>Internet</h1>
    </header>
    """
    print(f"internet = {internet}")
    response_body = ""
    for date,amount in internet.items():
        response_body += f"<p>{date}: {amount}</p>"
    
    return response_header + response_body
