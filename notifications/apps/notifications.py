from pyforms_web.widgets.django import ModelAdminWidget
from ..models import Notification
from confapp import conf

class NotificationsApp(ModelAdminWidget):

    UID = 'notifications'
    MODEL = Notification

    SEARCH_FIELDS = ['label__icontains', 'text__icontains']
    LIST_DISPLAY = ['label', 'user', 'created_on', 'read_on', 'sent_on', 'period']

    LIST_FILTER = ['notification_type__label', 'user', 'created_on', 'period']

    TITLE = 'Notifications'

    LAYOUT_POSITION = conf.ORQUESTRA_HOME

    ORQUESTRA_MENU = 'top'
    ORQUESTRA_MENU_ICON = 'desktop'
    ORQUESTRA_MENU_ORDER = 0

    FIELDSETS = [
        'label',
        'text',
        'user',
        'period',
        ('created_on', 'read_on', 'sent_on')
    ]