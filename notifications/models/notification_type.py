from django.db import models

class NotificationType(models.Model):

    code          = models.CharField('Code', max_length=100, unique=True)
    label         = models.CharField('Title', max_length=255)
    active        = models.BooleanField('Active', default=True)
    delay_send    = models.IntegerField('Delay send for X minutes', null=True, blank=True)
    notify_always = models.BooleanField('Notify always', default=False)
