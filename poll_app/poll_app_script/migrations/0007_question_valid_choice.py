# Generated by Django 3.1.4 on 2020-12-04 21:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poll_app_script', '0006_auto_20201205_0021'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='valid_choice',
            field=models.IntegerField(default=2),
        ),
    ]
