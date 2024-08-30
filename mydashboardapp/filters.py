from rest_framework import filters
from .models import *
from django.db.models import QuerySet
from rest_framework import viewsets
from rest_framework import request
import django_filters

class Imagefilter(filters.BaseFilterBackend):
    def filter_queryset(self,request,queryset,view):
        type_param = request.query_params.get('type', None)
        sub_type_param = request.query_params.get('sub_type', None)
        
        if type_param:
            queryset = queryset.filter(type=type_param)
        if sub_type_param:
            queryset = queryset.filter(sub_type=sub_type_param)
        
        return queryset
    
class Videofilter(filters.BaseFilterBackend):
    def filter_queryset(self,request, queryset,view):
        type_param = request.query_params.get('type', None)
        sub_type_param = request.query_params.get('sub_type', None)


        if type_param:
            queryset = queryset.filter(type=type_param)
        if sub_type_param:
            queryset = queryset.filter(sub_type=sub_type_param)
            
        return queryset 
    
class Bannerfilter(filters.BaseFilterBackend):
    def filter_queryset(self,request,queryset,view):    
        type_param = request.query_params.get('type', None)
        sub_type_param = request.query_params.get('sub_type', None)

        
        if type_param:
            queryset = queryset.filter(type=type_param)
        if sub_type_param:
            queryset = queryset.filter(sub_type=sub_type_param)
        
        return queryset

class Newsfilter(filters.BaseFilterBackend):
    def filter_queryset(self,request,queryset,view):
        type_parm = request.query_params.get('type',None)
        sub_type_parm = request.query_params.get('subtype',None)

        if type_parm:
            queryset = queryset.filter(type = type_parm)
        if sub_type_parm:
            queryset = queryset.filter(sub_type=sub_type_parm)

        return queryset
    
class GalleryImagesfilter(filters.BaseFilterBackend):
    def filter_queryset(self,request,queryset,view):
        type_parm = request.query_params.get('type',None)
        sub_type_parm = request.query_params.get('sub_type',None)

        if type_parm:
            queryset = queryset.filter(type = type_parm)
        if sub_type_parm:
            queryset = queryset.filter(sub_type=sub_type_parm)

        return queryset
    
class GalleryVideosfilter(filters.BaseFilterBackend):
    def filter_queryset(self,request,queryset,view):
        type_parm = request.query_params.get('type',None)
        sub_type_parm = request.query_params.get('sub_type',None)

        if type_parm:
            queryset = queryset.filter(type = type_parm)
        if sub_type_parm:
            queryset = queryset.filter(sub_type=sub_type_parm)

        return queryset
    
class EventsandActivitesfilter(filters.BaseFilterBackend):
    def filter_queryset(self,request,queryset,view):
        type_parm = request.query_params.get('type',None)
        sub_type_parm = request.query_params.get('sub_type',None)

        if type_parm:
            queryset = queryset.filter(type = type_parm)
        if sub_type_parm:
            queryset = queryset.filter(sub_type=sub_type_parm)

        return queryset
    
    
class AlumniFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(field_name='name', lookup_expr='icontains')
    location = django_filters.CharFilter(field_name='location', lookup_expr='icontains')
    designation = django_filters.CharFilter(field_name='designation', lookup_expr='icontains')

    class Meta:
        model = Alumni
        fields = ['name', 'location', 'designation']
