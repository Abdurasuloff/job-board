# Generated by Django 3.1.14 on 2022-07-06 16:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('job', '0007_auto_20220706_1934'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='apply',
            name='employee',
        ),
        migrations.AddField(
            model_name='apply',
            name='employer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='employer', to=settings.AUTH_USER_MODEL),
        ),
    ]
