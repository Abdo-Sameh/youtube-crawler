import os

from crontab import CronTab

my_cron = CronTab(user=True)
job = my_cron.new(command='cd ' + os.getcwd() + ' && /usr/bin/python crawler_task.py')
job.every().day()
my_cron.write()
