# Generated by Django 4.2.9 on 2024-08-19 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mydashboardapp', '0009_alter_video_sub_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='Alumni',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('alumni_image', models.ImageField(upload_to='Alumni/Images')),
                ('alumni_video', models.FileField(blank=True, null=True, upload_to='Alumni/Videos/')),
                ('branch', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=50)),
                ('location', models.CharField(max_length=160)),
            ],
        ),
        migrations.CreateModel(
            name='CollegeUpdates',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updates_text', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='FactulyCount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('factuly_count', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Faculty_Mba',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slno', models.IntegerField()),
                ('name', models.CharField(max_length=50)),
                ('designation', models.CharField(max_length=70)),
                ('qualification', models.CharField(max_length=70)),
                ('experience_teaching', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Faculty_Pharamacy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slno', models.IntegerField()),
                ('name', models.CharField(max_length=50)),
                ('designation', models.CharField(max_length=70)),
                ('qualification', models.CharField(max_length=70)),
                ('experience_teaching', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='GalleryImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='Gallery/Images/')),
            ],
        ),
        migrations.CreateModel(
            name='GalleryVideos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video', models.FileField(upload_to='Gallery/videos/')),
            ],
        ),
        migrations.CreateModel(
            name='ProgramsCount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('programs_count', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='StudentForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='StudentsCount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_count', models.IntegerField()),
            ],
        ),
    ]
