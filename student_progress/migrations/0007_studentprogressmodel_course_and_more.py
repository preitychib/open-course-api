# Generated by Django 4.0.5 on 2022-08-09 18:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0019_alter_coursemodel_published_on_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('student_progress', '0006_remove_studentprogressmodel_course_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentprogressmodel',
            name='course',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='course_progress', to='course.coursemodel'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='studentprogressmodel',
            name='student',
            field=models.ForeignKey(default=17, on_delete=django.db.models.deletion.CASCADE, related_name='student_progress', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
