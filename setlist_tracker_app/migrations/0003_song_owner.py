# Generated by Django 3.2.8 on 2021-10-20 20:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('setlist_tracker_app', '0002_rename_type_link_link_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='owner',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
            preserve_default=False,
        ),
    ]
