from django.http import HttpResponseRedirect
from django.shortcuts import render , redirect, get_object_or_404
from django.contrib.auth import authenticate , login
from django.core.files.storage import FileSystemStorage
import os
from.forms import RegisterForm , LoginForm
from.models import UserAvarta

fs = FileSystemStorage()
def register_user(request):
    form = RegisterForm
    if request.method == "POST":
        print(request.POST)
        #Luu anh User dang ky
        file = request.FILES.get('avarta')
        form = RegisterForm(request.POST)
        if form.is_valid():
            user_created = form.save_user()
            #form.save_user()
            if file != None and file.name != '':
                filepath = os.path.join('static', file.name)
                saved_path= fs.save(filepath, file)
                UserAvarta.objects.create(user = user_created, avarta = saved_path)
            return redirect("index")
            
    return render(
        request= request,
        template_name= "user/register.html",
        context={
            'form': form
        }
    )
    
def login_user(request):
    message= ""
    form = LoginForm()
    if request.method =="POST":
        form =LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                username = form.cleaned_data['username'],
                password = form.cleaned_data['password']
            )
            if user:
                # Kiem tra thong tin tu cline gui len la dung chua 
                # Neu dung thi se dang nhap va tra ve trang index
                print("Thong tin gui len la dung")
                login(request, user)
                # Thay vi login thanh cong chuyen ve trang index , page se o chinh trang day
                if request.GET.get("next"):
                    return HttpResponseRedirect(request.GET.get("next"))
                return redirect("index")
            else:
                print("Thong tin gui len la sai")
                message = "Thong tin ban nhap khong dung. Vui long nhap lai"
    return render(
        request = request ,
        template_name= "user/login.html",
        context= {
            'form': form,
            'message': message
        }
    )
    
    