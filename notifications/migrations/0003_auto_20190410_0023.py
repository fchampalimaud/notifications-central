# Generated by Django 2.2 on 2019-04-09 23:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notifications', '0002_auto_20190410_0021'),
    ]

    operations = [
        migrations.RenameField(
            model_name='notification',
            old_name='title',
            new_name='label',
        ),
    ]
