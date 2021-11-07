from django.shortcuts import HttpResponseRedirect, render
from .forms import StudentRagistraion
from .models import User


# Create your views here.
def add_show(request):
    if request.method == 'POST':
        fm = StudentRagistraion(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            pw = fm.cleaned_data['password']
            reg = User(name=nm, email=em, password=pw)
            reg.save()
            fm = StudentRagistraion()
            stud = User.objects.all()
    else:
        fm = StudentRagistraion()
        stud = User.objects.all()
    return render(request, 'enroll/addandshow.html', {'form': fm, 'stu': stud})


# update
def update_data(request, id):
    if request.method == 'POST':
        pi = User.objects.get(pk=id)
        fm = StudentRagistraion(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi = User.objects.get(pk=id)
        fm = StudentRagistraion(instance=pi)
    return render(request, 'enroll/updatestudent.html', {'form': fm})


# Delete
def delete_data(request, id):
    if request.method == 'POST':
        pi = User.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')
