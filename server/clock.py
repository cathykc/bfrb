from apscheduler.schedulers.background import BackgroundScheduler

from app import db

scheduler = BackgroundScheduler()

@scheduler.scheduled_job('cron', hour=0)
def reminder_example():
    pass

scheduler.start()
