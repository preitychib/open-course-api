# Generated by Django 4.0.5 on 2022-08-05 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0014_rename_meta_courseenrollmentmodel_meta_data'),
        ('student_progress', '0003_alter_studentprogressmodel_created_on'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentprogressmodel',
            name='course',
            field=models.ManyToManyField(to='course.coursemodel'),
        ),
    ]
