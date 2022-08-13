from urllib import response
from django.shortcuts import render , redirect
from django.http import HttpResponse, JsonResponse
from django.http.response import JsonResponse
from django.views.generic import ListView ,DetailView, CreateView , UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .models import Reporter, Article
from .forms import ReporterForm , ArticleForm , RegisterForm
from .forms import ReporterForm


class ReporterListView(ListView):
    #model = Reporter
    queryset = Reporter.objects.order_by('first_name')
    # Su dung ListView thi phai dinh nghia 1 trong 3 cai:
    # 1. model
    # 2. queryset
    # 3. Override method get_queryset()
    context_object_name = "all_reporters" # all_reporters se thay cho bien objeect_list  {% for reporter in <object_list %}
    # Template mac dinh la LítView nay hien thi la <ten appname> /<ten class modeel viet thuong>_list.html
    # App name , ten model la reporter thi no se hien thi template la myapp/reporter_lít.html
    # Doi templae hien thi
    template_name ="class_base/list_view.html" # Doi template qua template_name
    
    #Hien thi so trang len
    paginate_by = 5
    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['exmaple'] = "Hello from addtional context"
        return context
    
    def get_queryset(self):
        return Reporter.objects.all()
 
@method_decorator(login_required(login_url="/login"), name="dispatch")   
class ReporterDetailView(DetailView):
    model = Reporter
    template_name = "class_base/detail_view.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['exmaple'] = "Hello from addtional context"
        return context
    
    
@method_decorator(login_required(login_url="/login"), name="dispatch")      
class ReporterCreateView(CreateView):
    model = Reporter
    #fields = "__all__"
    form_class = ReporterForm
    template_name = "class_base/create_view.html"
    # khi them 1 thong tin nguoi dung se tra ve trang "all-reporter" 
    success_url = "/all-reporter"


@method_decorator(login_required(login_url="/login"), name="dispatch")       
class ReporterUpdateView(UpdateView):
    model = Reporter
    fields ="__all__"
    template_name = "class_base/update_view.html"
    success_url = "/all-reporter"


@method_decorator(login_required(login_url="/login"), name="dispatch")      
class reporterDeleteView(DeleteView):
    model = Reporter
    template_name = "class_base/confirm_delete_view.html"
    success_url = "/all-reporter"
  

  
# ListView / DetailView R
# CreateView C
# UpdateView U
# DeleteView D