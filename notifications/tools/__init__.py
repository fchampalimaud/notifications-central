import os, traceback
from django.template.loader import render_to_string
from ..models import NotificationType, Notification, UserNotificationConf
from django.utils import timezone
from django.core.mail import EmailMessage
from django.conf import settings

def notify(code, title, text, user=None):

    try:
        ntype = NotificationType.objects.get(code=code)
    except NotificationType.DoesNotExist:
        ntype = NotificationType(code=code, label=code)
        ntype.save()

    # don't register the notification if is not active
    if not ntype.active:
        return

    # The notification is set to occur only once
    if ntype.once and Notification.objects.filter(label=title, text_hash=Notification.hash_text(text)).exists():
        return

    notification = Notification(label=title, text=text, user=user, notification_type=ntype)

    try:
        ntypeconf = UserNotificationConf.objects.get(
            notification_type=ntype, user=user
        )
        notification.period = ntypeconf.period
    except UserNotificationConf.DoesNotExist:
        notification.period = ntype.period

    if notification.period == 'I' and user.email:
        try:
            template = os.path.join('emails', 'notification.html')
            rendered_msg = render_to_string(
                template,
                {
                    'notifications': [(ntype.label, [notification])]
                }
            )
            msg = EmailMessage(notification.label, rendered_msg, settings.DEFAULT_FROM_EMAIL, (user.email,))
            msg.content_subtype = "html"
            msg.send()

            notification.sent_on = timezone.now()
        except Exception:
            traceback.print_exc()

    notification.save()



