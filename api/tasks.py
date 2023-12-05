from datetime import datetime
from celery import shared_task
from celery.utils.log import get_task_logger

logger = get_task_logger(__name__)


@shared_task
def do_nothing():
    logger.info("Hello from do_nothing")
    return datetime.now().isoformat()
