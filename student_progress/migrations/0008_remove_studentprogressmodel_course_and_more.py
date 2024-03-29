# Generated by Django 4.0.5 on 2022-08-09 18:56

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0019_alter_coursemodel_published_on_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('student_progress', '0007_studentprogressmodel_course_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='studentprogressmodel',
            name='course',
        ),
        migrations.AddField(
            model_name='studentprogressmodel',
            name='course',
            field=models.ManyToManyField(to='course.coursemodel'),
        ),
        migrations.RemoveField(
            model_name='studentprogressmodel',
            name='student',
        ),
        migrations.AddField(
            model_name='studentprogressmodel',
            name='student',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]
