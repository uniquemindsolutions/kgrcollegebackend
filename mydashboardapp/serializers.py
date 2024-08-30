from rest_framework import serializers
from .models import *


class BannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banner
        fields = '__all__'


class CollegeUpdatesSerializer(serializers.ModelSerializer):
    class Meta:
        model = CollegeUpdates
        fields = '__all__'

class StudentsCountSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentsCount
        fields = '__all__'

class FactulyCountSerializer(serializers.ModelSerializer):
    class Meta:
        model = FactulyCount
        fields = '__all__'

class ProgramsCountSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProgramsCount
        fields = '__all__'
    
class StudentFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentForm
        fields = '__all__'
    
class GalleryImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = GalleryImages
        fields = '__all__'
    
class GalleryVideosSerializer(serializers.ModelSerializer):
    class Meta:
        model = GalleryVideos
        fields = '__all__'
    
class Faculty_MbaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Faculty_Mba
        fields = '__all__'
    
class Faculty_PharamacySerializer(serializers.ModelSerializer):
    class Meta:
        model = Faculty_Pharamacy
        fields = '__all__'

class AlumniSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alumni
        fields = '__all__'

class EventsandActivitesSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventsandActivites
        fields = '__all__'
    
class CommitteesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Committees
        fields = '__all__'