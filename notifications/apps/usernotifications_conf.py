from pyforms_web.widgets.django import ModelAdminWidget
from ..models import UserNotificationConf
from confapp import conf

class UserNotificationsConfApp(ModelAdminWidget):

    UID = 'conf-users-notifications'
    MODEL = UserNotificationConf


    LIST_DISPLAY = ['user', 'notification_type', 'period']

    LIST_FILTER = ['user', 'notification_type', 'period']

    TITLE = 'Users notifications'

    LAYOUT_POSITION = conf.ORQUESTRA_HOME

    ORQUESTRA_MENU = 'middle-left>NotificationsApp'
    ORQUESTRA_MENU_ICON = 'database'
    ORQUESTRA_MENU_ORDER = 0

    FIELDSETS = [
        'period',
        ('user', 'notification_type'),

    ]

    AUTHORIZED_GROUPS = ['superuser']