from rest_framework import serializers
from courses.models import *

class CoursesListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['id']


class CoursesDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['id']


class CoursesUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['__all__']

class CoursesCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['__all__']

class LessonDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = ['id']

class LessonListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = ['id']

class LessonUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = ['__all__']

class LessonCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['__all__']

