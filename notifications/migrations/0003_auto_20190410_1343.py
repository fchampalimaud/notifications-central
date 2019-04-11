# Generated by Django 2.2 on 2019-04-10 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notifications', '0002_notificationtype_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notificationtype',
            name='period',
            field=models.CharField(choices=[('0', 'Do not send'), ('I', 'Send immediately'), ('D', 'Daily'), ('W', 'Weekly'), ('M', 'Monthly')], default='I', max_length=1, verbose_name='When to send the email'),
        ),
    ]