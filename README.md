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

```python
from notifications.tools import notify

...

notify('CODE OF THE NOTIFICATION', msg_subject, msg_text, user=user_to_send)

```


###On the Web App

####Superuser view

![Superuser menu](docs/images/superuser-menu.png)


![All users notifications](docs/images/superuser-allnotifications.png)

![Configure notifications](docs/images/superuser-notificationstypes.png)

#### Users

![Configure notifications](docs/images/notifications-icon.png)


![Configure notifications](docs/images/notifications-app.png)


![Configure notifications](docs/images/notifications-config.png)

