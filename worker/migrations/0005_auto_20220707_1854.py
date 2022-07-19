# Generated by Django 3.1.14 on 2022-07-07 13:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0010_delete_hire'),
        ('worker', '0004_auto_20220707_1813'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='resume',
            name='category',
        ),
        migrations.AddField(
            model_name='resume',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='job.category'),
        ),
    ]
