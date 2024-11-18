from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.
def exams_views(request):
    return HttpResponse(" Exams Views")

def attendance_views(request):
    return HttpResponse("Attendance views")

def fees_views(request):
    return HttpResponse("Fees Views")

