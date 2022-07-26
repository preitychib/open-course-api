# Generated by Django 4.0.5 on 2022-07-26 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0004_alter_coursemodel_course_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coursemodel',
            name='course_status',
            field=models.CharField(choices=[('published', 'published'), ('requested', 'requested'), ('drafted', 'drafted')], max_length=14),
        ),
    ]
