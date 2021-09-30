from django.http.response import HttpResponseRedirect
from django.shortcuts import render, HttpResponse
from .forms import Registration
from .models import User
# Create your views here.
# add all items and show all items
def add_show(request):
    if request.method == 'POST':
        fm=Registration(request.POST)
        if fm.is_valid():
            fm.save()
            fm=Registration()
    else:
        fm=Registration()
    stud=User.objects.all()
    return render(request, 'enroll/addshow.html',{'form':fm,'stud':stud})


# delte view
def delete(request,id):
    if request.method == 'POST':
        pi=User.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')


# update or edit view function
def update(request, id):
    if request.method =='POST':
        pi=User.objects.get(pk=id)
        fm=Registration(request.POST,instance=pi)
        if fm.is_valid():
            fm.save()
    
    else:
        pi=User.objects.get(pk=id)
        fm=Registration(instance=pi)
    return render(request,'enroll/updateshow.html',{'for':fm})
