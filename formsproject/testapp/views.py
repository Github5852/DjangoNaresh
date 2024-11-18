from django.shortcuts import render
from testapp.forms import StudentForms

# Create your views here.
def studentinput_view(request):
    submitted = False
    sname = ''
    if request.method == "POST":
        form = StudentForms(request.POST)
        if form.is_valid():
            print('form validation is success and print data')
            print('ROLLNO:',form.cleaned_data['rollno'])
            print('NAME :', form.cleaned_data['name'])
            print('MARKS :', form.cleaned_data['marks'])
            sname = form.cleaned_data['name']
            submitted = True
    form = StudentForms()
    return render(request,'testapp/input.html', {'form':form,'sname':sname,'submitted':submitted})
