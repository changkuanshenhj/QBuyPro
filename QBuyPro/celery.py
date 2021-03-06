from __future__ import absolute_import, unicode_literals
import os

from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'QBuyPro.settings')

app = Celery('QBuyPro',
             broker='redis://127.0.0.1:6379/5',
             backend='redis://127.0.0.1:6379/6',
             namespace='Celery')

app.config_from_object('django.conf:settings')
app.autodiscover_tasks()

