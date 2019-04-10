from pyforms_web.widgets.django import ModelAdminWidget
from ..models import NotificationType
from confapp import conf

class NotificationsTypesApp(ModelAdminWidget):

    UID = 'notifications-types'
    MODEL = NotificationType

    SEARCH_FIELDS = ['code__icontains', 'label__icontains']
    LIST_DISPLAY = ['code', 'label', 'period']

    LIST_FILTER = ['period']

    TITLE = 'Notifications types'

    LAYOUT_POSITION = conf.ORQUESTRA_HOME

    ORQUESTRA_MENU = 'top'
    ORQUESTRA_MENU_ICON = 'desktop'
    ORQUESTRA_MENU_ORDER = 0

    FIELDSETS = [
        'period',
        ('code', 'label')
    ]