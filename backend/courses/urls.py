from django.urls import path
from courses.views import *
urlpatterns = [
    path('courses/', CoursesListCreateView.as_view()),
    path('courses/<int:id>/', CoursesDeleteUpdateDetailView.as_view()),
]
