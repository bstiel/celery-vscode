import os
import json
import urllib3
import requests
import time
import requests
from celery import shared_task
from requests.adapters import HTTPAdapter
from urllib3 import Retry


from celery import Celery
from celery.utils.log import get_task_logger

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "api.settings")

app = Celery("api")

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object("django.conf:settings", namespace="CELERY")

# from django.conf import settings
# app.conf.update(settings.CELERY)

# Load task modules from all registered Django apps.
app.autodiscover_tasks()

# from celery.utils.log import get_task_logger
