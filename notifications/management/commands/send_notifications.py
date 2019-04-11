from django.core.mail import EmailMessage
from django.core.management.base import BaseCommand
from django.template.loader import render_to_string
from notifications.models import Notification
from django.conf import settings
from django.utils import timezone
import os, traceback

class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('period', type=str)

    def handle(self, *args, **options):

        period = options['period']

        notifications = Notification.objects.filter(sent_on=None, period=period).order_by('notification_type', 'created_on')

        res = {}
        for n in notifications:
            if n.user not in res: res[n.user] = {}

            group = n.notification_type.label
            if group not in res[n.user]: res[n.user][group] = []
            res[n.user][group].append(n)

        template = os.path.join('emails', 'notification.html')
        for user, notifications_groups in res.items():

            rendered_msg = render_to_string(
                template,
                {
                    'notifications': notifications_groups.items()
                }
            )

            try:
                msg = EmailMessage('CORE NOTIFICATIONS', rendered_msg, settings.DEFAULT_FROM_EMAIL, (user.email,))
                msg.content_subtype = "html"
                msg.send()

                for notifications in notifications_groups.values():
                    for n in notifications:
                        n.sent_on = timezone.now()
                        n.save()
            except Exception:
                traceback.print_exc()

