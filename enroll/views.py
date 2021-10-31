from django.shortcuts import render

# Create your views here.

def add_show(req):
    return render(req, 'enroll/addandshow.html')
    
