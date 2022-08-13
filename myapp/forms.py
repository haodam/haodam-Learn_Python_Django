from pyexpat import model
from turtle import width
from django import forms
from django.forms import ModelForm , widgets, Form
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User

from .models import Reporter , Article

class ReporterForm(ModelForm):
    class Meta:
        model = Reporter
        #Lay het tat ca
        #Thuoc tinh fields quan trong minh muon cai property/ thuoc tinh cua class duoc hien thi HTML
        #Lay tat ca luon: fields = "__all__"
        fields = "__all__"
        widgets = {
            'first_name': forms.TextInput(attrs={'class': {'form-control'} }),
            'last_name': forms.TextInput(attrs={'class': {'form-control'} }),
            'email': forms.EmailInput(attrs={'class': {'form-control'} })
        }
    #validation o phia server thi viet for, va muon validate field nao thi tao ham ten clean_<field>  
    def clean_email(self): #Validation cho thuoc tinh email cua Reporter
        input_email = self.cleaned_data['email']
        try:
            Reporter.objects.get(email = input_email) # Lay Reporter theo email
        except Reporter.DoesNotExist:
            # Reporter lay khong duoc
            # Chung to input_email nay chua co trong database
            return input_email
        #input_email da ton tai trong database
        #raise erro cho client biet
        raise ValidationError(f"{input_email} da ton tai. Vui long chon email khac !")

class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = "__all__"
        widgets = {
            'headline': forms.TextInput(attrs={'class': {'form-control'} }),
            'pub_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'reporter': forms.Select(attrs={'class': {'form-control'} })
        }
        
    
class RegisterForm(Form):
    username = forms.CharField(
        label = "Ten Dang Ky",
        widget= forms.TextInput(
            attrs={
                "class": "form-control",
                "id": "username"
            }
        )
    )
    password = forms.CharField(
        label = "Mat Khau", 
        widget = forms.PasswordInput(
            attrs={
                "class": "form-control",
                "id": "password"
            }       
        )
    )
    confirm_password = forms.CharField(
        label = "Nhap Lai Mat Khau",
        widget = forms.PasswordInput(        
            attrs={
                "class": "form-control",
                "id": "confirm_password"
            }        
        )
    )
    email = forms.EmailField(
        label = "Email",
        widget = forms.EmailInput(
            attrs={
                "class": "form-control",
                "id": "email"
            }
        )
    )
    first_name = forms.CharField(
        label = "Ten Dang Ky",
        widget= forms.TextInput(
            attrs={
                "class": "form-control",
                "id": "first_name"
            }
        )       
    )
    last_name = forms.CharField(
        label = "Ho Dang Ky",
        widget= forms.TextInput(
            attrs={
                "class": "form-control",
                "id": "last_name"
            }
        )
    )  
    #avarta = forms.ImageField()
    
    def clean_username(self):
        inputed_username = self.cleaned_data['username']
        try:
            User.objects.get(username = inputed_username)
            raise ValidationError(f"Ten Dang Nhap {inputed_username} da ton tai . Vui long chon ten dang nhap khac")
        except User.DoesNotExist:
            return inputed_username
            
    
    def clean_email(self):
        inputed_email = self.cleaned_data['email']
        try:
            User.objects.get(email = inputed_email) # Lay Reporter theo email
            raise ValidationError(f"{inputed_email} da ton tai. Vui long chon email khac !")
        except User.DoesNotExist:
            # Reporter lay khong duoc
            # Chung to input_email nay chua co trong database   
            #input_email da ton tai trong database
            #raise erro cho client biet
            return inputed_email
       
    
    def clean_confirm_password(self):
        inputed_password = self.cleaned_data['password']
        inputed_confirm_password = self.cleaned_data['confirm_password']
        if inputed_password != inputed_confirm_password:
            raise ValidationError(f"Mat Khau Khong Trung Nhau")
        return inputed_confirm_password
    
    def save_user(self):
        User.objects.create_user(
           username = self.cleaned_data["username"],
           password = self.cleaned_data["password"],
           email = self.cleaned_data["email"],
           first_name = self.cleaned_data["first_name"],
           last_name = self.cleaned_data["last_name"]
        )
        return User.objects.get(username = self.cleaned_data["username"])

class LoginForm(Form):
    username = forms.CharField(
        label = "Ten Dang Ky",
        widget= forms.TextInput(
            attrs={
                "class": "form-control",
                "id": "username"
            }
        )
    )
    password = forms.CharField(
        label = "Mat Khau", 
        widget = forms.PasswordInput(
            attrs={
                "class": "form-control",
                "id": "password"
            }       
        )
    )
    

  