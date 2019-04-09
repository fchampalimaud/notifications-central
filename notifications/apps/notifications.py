from pyforms_web.widgets.django import ModelAdminWidget
from ..models import Notification
from confapp import conf

class NotificationsApp(ModelAdminWidget):

    UID = 'notifications'
    MODEL = Notification

    SEARCH_FIELDS = ['label__icontains', 'text__icontains']
    LIST_DISPLAY = ['label', 'user', 'receivedon', 'readon', 'senton']

    LIST_FILTER = ['notification_type__label', 'user', 'receivedon']

    TITLE = 'Notifications'

    LAYOUT_POSITION = conf.ORQUESTRA_HOME

    ORQUESTRA_MENU = 'top'
    ORQUESTRA_MENU_ICON = 'desktop'
    ORQUESTRA_MENU_ORDER = 0

    FIELDSETS = [
        'label',
        'text',
        'user',
        ('receivedon', 'readon', 'senton')
    ]