from pyforms_web.widgets.django import ModelAdminWidget
from ..models import NotificationType
from confapp import conf

class NotificationsTypesApp(ModelAdminWidget):

    UID = 'notifications-types'
    MODEL = NotificationType

    SEARCH_FIELDS = ['code__icontains', 'label__icontains']
    LIST_DISPLAY = ['active', 'code', 'label', 'notify_always', 'delay_send']

    LIST_FILTER = ['active', 'notify_always']

    TITLE = 'Notifications types'

    LAYOUT_POSITION = conf.ORQUESTRA_HOME

    ORQUESTRA_MENU = 'top'
    ORQUESTRA_MENU_ICON = 'desktop'
    ORQUESTRA_MENU_ORDER = 0

    FIELDSETS = [
        'active',
        ('code', 'label'),
        ('notify_always', 'delay_send')
    ]