# Generated by Django 5.0.7 on 2024-09-27 04:41

import datetime
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('comment_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('category', models.CharField(max_length=255)),
                ('content', models.TextField(blank=True, null=True)),
                ('datetime', models.DateTimeField(default=datetime.datetime(2024, 9, 27, 4, 41, 37, 443724, tzinfo=datetime.timezone.utc))),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
