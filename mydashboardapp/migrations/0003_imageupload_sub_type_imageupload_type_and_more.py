from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('mydashboardapp', '0002_banner_news_video'),
    ]

    operations = [
        migrations.AddField(
            model_name='imageupload',
            name='sub_type',
            field=models.CharField(
                choices=[('Image', 'Image'), ('Video', 'Video')],
                default='Image',
                max_length=50
            ),
        ),
        migrations.AddField(
            model_name='imageupload',
            name='type',
            field=models.CharField(
                choices=[('Home', 'Home'), ('Gallery', 'Gallery')],
                default='Home',
                max_length=50
            ),
        ),
        migrations.AlterField(
            model_name='imageupload',
            name='file_size',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='imageupload',
            name='format',
            field=models.CharField(max_length=50, default='Unknown'),  # Assuming a sensible default
        ),
        migrations.AlterField(
            model_name='imageupload',
            name='height',
            field=models.PositiveIntegerField(default=0),  # Default should be numeric
        ),
        migrations.AlterField(
            model_name='imageupload',
            name='width',
            field=models.PositiveIntegerField(default=0),  # Default should be numeric
        ),
        migrations.AlterField(
            model_name='imageupload',
            name='image',
            field=models.ImageField(upload_to='photos/'),
        ),
    ]
