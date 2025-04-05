from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile

class SignupUserForm(UserCreationForm):
    username = forms.CharField(
        required=True,
        widget=forms.widgets.TextInput(attrs={
            'class': 'form-control form-control-lg', 'placeholder': 'Username'
        }),
        label="",
        help_text='<span class="form-text text-muted"><small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</small></span>'
    )
    
    first_name = forms.CharField(
        required=True,
        widget=forms.widgets.TextInput(attrs={
            'class': 'form-control form-control-lg', 'placeholder': 'First Name'
        }),
        label=""
    )
    
    last_name = forms.CharField(
        required=True,
        widget=forms.widgets.TextInput(attrs={
            'class': 'form-control form-control-lg', 'placeholder': 'Last Name'
        }),
        label=""
    )
    
    email = forms.EmailField(
        required=True,
        widget=forms.widgets.EmailInput(attrs={
            'class': 'form-control form-control-lg', 'placeholder': 'Email'
        }),
        label=""
    )
    
    password1 = forms.CharField(
        required=True,
        widget=forms.widgets.PasswordInput(attrs={
            'class': 'form-control form-control-lg', 'placeholder': 'Password'
        }),
        label="",
        help_text='<ul class="form-text text-muted small"><li>Your password can\'t be too similar to your other personal information.</li><li>Your password must contain at least 8 characters.</li><li>Your password can\'t be a commonly used password.</li><li>Your password can\'t be entirely numeric.</li></ul>'
    )
    
    password2 = forms.CharField(
        required=True,
        widget=forms.widgets.PasswordInput(attrs={
            'class': 'form-control form-control-lg', 'placeholder': 'Confirm Password'
        }),
        label="",
        help_text='<span class="form-text text-muted"><small>Enter the same password as before, for verification.</small></span>'
    )
    
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')
        
class UserProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('image', )
        widgets = {
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'})
        }
        labels = {
            'image': ''
        }

class EditUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control form-control-lg', 'placeholder': 'Username'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control form-control-lg', 'placeholder': 'First name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control form-control-lg', 'placeholder': 'Last name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control form-control-lg', 'placeholder': 'Email'}),
        }
        labels = {
            'username': '',
            'first_name':  '',
            'last_name':  '',
            'email':  '',
        }