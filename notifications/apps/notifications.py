from pyforms_web.widgets.django import ModelAdminWidget, ModelViewFormWidget
from ..models import Notification
from confapp import conf
from pyforms.controls import ControlHtml

class ViewNotification(ModelViewFormWidget):
    MODEL = Notification

    LAYOUT_POSITION = conf.ORQUESTRA_NEW_WINDOW

    AUTHORIZED_GROUPS = ['superuser']

    FIELDSETS = [
        'label',
        'text',
        ('user', 'period', 'created_on', 'read_on', 'sent_on')
    ]

    def __init__(self, *args, **kwargs):
        self.text = ControlHtml('Message')
        super().__init__(*args, **kwargs)


class NotificationsApp(ModelAdminWidget):

    UID = 'notifications'
    MODEL = Notification

    SEARCH_FIELDS = ['label__icontains', 'text__icontains']
    LIST_DISPLAY = ['label', 'user', 'created_on', 'read_on', 'sent_on', 'period']

    LIST_FILTER = ['notification_type__label', 'user', 'created_on', 'period']

    TITLE = 'Notifications'

    LAYOUT_POSITION = conf.ORQUESTRA_HOME

    USE_DETAILS_TO_EDIT = False
    EDITFORM_CLASS = ViewNotification

    ORQUESTRA_MENU = 'middle-left'
    ORQUESTRA_MENU_ICON = 'bell blue'
    ORQUESTRA_MENU_ORDER = 0
    
    
    AUTHORIZED_GROUPS = ['superuser']

    LIST_ROWS_PER_PAGE = 15



    def has_add_permissions(self):
        return False

    def has_remove_permissions(self, obj):
        return False

    def has_update_permissions(self, obj):
        return False