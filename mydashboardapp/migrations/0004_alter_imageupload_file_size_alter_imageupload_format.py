# Generated by Django 5.0.3 on 2024-07-25 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mydashboardapp', '0003_imageupload_sub_type_imageupload_type_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imageupload',
            name='file_size',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='imageupload',
            name='format',
            field=models.CharField(max_length=50),
        ),
    ]
