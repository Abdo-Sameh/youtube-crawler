import os

from crontab import CronTab


def run_task():
    my_cron = CronTab(user=True)
    print 'hiiiiiiiiiiiii'
    job = my_cron.new(command='cd ' + os.getcwd() + ' && /usr/bin/python crawler_task.py')
    job.minute.every(3)
    my_cron.write()
