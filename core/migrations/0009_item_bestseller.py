# Generated by Django 2.2.3 on 2019-11-28 03:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_auto_20191126_1045'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='bestseller',
            field=models.BooleanField(default=False),
        ),
    ]
