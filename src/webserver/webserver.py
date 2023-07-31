#!/usr/bin/env python

from flask import Flask, request

from gpiozero import CPUTemperature

from src.pump_controller.pump_controller import PumpController

app = Flask(__name__)

        
@app.route("/")
def flask_main():
    return "<h1>Flask is running</h1><p>Awesome, that worked.  Now add more code.</p>"

@app.route("/run-pump")
def run_pump_manual():
    # run_time = request.args.get('duration', 10)
    run_time = 1
    print(f"Called with duration {run_time}")
    
    
    with PumpController() as pump:
        pump.run(duration_s=2)

    return f"<h1>Pump was running for {run_time} s</h1><p>Awesome, that worked.</p>"


def main():
    app.run(host="0.0.0.0", port=8080, debug=True)


if __name__ == "__main__":
    main()