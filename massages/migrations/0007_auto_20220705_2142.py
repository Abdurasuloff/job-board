# Generated by Django 3.1.14 on 2022-07-05 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('massages', '0006_apply_vacancy'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apply',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='massage',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
