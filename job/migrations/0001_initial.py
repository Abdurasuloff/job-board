# Generated by Django 4.0.5 on 2022-07-02 09:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('slug', models.SlugField()),
            ],
        ),
        migrations.CreateModel(
            name='Vacancy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('description', models.TextField()),
                ('cost', models.PositiveIntegerField()),
                ('cost_for', models.CharField(max_length=50)),
                ('work_type', models.CharField(max_length=50)),
                ('is_closed', models.BooleanField(default=False)),
                ('location', models.CharField(max_length=150)),
                ('needed_experience', models.CharField(max_length=100)),
                ('tags', models.CharField(blank=True, max_length=150, null=True)),
                ('date', models.DateField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='job.category')),
            ],
        ),
    ]