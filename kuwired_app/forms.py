
from django import forms

from .models import ContactMessage


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'subject', 'message']
        widgets = {
            'name' :forms.TextInput(attrs={'placeholder':'Full Name','class':'form-control'}),
            'email':forms.EmailInput(attrs={'placeholder':'e.g.123@example.com','class':'form-control'}),
            'subject' :forms.TextInput(attrs={'placeholder':'subject','class':'form-control'}),
            'message' :forms.Textarea(attrs={'placeholder':'what do you want to share with us?','class':'form-control','rows': 5})
             }
        
