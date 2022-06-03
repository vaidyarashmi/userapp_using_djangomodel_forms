from django.shortcuts import redirect, render
from testapp.forms import UserForm
from testapp.models import User
from django.http import HttpResponse
# Create your views here.


def user_views(request):
    form=UserForm()
    if request.method=='POST':
        form=UserForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect('/testapp/user')
        else:
            print("ERROR FORM INVALID")        
    return render(request,'users.html',{'form':form})