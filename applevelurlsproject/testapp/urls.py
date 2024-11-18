from django.urls import path
from . import views


urlpatterns = [
    path('exams/',views.exams_views),
    path('attendance/',views.attendance_views),
    path('fees/',views.fees_views),
]
