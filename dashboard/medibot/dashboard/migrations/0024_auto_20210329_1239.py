# Generated by Django 3.1.5 on 2021-03-29 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0023_auto_20210329_0750'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patient_history',
            name='date',
        ),
        migrations.AlterField(
            model_name='patient_history',
            name='prescription',
            field=models.CharField(blank=True, max_length=1000),
        ),
        migrations.AlterField(
            model_name='patient_history',
            name='symptom',
            field=models.CharField(blank=True, max_length=1000),
        ),
    ]
