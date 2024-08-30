from django.db import models
import os
from PIL import Image
from django.utils.timezone import now
from django.core.validators import RegexValidator


class Banner(models.Model):
    TYPE_CHOICES = [
        ('Home', 'Home'),
        ('Gallery', 'Gallery'),
        ('Faculty','Faculty')
    ]
    SUB_TYPE_CHOICES = [
        ('Image', 'Image'),
        ('Video', 'Video'),
        ('Banner','Banner'),
        ('News','News')
    ]

    type = models.CharField(max_length=50, choices=TYPE_CHOICES, default='Home')
    sub_type = models.CharField(max_length=50, choices=SUB_TYPE_CHOICES, default='Banner')
    format = models.CharField(max_length=50, blank=True, null=True)
    file_size = models.PositiveIntegerField(blank=True, null=True)
    image = models.ImageField(upload_to='Home/banners/')
    uploaded_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.image.path)
        self.width, self.height = img.size
        super().save(*args, **kwargs)


class CollegeUpdates(models.Model):
    updates_text = models.TextField()

class StudentsCount(models.Model):
    student_count = models.IntegerField()

class FactulyCount(models.Model):
    factuly_count = models.IntegerField()

class ProgramsCount(models.Model):
    programs_count = models.IntegerField()

class StudentForm(models.Model):
    name = models.CharField(max_length=40)
    email = models.EmailField()
    phone_number = models.CharField(max_length=10,
        validators=[
            RegexValidator(
                regex=r'^\d{10}$',
                message='Phone number must be exactly 10 digits.'
            )
        ])


class GalleryImages(models.Model):
    TYPE_CHOICES = [
        ('Home', 'Home'),
        ('Gallery', 'Gallery'),
        ('Faculty','Faculty')
    ]

    SUB_TYPE_CHOICES = [
        ('Image', 'Image'),
        ('Video', 'Video'),
        ('Banner','Banner'),
        ('News','News')
    ]

    type = models.CharField(max_length=50, choices=TYPE_CHOICES, default='Gallery')
    sub_type = models.CharField(max_length=50, choices=SUB_TYPE_CHOICES, default='Image')
    heading = models.CharField(max_length=100)
    format = models.CharField(max_length=50, blank=True, null=True)
    file_size = models.PositiveIntegerField(blank=True, null=True)
    image = models.ImageField(upload_to='Gallery/photos/')
    uploaded_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        
        super().save(*args, **kwargs)
        img = Image.open(self.image.path)
        self.format = img.format  
        self.file_size = os.path.getsize(self.image.path)  
        super().save(*args, **kwargs)


class GalleryVideos(models.Model):
    TYPE_CHOICES = [
        ('Home', 'Home'),
        ('Gallery', 'Gallery'),
        ('Faculty','Faculty')
    ]

    SUB_TYPE_CHOICES = [
        ('Image', 'Image'),
        ('Video', 'Video'),
        ('Banner','Banner'),
        ('News','News')
    ]

    type = models.CharField(max_length=50, choices=TYPE_CHOICES, default='Gallery')
    sub_type = models.CharField(max_length=50, choices=SUB_TYPE_CHOICES, default='Videos')
    heading = models.CharField(max_length=100)
    format = models.CharField(max_length=50, blank=True, null=True)
    file_size = models.PositiveIntegerField(blank=True, null=True)
    video = models.FileField(upload_to='Gallery/videos/')
    uploaded_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.file_size = os.path.getsize(self.video.path) 
        self.format = self.video.path.split('.')[-1].lower()  
        super().save(*args, **kwargs)


class Faculty_Mba(models.Model):
    slno = models.IntegerField()
    name = models.CharField(max_length=50)
    designation = models.CharField(max_length=70)
    qualification = models.CharField(max_length=70)
    experience_teaching = models.CharField(max_length=40)


class Faculty_Pharamacy(models.Model):
    slno = models.IntegerField()
    name = models.CharField(max_length=50)
    designation = models.CharField(max_length=70)
    qualification = models.CharField(max_length=70)
    experience_teaching = models.CharField(max_length=40)


class Alumni(models.Model):
    alumni_image = models.ImageField(upload_to='Alumni/Images')
    alumni_video = models.FileField(upload_to='Alumni/Videos/', null=True, blank=True)
    branch = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=160)
    designation = models.CharField(max_length=100)

class EventsandActivites(models.Model):
    TYPE_CHOICES = [
        ('Home', 'Home'),
        ('Gallery', 'Gallery'),
        ('Faculty', 'Faculty'),
        ('EventsandActivites', 'EventsandActivites')
    ]

    SUB_TYPE_CHOICES = [
        ('Image', 'Image'),
        ('Video', 'Video')
    ]

    type = models.CharField(max_length=50, choices=TYPE_CHOICES, default='EventsandActivites')
    sub_type = models.CharField(max_length=50, choices=SUB_TYPE_CHOICES, default='Image')
    heading = models.CharField(max_length=100)
    format = models.CharField(max_length=50, blank=True, null=True)
    file_size = models.PositiveIntegerField(blank=True, null=True)
    image = models.ImageField(upload_to='EventsandActivites/Images/')
    Video = models.FileField(upload_to='EventsandActivites/Videos/', blank=True, null=True)
    uploaded_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.image:
            img = Image.open(self.image.path)
            self.format = img.format
            self.file_size = os.path.getsize(self.image.path)
            super().save(*args, **kwargs)

class StudentOnlineRegistration(models.Model):
    STUDENT_STATUS_CHOICES = [
        ('Pursuing', 'Pursuing'),
        ('Passed', 'Passed'),
    ]

    student_name = models.CharField(max_length=255)
    father_name = models.CharField(max_length=255)
    date_of_birth = models.DateField()
    permanent_address = models.TextField()
    contact_number = models.CharField(max_length=15)
    email_address = models.EmailField(unique=True)
    mba_status = models.CharField(max_length=10, choices=STUDENT_STATUS_CHOICES, default='Pursuing')
    passed_year = models.IntegerField(null=True, blank=True)
    college = models.CharField(max_length=255, null=True, blank=True)
    university = models.CharField(max_length=255, null=True, blank=True)
    percentage_of_marks = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    cv_or_resume = models.FileField(upload_to='resumes/', null=True, blank=True)

    def __str__(self):
        return self.student_name

class Committees(models.Model):
    file = models.FileField(upload_to='committees/')

