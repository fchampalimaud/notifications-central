# Generated by Django 2.2 on 2019-04-09 23:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notifications', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='notificationtype',
            old_name='title',
            new_name='label',
        ),
    ]
