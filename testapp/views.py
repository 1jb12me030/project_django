

from django.shortcuts import render
import datetime

# Create your views here.
def wish(request):
    date=datetime.datetime.now()
    h=int(date.strftime('%H'))
    msg = 'django frame is quite better!!!'
    if h<12:
        msg=msg+'python!!!'
    elif h<16:
        msg=msg+'java!!!'
    elif h<21:
        msg=msg+'javascript!!!'
    else:
        msg = msg+'night'
        
        
          
    response = render(request,'testapp/results.html',{'m':msg,'date':date}) 
    return response  
      
