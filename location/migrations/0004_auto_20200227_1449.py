# Generated by Django 3.0.3 on 2020-02-27 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('location', '0003_auto_20200227_1442'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movierent',
            name='date_return',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
