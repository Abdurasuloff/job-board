# Generated by Django 3.1.14 on 2022-07-05 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_remove_worker_user_user_company_name_user_location_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='company_name',
        ),
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]