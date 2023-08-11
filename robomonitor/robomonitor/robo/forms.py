from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField
from django.contrib.auth import get_user_model as gum
from django import forms
from django.forms import ModelForm

from .models import Websites


class UserCreateForm(UserCreationForm):
    email = forms.EmailField(required=True)

    # def __init__(self, *args, **kwargs):
        # super(UserCreateForm, self).__init__(*args, **kwargs)

        #for fieldname in self.fields:
            #self.fields[fieldname].help_text = None
            #self.fields[fieldname].label = ""


class RegisterForm(UserCreateForm):
    class Meta:
        model = gum()
        fields = ("email", "password1", "password2")

    email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'Email',
                                                           }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password',
                                                                  }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password',
                                                                  }))

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])

        if commit:
            user.save()
        return user


class UserLoginForm(AuthenticationForm):
    #def __init__(self, *args, **kwargs):
        #super(UserLoginForm, self).__init__(*args, **kwargs)

        #for fieldname in self.fields:
            #self.fields[fieldname].help_text = None
            #self.fields[fieldname].label = ""

    username = UsernameField(widget=forms.TextInput(
        attrs={'placeholder': 'Email'}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'placeholder': 'Password',
        }))
    password2 = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'placeholder': 'Confirm Password',
        }))


class DNSCheckForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(DNSCheckForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'test'


class WebsiteCreationForm(ModelForm):
    # def __init__(self, *args, **kwargs):
    #     super(ModelForm, self).__init__(*args, **kwargs)
    #
    #     for fieldname in self.fields:
    #         self.fields[fieldname].help_text = None
    #         self.fields[fieldname].label = ""

    class Meta:
        model = Websites
        fields = ("domain", "checker_rate",)

    def clean(self):
        self.cleaned_data['verification_status'] = "NOT VERIFIED"
    #
    # domain = forms.CharField(widget=forms.TextInput(
    #     attrs={'class': 'form-control add-form', 'placeholder': 'Website'}))
