# Generated by Django 5.1.4 on 2024-12-12 13:18

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registrationapp', '0007_delete_member'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='studentregistration',
            name='email',
        ),
        migrations.RemoveField(
            model_name='studentregistration',
            name='name',
        ),
        migrations.AddField(
            model_name='studentregistration',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='registrations', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
