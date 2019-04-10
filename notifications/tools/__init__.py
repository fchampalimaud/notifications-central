from ..models import NotificationType, Notification, UserNotificationConf

def notify(code, title, text, user=None):

    try:
        ntype = NotificationType.objects.get(code=code)
    except NotificationType.DoesNotExist:
        ntype = NotificationType(code=code, label=code)
        ntype.save()

    # don't register the notification if is not active
    if not ntype.active:
        return

    notification = Notification(label=title, text=text, user=user, notification_type=ntype)
    notification.save()
