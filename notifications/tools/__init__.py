from ..models import NotificationType, Notification

def notify(code, title, text, user=None):

    try:
        ntype = NotificationType.objects.get(code=code)
    except NotificationType.DoesNotExist:
        ntype = NotificationType(code=code, label=code)
        ntype.save()

    notification = Notification(label=title, text=text, user=user, notification_type=ntype)
    notification.save()
