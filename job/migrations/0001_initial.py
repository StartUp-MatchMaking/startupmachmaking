# Generated by Django 3.0.5 on 2021-04-23 12:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('jobdesc', models.TextField()),
                ('jobtype', models.CharField(max_length=255)),
                ('statdate', models.DateField()),
                ('applyby', models.DateField()),
                ('salary', models.IntegerField()),
                ('aboutjob', models.TextField()),
                ('skills', models.CharField(max_length=255)),
                ('slug', models.CharField(blank=True, max_length=1000, null=True, unique=True)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.Company')),
            ],
        ),
    ]
