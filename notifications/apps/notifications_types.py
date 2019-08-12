from pyforms_web.widgets.django import ModelAdminWidget
from ..models import NotificationType
from confapp import conf

class NotificationsTypesApp(ModelAdminWidget):

    UID = 'notifications-types'
    MODEL = NotificationType

    AUTHORIZED_GROUPS = ['superuser']

    SEARCH_FIELDS = ['code__icontains', 'label__icontains']
    LIST_DISPLAY = ['code', 'label', 'period', 'active', 'once']

    LIST_FILTER = ['period', 'active', 'once']

    TITLE = 'Notifications types'

    LAYOUT_POSITION = conf.ORQUESTRA_HOME

    ORQUESTRA_MENU = 'top>NotificationsApp'
    ORQUESTRA_MENU_ICON = 'database'
    ORQUESTRA_MENU_ORDER = 0

    FIELDSETS = [
        ('active', 'once','period'),
        ('code', 'label')
    ]
