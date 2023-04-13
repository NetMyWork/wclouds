# Generated by Django 4.1.7 on 2023-03-06 12:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('backend', '0005_alter_message_body'),
    ]

    operations = [
        migrations.CreateModel(
            name='ShareClouds',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(blank=True, max_length=500)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('blog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.blog')),
            ],
        ),
        migrations.AddField(
            model_name='cloud',
            name='recomend',
            field=models.IntegerField(default=0),
        ),
        migrations.DeleteModel(
            name='Elements',
        ),
        migrations.AddField(
            model_name='shareclouds',
            name='cloud',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='recivercloudcloud', to='backend.cloud'),
        ),
        migrations.AddField(
            model_name='shareclouds',
            name='community',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='recieverusercloud', to='backend.community'),
        ),
        migrations.AddField(
            model_name='shareclouds',
            name='sender',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='sendercloud', to=settings.AUTH_USER_MODEL),
        ),
    ]