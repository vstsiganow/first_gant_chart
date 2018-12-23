# Generated by Django 2.1.4 on 2018-12-23 16:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CalendarPlan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plan_title', models.CharField(max_length=255, unique=True)),
                ('plan_type', models.CharField(max_length=255, unique=True)),
                ('month', models.CharField(max_length=32, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('start_project', models.DateTimeField(verbose_name='start project')),
                ('end_project', models.DateTimeField(verbose_name='end project')),
            ],
        ),
        migrations.AddField(
            model_name='calendarplan',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='NEW_START.Project'),
        ),
    ]
