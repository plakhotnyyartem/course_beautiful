from rest_framework import generics
from courses.models import *
from courses.serializers import *

class CoursesListCreateView(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CoursesListSerializer
    def get_serializer_class(self):
        if self.request.method == 'POST':
            return CoursesCreateSerializer
        return self.serializer_class

class CoursesDeleteUpdateDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    lookup_url_kwarg = 'id'
    serializer_class = CoursesUpdateSerializer

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return CoursesDetailSerializer
        return self.serializer_class

class LessonListCreateView(generics.ListCreateAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonListSerializer

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return LessonCreateSerializer
        return self.serializer_class

class LessonDetailUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Lesson.objects.all()
    lookup_url_kwarg = 'id'
    serializer_class = LessonUpdateSerializer

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return LessonDetailSerializer
        return self.serializer_class
