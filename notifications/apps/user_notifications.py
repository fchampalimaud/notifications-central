from pyforms_web.web.middleware import PyFormsMiddleware
from pyforms_web.widgets.django import ModelAdminWidget, ModelViewFormWidget
from django.utils import timezone
from ..models import Notification
from confapp import conf
from pyforms.controls import ControlHtml, ControlCheckBox, ControlButton
from .user_notifications_conf import UserNotificationsConfigApp

class ViewUserNotification(ModelViewFormWidget):
    MODEL = Notification

    LAYOUT_POSITION = conf.ORQUESTRA_NEW_WINDOW



    FIELDSETS = [
        '_unread',
        'label',
        'text',
        ('user', 'period', 'created_on', 'read_on', 'sent_on')
    ]

    def __init__(self, *args, **kwargs):
        self.text = ControlHtml('Message')
        self._unread = ControlButton(
            "<i class='icon envelope'></i>Mark as unread",
            css='orange right floated',
            label_visible=False,
            default=self.__mark_unread_evt
        )

        super().__init__(*args, **kwargs)

    def __mark_unread_evt(self):
        obj = self.model_object
        obj.read_on = None
        self.read_on.value = None
        obj.save()
        self._unread.hide()
        self.parent.populate_list()



class UserNotificationsApp(ModelAdminWidget):

    UID = 'user-notifications'
    MODEL = Notification

    SEARCH_FIELDS = ['label__icontains', 'text__icontains']
    LIST_DISPLAY = ['label', 'created_on', 'read_on', 'sent_on']

    LIST_FILTER = ['created_on']

    TITLE = 'Notifications'

    LAYOUT_POSITION = conf.ORQUESTRA_NEW_TAB

    EDITFORM_CLASS = ViewUserNotification

    ORQUESTRA_MENU = 'top'
    ORQUESTRA_MENU_ORDER = 0

    USE_DETAILS_TO_EDIT = False


    def __init__(self, *args, **kwargs):

        self._unread = ControlCheckBox(
            'Show only unread messages',
            changed_event=self.populate_list,
            default=True,
            css='right floated'
        )

        self._confbtn = ControlButton(
            '<i class="icon cog" ></i>Config',
            css='basic blue right floated',
            default=self.__confbtn_evt
        )

        super().__init__(*args, **kwargs)


    def __confbtn_evt(self):
        UserNotificationsConfigApp()

    def get_toolbar_buttons(self, has_add_permission=False):
        return [ ('_unread', '_confbtn') ]


    def get_queryset(self, request, queryset):
        if self._unread.value:
            return queryset.filter(user=request.user, read_on=None)
        else:
            return queryset.filter(user=request.user)

    def has_add_permissions(self):
        return False

    def has_remove_permissions(self, obj):
        return False

    def has_update_permissions(self, obj):
        return False

    def show_edit_form(self, obj_pk=None):
        try:
            n = Notification.objects.get(pk=obj_pk)
            n.read_on = timezone.now()
            n.save()

        except Notification.DoesNotExist:
            pass
        return super().show_edit_form(obj_pk)

    @property
    def title(self):
        return "Notifications"

    @title.setter
    def title(self, value):
        pass

    @property
    def TITLE(self):
        user = PyFormsMiddleware.user()
        n_msgs = Notification.objects.filter(user=user, read_on=None).count()
        if n_msgs == 0:
            return """<i class="bell icon"></i>"""
        else:
            return """<i class="bell red icon"></i> {0}""".format(n_msgs)