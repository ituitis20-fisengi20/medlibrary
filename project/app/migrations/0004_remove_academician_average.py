# Generated by Django 4.2.2 on 2023-07-15 01:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_academician_attendance_alter_academician_copy_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='academician',
            name='average',
        ),
    ]
