# Generated by Django 4.0.5 on 2022-07-23 05:41

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='categorymodel',
            name='created_on',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
