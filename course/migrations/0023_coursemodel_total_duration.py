# Generated by Django 4.0.5 on 2022-08-11 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0022_remove_coursemodel_total_duration'),
    ]

    operations = [
        migrations.AddField(
            model_name='coursemodel',
            name='total_duration',
            field=models.IntegerField(null=True),
        ),
    ]