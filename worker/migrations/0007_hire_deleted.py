# Generated by Django 3.1.14 on 2022-07-08 04:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('worker', '0006_hire_resume'),
    ]

    operations = [
        migrations.AddField(
            model_name='hire',
            name='deleted',
            field=models.BooleanField(default=False),
        ),
    ]
