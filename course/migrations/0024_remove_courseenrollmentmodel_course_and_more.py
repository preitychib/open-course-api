# Generated by Django 4.0.5 on 2022-08-13 09:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('course', '0023_coursemodel_total_duration'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='courseenrollmentmodel',
            name='course',
        ),
        migrations.AddField(
            model_name='courseenrollmentmodel',
            name='course',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='course.coursemodel'),
            preserve_default=False,
        ),
        migrations.RemoveField(
            model_name='courseenrollmentmodel',
            name='student',
        ),
        migrations.AddField(
            model_name='courseenrollmentmodel',
            name='student',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]