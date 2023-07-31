import threading
import time
import schedule
from src.pump_controller.pump_controller import PumpTask, pump_task_queue


default_pump_task = PumpTask(duration_s=10)

pump_scheduler = schedule.Scheduler()
pump_scheduler.every().minute.do(pump_task_queue.put, default_pump_task)
# pump_scheduler.every().day.at("12:09").do(pump_task_queue.put, default_pump_task)
# pump_scheduler.every().day.at("12:10").do(pump_task_queue.put, default_pump_task)
# pump_scheduler.every().day.at("12:11").do(pump_task_queue.put, default_pump_task)
# pump_scheduler.every().day.at("12:12").do(pump_task_queue.put, default_pump_task)
# pump_scheduler.every().day.at("12:13").do(pump_task_queue.put, default_pump_task)

def run_continuously(interval=1):
    """Continuously run, while executing pending jobs at each
    elapsed time interval.
    @return cease_continuous_run: threading. Event which can
    be set to cease continuous run. Please note that it is
    *intended behavior that run_continuously() does not run
    missed jobs*. For example, if you've registered a job that
    should run every minute and you set a continuous run
    interval of one hour then your job won't be run 60 times
    at each interval but only once.
    """
    cease_continuous_run = threading.Event()

    class ScheduleThread(threading.Thread):
        @classmethod
        def run(cls):
            while not cease_continuous_run.is_set():
                pump_scheduler.run_pending()
                time.sleep(interval)

    continuous_thread = ScheduleThread()
    continuous_thread.start()
    return cease_continuous_run