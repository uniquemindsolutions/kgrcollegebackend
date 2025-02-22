from django import forms
from .models import *
from PIL import Image
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class BannerForm(forms.ModelForm):
    class Meta:
        model = Banner
        fields = ['image', 'type', 'sub_type', 'video']

    def clean(self):
        cleaned_data = super().clean()
        image = cleaned_data.get('image')
        video = cleaned_data.get('video')

        # Ensure either an image or a video is uploaded, but not both
        if not image and not video:
            raise forms.ValidationError('You must upload either an image or a video.')
        if image and video:
            raise forms.ValidationError('You cannot upload both an image and a video at the same time.')

        return cleaned_data


class CollegeUpdatesForm(forms.ModelForm):
    class Meta:
        model = CollegeUpdates
        fields = ['updates_text', 'updates_url', 'updates_files']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['updates_files'].widget.attrs.update({'class': 'form-control'})

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

class ImportantSitesForm(forms.ModelForm):
    class Meta:
        model = ImportantSites
        fields = ('__all__')
        widgets = {
            'site_name': forms.TextInput(attrs={'placeholder': 'Enter site name'}),
            'site_url': forms.URLInput(attrs={'placeholder': 'Enter site URL'}),
        }

class StudentFormForm(forms.ModelForm): 
    class Meta:
        model = StudentForm
        fields = ['name', 'email', 'phone_number','message']

class SyllabusForm(forms.ModelForm):
    class Meta:
        model = Syllabus
        fields = ['name','file']

class AlumniForm(forms.ModelForm):
    class Meta:
        model = Alumni
        fields = ['name','designation','branch','location','alumni_image']

class LibraryinfoForm(forms.ModelForm):
    class Meta:
        model = LibraryInfo
        fields = ['library_particulars','description']

class Library_Books_Form(forms.ModelForm):
    class Meta:
        model = Library_Books
        fields = ('__all__')
        
class CommitteesForm(forms.ModelForm):
    class Meta:
        model = Committees
        fields = ['name','file']

class Mba_Faculty_Images_Form(forms.ModelForm):
    class Meta:
        model = Mba_Faculty_Images
        fields = ('__all__')

class BulkFacultyUploadForm(forms.Form):
    excel_file = forms.FileField()
          
class FacultyMBAForm(forms.ModelForm):
    class Meta:
        model = Faculty_Mba
        fields = ['name', 'designation', 'qualification', 'experience_teaching']
        ordering = ['id']           

class FacultyPharmacyForm(forms.ModelForm):
    class Meta:
        model = Faculty_Pharamacy
        fields = ['name', 'designation', 'qualification', 'experience_teaching']

class Course_AdmissionsForm(forms.ModelForm):
    class Meta:
        model = Course_Admissions
        fields = ('__all__')
        
class GalleryImagesForm(forms.ModelForm):
    class Meta:
        model = GalleryImages
        fields = ['type','sub_type','image']

class GalleryVideosForm(forms.ModelForm):
    class Meta:
        model = GalleryVideos
        fields = ['type','sub_type','video']

class StudentOnlineRegistrationForm(forms.ModelForm):
    class Meta:
        model = StudentOnlineRegistration
        fields = "__all__"
               
class EventsandActivitesForm(forms.ModelForm):
    class Meta:
        model = EventsandActivites
        fields = ['type', 'sub_type', 'heading', 'image', 'Video']
        
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
    
