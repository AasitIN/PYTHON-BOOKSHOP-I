# Generated by Django 2.2.1 on 2019-12-14 14:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0011_auto_20191214_1427'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='payment',
            name='paytm',
        ),
        migrations.RemoveField(
            model_name='payment',
            name='phone_pay',
        ),
    ]
