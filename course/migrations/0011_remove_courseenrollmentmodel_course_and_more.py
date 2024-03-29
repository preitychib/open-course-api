# Generated by Django 4.0.5 on 2022-07-31 18:50

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('course', '0010_alter_courseenrollmentmodel_meta_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='courseenrollmentmodel',
            name='course',
        ),
        migrations.AddField(
            model_name='courseenrollmentmodel',
            name='course',
            field=models.ManyToManyField(to='course.coursemodel'),
        ),
        migrations.RemoveField(
            model_name='courseenrollmentmodel',
            name='student',
        ),
        migrations.AddField(
            model_name='courseenrollmentmodel',
            name='student',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]
