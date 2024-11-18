from django.shortcuts import render
import datetime

# Create your views here.
def wish(request):
    date  = datetime.datetime.now()
    name = "Akshay"
    roll_no = 26
    Marks = 89
    h = int(date.strftime("%H"))
    msg = "Hello Everyone a Very "
    if h < 12:
        msg = msg + "Morning"
    elif  h < 16:
        msg += "Afternoon"
    elif h < 21:
        msg += "Evening"
    else: 
        msg += "Night"  
    my_date = {'insert_date':date,"name":name,"roll_no":roll_no,"marks":Marks,"insert_msg":msg}
    return render(request,'testapp/wish.html', context = my_date)