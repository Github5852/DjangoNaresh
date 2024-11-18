from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def first_view(request):
    return HttpResponse( 'First view response')

def second_view(request):
    return HttpResponse( 'Second view response')

def third_view(request):
    return HttpResponse( 'Third view response')