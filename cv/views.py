from django.http import HttpResponse

from django.shortcuts import render

# Create your views here.
def home(request):
    data = {
        'title' : 'about us',
        
    }
    return render(request,'cv/home.html',data)