# Generated by Django 4.0.5 on 2022-07-24 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course_video', '0006_rename_coursevideo_coursevideomodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coursevideomodel',
            name='duration',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='coursevideomodel',
            name='video_link',
            field=models.URLField(null=True),
        ),
    ]