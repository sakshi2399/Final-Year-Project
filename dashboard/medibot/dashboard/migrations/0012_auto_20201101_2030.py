# Generated by Django 3.1.2 on 2020-11-01 15:00

from django.db import migrations, models
import django.utils.timezone
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0011_auto_20201101_2025'),
    ]

    operations = [
        migrations.CreateModel(
            name='patient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100)),
                ('gender', models.CharField(blank=True, max_length=10)),
                ('birthday', models.CharField(blank=True, max_length=10)),
                ('email', models.CharField(blank=True, max_length=50)),
                ('age', models.CharField(blank=True, max_length=3)),
                ('address', models.CharField(blank=True, max_length=500)),
                ('pincode', models.CharField(blank=True, max_length=10)),
            ],
        ),
        migrations.RemoveField(
            model_name='reports',
            name='address',
        ),
        migrations.RemoveField(
            model_name='reports',
            name='birthday',
        ),
        migrations.RemoveField(
            model_name='reports',
            name='email',
        ),
        migrations.RemoveField(
            model_name='reports',
            name='pincode',
        ),
        migrations.AddField(
            model_name='reports',
            name='abnormal',
            field=jsonfield.fields.JSONField(null=True),
        ),
        migrations.AddField(
            model_name='reports',
            name='date',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='reports',
            name='file_path',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='reports',
            name='normal',
            field=jsonfield.fields.JSONField(null=True),
        ),
        migrations.AddField(
            model_name='reports',
            name='uploaded_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
