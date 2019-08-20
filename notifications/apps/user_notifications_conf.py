import traceback

from confapp import conf
from pyforms.basewidget import BaseWidget
from pyforms.controls import ControlCombo
from pyforms_web.utils import make_lambda_func
from pyforms_web.web.middleware import PyFormsMiddleware

from ..models import NotificationType, UserNotificationConf


class UserNotificationsConfigApp(BaseWidget):
    """
    Allow users to configure which notifications they receive and when.
    """

    TITLE = "Configure your notifications"

    LAYOUT_POSITION = conf.ORQUESTRA_NEW_WINDOW

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.formset = [
            "info:Group your notifications by the frequency you want to received them."
        ]

        PERIODS = [(n, c) for c, n in NotificationType.PERIODS]

        user = PyFormsMiddleware.user()

        for n in NotificationType.objects.filter(active=True, visible=True).order_by(
            "code"
        ):
            field_name = "period_{0}".format(n.pk)
            field = ControlCombo(
                n.label,
                items=PERIODS,
                changed_event=make_lambda_func(self.configure, notification_pk=n.pk),
            )

            try:
                un = UserNotificationConf.objects.get(notification_type=n, user=user)
                field.value = un.period
            except UserNotificationConf.DoesNotExist:
                field.value = n.period
                traceback.print_exc()

            setattr(self, field_name, field)
            self.formset.append(field_name)

    def configure(self, notification_pk=None):
        if notification_pk is None:
            return
        try:
            n = NotificationType.objects.get(pk=notification_pk)
        except NotificationType.DoesNotExist:
            traceback.print_exc()

        user = PyFormsMiddleware.user()

        try:
            un = UserNotificationConf.objects.get(notification_type=n, user=user)
        except UserNotificationConf.DoesNotExist:
            un = UserNotificationConf(notification_type=n, user=user)

        field = getattr(self, "period_{0}".format(n.pk))
        un.period = field.value
        un.save()
