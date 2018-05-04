import gc
import logging

from celery import Task, shared_task
from chatrender.views.channel import Channel

logger = logging.getLogger(__name__)


class LoggedTask(Task):
    def on_success(self, retval, task_id, args, kwargs):
        logger.info(
            'Published slackchat {}'.format(task_id)
        )

    def on_failure(self, exc, task_id, args, kwargs, einfo):
        logger.error(
            'Slackchat {0} failed to publish: \n{1}'.format(task_id, exc)
        )


@shared_task(acks_late=True, base=LoggedTask)
def publish_slackchat(chat_type, channel_id, statics=False):
    kwargs = {
        'chat_type': chat_type,
        'channel_id': channel_id,
        'statics': statics,
    }
    view = Channel(**kwargs)
    view.publish(**kwargs)
    # Garbage collect after run.
    gc.collect()
