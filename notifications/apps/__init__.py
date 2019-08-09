from django.apps import AppConfig


class NotificationsConfig(AppConfig):
    name = "notifications"
    verbose_name = "Notifications"

    def ready(self):
        # from .. import signals

        from .usernotifications_conf import UserNotificationsConfApp
        from .notifications_types import NotificationsTypesApp
        from .notifications import NotificationsApp
        from .user_notifications import UserNotificationsApp

        global UserNotificationsConfApp
        global NotificationsTypesApp
        global NotificationsApp
        global UserNotificationsApp
