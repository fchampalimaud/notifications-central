from pyforms_web.widgets.django import ModelAdminWidget
from ..models import UserNotificationConf
from confapp import conf

class UserNotificationsConfApp(ModelAdminWidget):

    UID = 'conf-users-notifications'
    MODEL = UserNotificationConf


    LIST_DISPLAY = ['user', 'notification_type', 'send_email', 'wait_send']

    LIST_FILTER = ['user', 'notification_type', 'send_email']

    TITLE = 'Users notifications'

    LAYOUT_POSITION = conf.ORQUESTRA_HOME

    ORQUESTRA_MENU = 'top'
    ORQUESTRA_MENU_ICON = 'desktop'
    ORQUESTRA_MENU_ORDER = 0

    FIELDSETS = [
        ('send_email', 'wait_send'),
        ('user', 'notification_type'),

    ]