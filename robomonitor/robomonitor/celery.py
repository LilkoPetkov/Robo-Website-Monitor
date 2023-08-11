from __future__ import absolute_import, unicode_literals
import os
from celery.schedules import crontab

from celery import Celery

# Set the default Django settings module for the 'celery' program.
# "sample_app" is name of the root app
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'robomonitor.settings')

app = Celery('celery_app',
             broker='redis://localhost:6379/0',
             backend='redis://localhost:6379/0'
             )

# Load task modules from all registered Django apps.
app.autodiscover_tasks()

app.conf.beat_schedule = {
    'my_scheduled_task': {
        'task': 'robomonitor.robo.tasks.scheduled_website_check_24',
        'schedule': crontab(minute="0", hour="*/24"),
    },
    '5 Minute Check': {
        'task': 'robomonitor.robo.tasks.scheduled_website_check_5_minutes',
        'schedule': crontab(minute="*"),
        #'schedule': crontab(minute='*/5'),
    },
    '15 Minute Check': {
        'task': 'robomonitor.robo.tasks.scheduled_website_check_15_minutes',
        'schedule': crontab(minute='*/15'),
    },
    '30 Minute Check': {
        'task': 'robomonitor.robo.tasks.scheduled_website_check_30_minutes',
        'schedule': crontab(minute='*/30'),
    },
    '60 Minute Check': {
        'task': 'robomonitor.robo.tasks.scheduled_website_check_60_minutes',
        'schedule': crontab(minute="0", hour='*/1'),
    },
}



