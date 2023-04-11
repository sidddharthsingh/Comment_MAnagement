from django.shortcuts import render,HttpResponsePermanentRedirect
from .forms import CommentManagement
from .models import User
# Create your views here.
def add_show(request):
    if request.method == 'POST':
        
        fm=CommentManagement(request.POST)
        if fm.is_valid():
            co=fm.cleaned_data["Comment"]
            reg = User (Comment=co)
            fm.save()
            fm = CommentManagement()
    else:
        fm = CommentManagement()
    stud=User.objects.all()
    return render(request,'enroll/ADD.html',{'form':fm,'stu':stud})



def update_data(request,id):
    if request.method == 'POST':
        pi=User.objects.get(pk=id)
        fm= CommentManagement(request.POST,instance=pi) 
        if fm.is_valid():
            fm.save()
        else:
            pi = User.objects.get(pk=id)
            fm = CommentManagement(instance=pi)
    return render(request,'enroll/update.html', {'form':fm})

def delete_data(request,id):
    if request.method == 'POST':
        pi=User.objects.get(pk=id)
        pi.delete()
    return HttpResponsePermanentRedirect('/')

