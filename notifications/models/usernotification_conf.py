from django.db import models

class UserNotificationConf(models.Model):

    PERIODS = (
        ('I', 'Send immediately'),
        ('D', 'Wait one day'),
        ('W', 'Wait one week'),
        ('M', 'Wait one month')
    )

    user              = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    notification_type = models.ForeignKey('NotificationType', on_delete=models.CASCADE)

    send_email = models.BooleanField('Send email', default=True)
    wait_send  = models.CharField('Wait to send', choices=PERIODS, max_length=1)