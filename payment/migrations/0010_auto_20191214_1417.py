# Generated by Django 2.2.1 on 2019-12-14 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0009_auto_20191202_0723'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='card_no',
            field=models.CharField(default='', max_length=21),
        ),
        migrations.AlterField(
            model_name='payment',
            name='payment_type',
            field=models.CharField(default='', max_length=20),
        ),
    ]
