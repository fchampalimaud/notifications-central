# Generated by Django 2.1.5 on 2019-04-09 22:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Title')),
                ('text', models.TextField(verbose_name='Description')),
                ('receivedon', models.DateTimeField(auto_now_add=True, verbose_name='Received on')),
                ('readon', models.DateTimeField(blank=True, null=True, verbose_name='Read on')),
                ('senton', models.DateTimeField(blank=True, null=True, verbose_name='Sent on')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='NotificationType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=100, verbose_name='Code')),
                ('title', models.CharField(max_length=255, verbose_name='Title')),
                ('active', models.BooleanField(default=True, verbose_name='Active')),
                ('delay_send', models.IntegerField(blank=True, null=True, verbose_name='Delay send for X minutes')),
                ('notify_always', models.BooleanField(default=False, verbose_name='Notify always')),
            ],
        ),
        migrations.CreateModel(
            name='UserNotificationConf',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('send_email', models.BooleanField(default=True, verbose_name='Send email')),
                ('wait_send', models.CharField(choices=[('N', 'Send immediately'), ('D', 'Wait one day'), ('W', 'Wait one week'), ('M', 'Wait one month')], max_length=1, verbose_name='Wait to send')),
                ('notification_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='notifications.NotificationType')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
