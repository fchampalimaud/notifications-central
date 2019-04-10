import traceback
from django.utils import timezone
from django.core.mail import EmailMessage
from django.db import models
from django.conf import settings
from .notification_type import NotificationType
from .usernotification_conf import UserNotificationConf

class Notification(models.Model):

    label = models.CharField('Title', max_length=255)
    text  = models.TextField('Description')

    notification_type = models.ForeignKey('NotificationType', on_delete=models.CASCADE, default=1)
    user       = models.ForeignKey('auth.User', null=True, blank=True, on_delete=models.CASCADE)
    created_on = models.DateTimeField('Created on', auto_now_add=True)
    read_on    = models.DateTimeField('Read on', null=True, blank=True)
    sent_on    = models.DateTimeField('Sent on', null=True, blank=True)

    period = models.CharField('When to send the email', choices=NotificationType.PERIODS, max_length=1)


    def save(self, *args, **kwargs):
        try:
            ntypeconf = UserNotificationConf.objects.get(
                notification_type=self.notification_type, user=self.user
            )
            self.period = ntypeconf.period
        except UserNotificationConf.DoesNotExist:
            self.period = self.notification_type.period

        if self.period=='I' and self.user.email:
            try:
                msg = EmailMessage( self.label, self.text, settings.DEFAULT_FROM_EMAIL, self.user.email)
                msg.content_subtype = "html"
                msg.send()
                self.sent_on = timezone.now()
                super().save(*args, **kwargs)
            except Exception:
                traceback.print_exc()

        super().save(*args, **kwargs)
