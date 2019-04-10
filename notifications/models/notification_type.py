from django.db import models

class NotificationType(models.Model):

    PERIODS = (
        ('0', 'Do not send'),
        ('I', 'Send immediately'),
        ('D', 'Daily'),
        ('W', 'Weekly'),
        ('M', 'Monthly')
    )

    code   = models.CharField('Code', max_length=100, unique=True)
    label  = models.CharField('Title', max_length=255)
    period = models.CharField('When to send the email', choices=PERIODS, max_length=1)
