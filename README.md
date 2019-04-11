# Notification central


This module manages the user email notifications and aims to reduce the amount of emails sent to the users.
Users can now group their notifications on a single email that can be send daily, weekly or monthly. 

##How to configure

Add the module to the installed apps in django settings, and execute the migration command.

```python
INSTALLED_APPS = [
    'notifications',
    ...
]
```

##How it works

### In the code

Use the next code to notify the user about something. 
Then depending on how the notification is configured the user will receive it immediately by email,
or will receive it later in group with other notifications.

```python
from notifications.tools import notify

...

notify('UNIQUE CODE OF THE NOTIFICATION', msg_subject, msg_text, user=user_to_send)

```


###On the Web App

####Superuser view

The super user will see in its area the next menu:

![Superuser menu](docs/images/superuser-menu.png)

The superuser can configure the next options of the notifications:

- Set the default time when each notification type should be send.
- Activate or deactivate the notifications. In the case a notification type is not active, the messages will not be registered).
- Set the notifications unique code.
- Set the notifications label (Used to send to the user).
- Set a flag that avoid the user to be notified multiple times about the same message.

![Configure notifications](docs/images/superuser-notificationstypes.png)

Access all the users notifications:

![All users notifications](docs/images/superuser-allnotifications.png)



#### Users

![Configure notifications](docs/images/notifications-icon.png)


![Configure notifications](docs/images/notifications-app.png)


![Configure notifications](docs/images/notifications-config.png)

