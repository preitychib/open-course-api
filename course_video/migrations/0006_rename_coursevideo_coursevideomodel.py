# Generated by Django 4.0.5 on 2022-07-24 06:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course_section', '0003_coursesectionmodel_created_on'),
        ('course_video', '0005_coursevideo_created_on'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='CourseVideo',
            new_name='CourseVideoModel',
        ),
    ]
