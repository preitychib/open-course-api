# Generated by Django 4.0.5 on 2022-08-11 10:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0021_alter_coursemodel_total_videos'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='coursemodel',
            name='total_duration',
        ),
    ]