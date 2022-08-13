from urllib import response
from django.shortcuts import get_object_or_404, render , redirect, HttpResponseRedirect
from django.http import HttpResponse, JsonResponse
from django.http.response import JsonResponse
from django.contrib.auth.decorators import login_required
from .models import Reporter, Article
from .forms import ReporterForm , ArticleForm , RegisterForm

# Create your views here.

# R
#@login_required(login_url="/login")
def list_reporter(request):
    all_reporters = Reporter.objects.all()
    return render(
        request = request,
        template_name= "reporter/list.html",
        context={
            'all_reporters': all_reporters
        }
    )

# C
@login_required(login_url="/login")
def add_reporter(request):
    reporter_form = ReporterForm()
    if request.method == "POST":
        print(request.POST)
        reporter_form = ReporterForm(request.POST)    
        if reporter_form.is_valid(): #is_valid() kiem tra xem da thanh cong hay chua
            print("Form validate successful")
            reporter_form.save()
            return redirect('index')
              
    return render(
         request= request,
         template_name = "reporter/add.html",
         context={
             'form' : reporter_form
         }      
    )
    
# R 
@login_required(login_url="/login") 
def view_detail_reporter(request, reporter_id):
    reporter_data = Reporter.objects.get(id = reporter_id)
    
    return render(
        request = request,
        template_name = "reporter/detail.html",
        context={
            'reporter' : reporter_data
        }
    )

# U
@login_required(login_url="/login")  
def update_reporter(request, reporter_id):
    reporter_data = get_object_or_404(Reporter , id = reporter_id)
    reporter_form = ReporterForm(instance= reporter_data)
    if request.method == "POST":
        # Chinh sua lai thong tin ten nguoi , ho va email update lai vao co so du lieu
        reporter_data.first_name = request.POST.get('first_name', reporter_data.first_name)
        reporter_data.last_name = request.POST.get('last_name', reporter_data.last_name)
        reporter_data.email = request.POST.get('email', reporter_data.email)
        reporter_data.save() 
        return redirect('index')
            
    return render(
        request= request,
        template_name= "reporter/update.html",
        context={
            'form': reporter_form
        }
    )
    
# D
@login_required(login_url="/login")
def delete_reporter(request, reporter_id):
    reporter_data = get_object_or_404(Reporter , id = reporter_id)
    reporter_data.delete()
    return redirect("index")
 
    
def register_user(request):
    form = RegisterForm()
    return render(
        request= request,
        template_name= "register.html",
        context= {
            'form': form
        }
    )   
    
def validate_email(request):
    if request.method == "POST":
        try:
            input_email = request.POST['email']
            Reporter.objects.get(email = input_email) # Lay Reporter theo email
        except Reporter.DoesNotExist:
            return JsonResponse({
                'status': 200,
                "message": " OK "
            })
        return JsonResponse({
            'status': 500,
            "message": " Loi!"
        })   
    
def index(request):
    # response = HttpResponse()
    all_reporters = Reporter.objects.all()
    return render(
        request= request,
        template_name = "index.html",
        context={
            'all_reporters': all_reporters
        }
    )    
    
def add_article(request):
    form_article = ArticleForm()
    if request.method == "POST":
        print(request.POST)
        form_article = ArticleForm(request.POST)    
        if form_article.is_valid(): #is_valid() kiem tra xem da thanh cong hay chua
            print("Form validate successful")
            form_article.save()
            return redirect('index')
              
    return render(
         request= request,
         template_name = "article/add.html",
         context={
             'form' : form_article
         }      
    )
   
    


