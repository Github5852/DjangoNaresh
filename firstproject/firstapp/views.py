from django.shortcuts import render
from django.http import HttpResponse
import datetime

# Create your views here
def dispaly(request):
    s = "</h1>Welcome to django First Applications</h1>"
    return HttpResponse(s)

def time_info(request):
    date = datetime.datetime.now()
    msg = "</h1>Hello Everyone GM</h1><hr>"
    msg+= "<h2>Now Server Time is:"+str(date)+"</h2>"
    return HttpResponse(msg)

def punejobsinfo(request):
    s = "<h1>Pune Jobs Information</h1>"
    return HttpResponse(s)


def hydjobsinfo(request):
    s = "<h1>Hyderabad Jobs Information</h1>"
    return HttpResponse(s)

def Bngjobsinfo(request):
    s = "<h1>Banglore Jobs Information</h1>"
    return HttpResponse(s)

def delhijobsinfo(request):
    s = "<h1>Delhi Jobs Information</h1>"
    return HttpResponse(s)

def datetimeinfo(request):
    date = datetime.datetime.now()
    h = int(date.strftime("%H"))
    msg = "<h1>Hello Guest Very "
    if h < 12 :
        msg += "Good Morning"
    elif h < 16 :
        msg += "Good Afternoon"
    elif h < 21 :
        msg += "Good Evening"
    else:
        msg += "Good Night"
    
    msg += "</h1><hr>"
    msg += "</h1>Now the server time is:"+str(date)+"</h1>"
    return HttpResponse(msg)
        

    