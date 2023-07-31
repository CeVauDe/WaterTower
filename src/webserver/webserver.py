#!/usr/bin/env python

from multiprocessing import Process
from flask import Flask, request

from gpiozero import CPUTemperature

from src.pump_controller.pump_controller import pump_task_queue, PumpTask, pump_worker
import src.schedule.scheduler as scheduler

app = Flask(__name__)

        
@app.route("/")
def flask_main():
    return "<h1>Flask is running</h1><p>Awesome, that worked.  Now add more code.</p>"


@app.route("/run-pump")
def run_pump_on_request():
    duration_s = int(request.args.get('duration', 2))
    app.logger.info(f"Called with duration {duration_s}")
    
    task = PumpTask(duration_s=duration_s)
    pump_task_queue.put(task)
    
    return f"<h1>Queued pump task for pumping {duration_s} s</h1><p>Awesome, that worked.</p>"


def main():
    Process(target=pump_worker, args=(pump_task_queue,)).start()
    stop_scheduler = scheduler.run_continuously()
    app.run(host="0.0.0.0", port=8080, debug=True, use_reloader=False)


if __name__ == "__main__":
    main()