import hashlib

from django.conf import settings
from django.db import models

from .notification_type import NotificationType


class Notification(models.Model):

    label = models.CharField('Title', max_length=255)
    text  = models.TextField('Description')

    text_hash = models.CharField('Hash', max_length=255, null=True, blank=True, db_index=True)

    notification_type = models.ForeignKey('NotificationType', on_delete=models.CASCADE, default=1)
    user       = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.CASCADE)
    created_on = models.DateTimeField('Created on', auto_now_add=True)
    read_on    = models.DateTimeField('Read on', null=True, blank=True)
    sent_on    = models.DateTimeField('Sent on', null=True, blank=True)

    period = models.CharField('When to send the email', choices=NotificationType.PERIODS, max_length=1)

    def save(self, *args, **kwargs):
        if self.pk is None:
            self.text_hash = self.hash_text(self.text.encode())
        super().save(*args, **kwargs)


    @staticmethod
    def hash_text(text):
        return hashlib.sha224(text).hexdigest()