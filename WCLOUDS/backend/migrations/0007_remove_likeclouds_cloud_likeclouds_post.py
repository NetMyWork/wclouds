# Generated by Django 4.1.7 on 2023-03-06 12:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0006_shareclouds_cloud_recomend_delete_elements_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='likeclouds',
            name='cloud',
        ),
        migrations.AddField(
            model_name='likeclouds',
            name='post',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='backend.blog'),
        ),
    ]
