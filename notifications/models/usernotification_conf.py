from django.conf import settings
from django.db import models

from .notification_type import NotificationType


class UserNotificationConf(models.Model):

    user              = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    notification_type = models.ForeignKey('NotificationType', on_delete=models.CASCADE)

    period = models.CharField('When to send the email', choices=NotificationType.PERIODS, max_length=1)

    class Meta:
        unique_together = ( ('user', 'notification_type'), )