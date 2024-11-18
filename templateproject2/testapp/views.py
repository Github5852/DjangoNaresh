from django.shortcuts import render
import datetime

# Create your views here.
def info_view(request):
    time = datetime.datetime.now()
    name = "Django"
    requirement = "Python"
    my_dict = {"time":time, "name":name,"requirement":requirement}
    return render(request, 'testapp/result.html',context = my_dict)