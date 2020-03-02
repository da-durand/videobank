# Generated by Django 3.0.3 on 2020-03-02 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0003_auto_20200225_1007'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='director',
            field=models.CharField(max_length=200, null=True, verbose_name='réalisateur'),
        ),
        migrations.AddField(
            model_name='movie',
            name='synopsis',
            field=models.CharField(max_length=200, null=True),
        ),
    ]