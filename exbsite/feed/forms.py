from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column
from .models import *

GRADES = (
    ("","Select your grade..."),
    ('Grade 5 Red','Grade 5 Red'),
    ('Grade 5 Blue','Grade 5 Blue'),
    ('Grade 5 White','Grade 5 White')
    )

class PostForm(forms.Form):
  
  name = forms.CharField(max_length= 30,  widget=forms.TextInput(attrs={'placeholder': 'Enter your name here...'}))
  grade = forms.CharField(max_length =30, widget=forms.Select(choices=GRADES))
  email = forms.EmailField(max_length = 100, widget=forms.TextInput(attrs={'placeholder': 'Enter your email address...'}))
  title = forms.CharField(max_length = 50, widget=forms.TextInput(attrs={'placeholder': 'Enter the name of your product...'}))
  text = forms.CharField(label = 'Description', max_length=1000, widget=forms.Textarea(attrs={'placeholder': 'Enter your product description here...','cols': 200,
        'rows': 5,'style': 'width: 100%'}))
  pic = forms.ImageField(label = 'Choose an image (You can choose a maximum of upto 3 images).')
  pic1 = forms.ImageField(label = '', required = False)
  pic2 = forms.ImageField(label = '', required = False)

class ImagesForm(forms.ModelForm):
    class Meta:
        model = Picture
        fields = ['pic']
