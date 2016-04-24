from run import run
from apscheduler.schedulers.blocking import BlockingScheduler
import logging

logging.basicConfig()

sched = BlockingScheduler()

@sched.scheduled_job('cron', minute='*/15', hour='7-18')
def timed_job():
    run()

sched.start()
