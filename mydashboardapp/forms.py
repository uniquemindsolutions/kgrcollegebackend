from django import forms
from .models import *
from PIL import Image
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class BannerForm(forms.ModelForm):
    class Meta:
        model = Banner
        fields = ['image','type', 'sub_type']

    # def clean_image(self):
    #     image = self.cleaned_data.get('image')
    #     img = Image.open(image)
    #     if img.width != 1920 or img.height != 1080:
    #         raise forms.ValidationError("Image must be 1920x1080 pixels.")
    #     return image

class CollegeUpdatesForm(forms.ModelForm):
    class Meta:
        model = CollegeUpdates
        fields = ['updates_text']

class StudentsCountForm(forms.ModelForm):
    class Meta:
        model = StudentsCount
        fields = ['student_count']

class FacultyCountForm(forms.ModelForm):
    class Meta:
        model = FactulyCount
        fields = ['factuly_count']

class ProgramsCountForm(forms.ModelForm):
    class Meta:
        model = ProgramsCount
        fields = ['programs_count']

class StudentFormForm(forms.ModelForm): 
    class Meta:
        model = StudentForm
        fields = ['name', 'email', 'phone_number']

class GalleryImagesForm(forms.ModelForm):
    class Meta:
        model = GalleryImages
        fields = ['type','sub_type','image']

class GalleryVideosForm(forms.ModelForm):
    class Meta:
        model = GalleryVideos
        fields = ['type','sub_type','video']

class FacultyMBAForm(forms.ModelForm):
    class Meta:
        model = Faculty_Mba
        fields = ['name', 'designation', 'qualification', 'experience_teaching']
        ordering = ['id']  

class FacultyPharmacyForm(forms.ModelForm):
    class Meta:
        model = Faculty_Pharamacy
        fields = ['name', 'designation', 'qualification', 'experience_teaching']

class AlumniForm(forms.ModelForm):
    class Meta:
        model = Alumni
        fields = ['name','designation','branch','location','alumni_image']

class EventsandActivitesForm(forms.ModelForm):
    class Meta:
        model = EventsandActivites
        fields = ['type', 'sub_type', 'heading', 'image', 'Video']

class StudentOnlineRegistrationForm(forms.ModelForm):
    class Meta:
        model = StudentOnlineRegistration
        fields = "__all__"

class CommitteesForm(forms.ModelForm):
    class Meta:
        model = Committees
        fields = ['name','file']

class SyllabusForm(forms.ModelForm):
    class Meta:
        model = Syllabus
        fields = ['name','file']

class BulkFacultyUploadForm(forms.Form):
    excel_file = forms.FileField()

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
    
