# Generated by Django 3.1.14 on 2022-07-08 04:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0010_delete_hire'),
    ]

    operations = [
        migrations.AddField(
            model_name='apply',
            name='deleted',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='apply',
            name='edited',
            field=models.BooleanField(default=False),
        ),
    ]