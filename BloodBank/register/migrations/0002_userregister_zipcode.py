# Generated by Django 5.1.7 on 2025-03-19 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userregister',
            name='ZipCode',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
