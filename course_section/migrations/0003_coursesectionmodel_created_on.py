# Generated by Django 4.0.5 on 2022-07-23 05:50

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('course_section', '0002_coursesectionmodel_course_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='coursesectionmodel',
            name='created_on',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
