# Generated by Django 4.0.5 on 2022-07-26 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course_video', '0007_alter_coursevideomodel_duration_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coursevideomodel',
            name='duration',
            field=models.IntegerField(null=True),
        ),
    ]
