# Generated by Django 5.0.7 on 2024-09-27 04:42

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_comment_list', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='datetime',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
