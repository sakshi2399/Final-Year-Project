# Generated by Django 3.1.5 on 2021-02-12 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0019_auto_20210209_1029'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appointment',
            name='timeslot',
        ),
        migrations.AlterField(
            model_name='appointment',
            name='date',
            field=models.DateTimeField(),
        ),
    ]