from run import run
from apscheduler.schedulers.blocking import BlockingScheduler

sched = BlockingScheduler()

@sched.scheduled_job('cron', minute='*/15', hour='9-16')
def timed_job():
    run()

sched.start()
