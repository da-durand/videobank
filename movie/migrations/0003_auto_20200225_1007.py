# Generated by Django 3.0.3 on 2020-02-25 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0002_moviegenre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='thumb',
            field=models.ImageField(upload_to='media'),
        ),
    ]
