# Generated by Django 2.2.1 on 2019-10-02 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0012_auto_20191002_1010'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='product_id',
            field=models.IntegerField(default=0),
        ),
    ]