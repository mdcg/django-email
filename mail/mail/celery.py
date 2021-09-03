from __future__ import absolute_import, unicode_literals

import logging
import os

from celery import Celery
from django.conf import settings

logger = logging.getLogger("Celery")

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mail.settings")

app = Celery("mail")

app.config_from_object("django.conf:settings", namespace="CELERY")

app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print("Request: {0!r}".format(self.request))
