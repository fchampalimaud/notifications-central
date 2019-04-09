from django.db import models


class Notification(models.Model):

    label = models.CharField('Title', max_length=255)
    text  = models.TextField('Description')

    notification_type = models.ForeignKey('NotificationType', on_delete=models.CASCADE, default=1)
    user        = models.ForeignKey('auth.User', null=True, blank=True, on_delete=models.CASCADE)
    receivedon  = models.DateTimeField('Received on', auto_now_add=True)
    readon      = models.DateTimeField('Read on', null=True, blank=True)
    senton      = models.DateTimeField('Sent on', null=True, blank=True)