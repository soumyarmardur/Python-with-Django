from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
import re
from .models import UserProfile
from django import forms


class UserRegisterForm(UserCreationForm):
    username = forms.CharField(max_length=20,widget=forms.TextInput(attrs={'placeholder': 'Enter'}))

    Email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username','Email','password1','Email']


class profileCreationForm(UserCreationForm):
    first_name = forms.CharField(max_length=20)
    last_name = forms.CharField(max_length=20)
    phone_no = forms.CharField(max_length=20,required=False)
    address = forms.CharField(widget=forms.Textarea)
    email_id=forms.EmailField()
    Field=[("Engineer", "Engineer"),("Doctor","Doctor"),("Artist","Artist"),("Photographer","Photographer")]
    profession=forms.ChoiceField(choices=Field)
    Years=[(1,1),(2,2),(3,3),(4,4),(5,5)]
    experience=forms.ChoiceField(choices=Years)
    CHOICES = [('Female','Female'),('Male','Male')]
    gender = forms.ChoiceField(widget=forms.RadioSelect, choices=CHOICES)
    #photo=forms.ImageField()

    class Meta:
        model = User
        fields = ['first_name','last_name','gender','phone_no','address','email_id',
                    'password1', 'password2','profession','experience']

