from django import forms 
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from .models import CustomUser

#fields attributes
email_attrs = {'placeholder':'e.g.Fullname@kuwired.tech','class':'form-control'}
password_attrs = {'placeholder':'Password','class':'form-control'}
password_confrim_attrs = {'placeholder':'Confirm Password','class':'form-control'}
first_name_attrs = {'placeholder':'FirstName','class':'form-control'}
last_name_attrs = {'placeholder':'LastName','class':'form-control'}
user_name_attrs = {'placeholder':'UserName','class':'form-control'}
phone_number_attrs = {'placeholder':'Phone number e.g +260961234512','class':'form-control'}
email_attrs = {'placeholder':'e.g.Fullname@kuwired.tech','class':'form-control'}
ROLE_CHOICES = [
    ('are you a company or an individual', 'are you a company or an individual'),
    ('company', 'Company'),
    ('individual', 'Individual'),
]
company_name_attr = {'placeholder':'Company Name','class':'form-control'}
company_role_attr = {'placeholder':'Your Role In the Company','class':'form-control'}
class Registration_Form(UserCreationForm):
    password1 = forms.CharField(widget=forms.PasswordInput(attrs=password_attrs))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs = password_confrim_attrs))
    email = forms.EmailField(required=True,widget=forms.EmailInput(attrs=email_attrs))
    first_name = forms.CharField(widget=forms.TextInput(attrs=first_name_attrs))
    last_name = forms.CharField(widget=forms.TextInput(attrs=last_name_attrs))
    username = forms.CharField(widget=forms.TextInput(attrs=user_name_attrs))
    phone_number = forms.CharField(widget=forms.TextInput(attrs=phone_number_attrs))
    company_name = forms.CharField(widget=forms.TextInput(attrs=company_name_attr), max_length=255, required=False)
    company_role = forms.CharField(widget=forms.TextInput(attrs=company_role_attr),max_length=100, required=False)
    is_company = forms.ChoiceField(
        choices=ROLE_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control'}),required=True,label="Are you a Company:")  
    password1.label = ""
    password2.label = ""
    email.label = ""
    first_name.label = ""
    last_name.label = ""
    username.label = ""
    company_name.label =""
    company_role.label = ""

    class Meta:
        model = CustomUser
        fields = ['first_name','last_name', 'email', 'username', 'phone_number', 'company_name', 'company_role', 'password1', 'password2']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if CustomUser.objects.filter(email=email).exists():
            raise forms.ValidationError("This email is already registered.")
        return email

    def clean_phone_number(self):
        phone_number = self.cleaned_data.get('phone_number')
        if CustomUser.objects.filter(phone_number=phone_number).exists():
            raise forms.ValidationError("This phone number is already registered.")
        return phone_number
    #   def clean_role(self):
    #    role = self.cleaned_data.get('is_company')
    #    if role == 'are you a company or an individual' or 'are you a company or an individual':
    #       raise forms.ValidationError("select the valid option")