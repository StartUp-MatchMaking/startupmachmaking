# Generated by Django 3.0.5 on 2021-04-24 06:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_job_opening'),
    ]

    operations = [
        migrations.AddField(
            model_name='job_opening',
            name='company',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='user.Company'),
        ),
    ]