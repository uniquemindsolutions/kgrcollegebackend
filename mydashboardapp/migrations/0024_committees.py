# Generated by Django 4.2.9 on 2024-08-29 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mydashboardapp', '0023_rename_mba_studentonlineregistration_mba_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='committees',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='uploads/')),
            ],
        ),
    ]
