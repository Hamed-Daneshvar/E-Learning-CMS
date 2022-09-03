from rest_framework import serializers
from ..models import Subject, Course, Module


class SubjectSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Subject
        fields = ['id', 'title', 'slug']


class ModuleSrializers(serializers.ModelSerializer):

    class Meta:
        model = Module
        fields = ['order', 'title', 'description']


class CourseSerializers(serializers.ModelSerializer):
    modules = ModuleSrializers(many=True, read_only=True)

    class Meta:
        models = Course
        fields = ['id', 'subject', 'title', 'slug', 'overview',
                  'created', 'owner', 'modules']