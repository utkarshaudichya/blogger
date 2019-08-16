from django import forms
from django.contrib.auth.models import User
from .models import Profile, PermanentAddress, CorrespondenceAddress
from django.contrib.auth.models import User

class UserLoginForm(forms.Form):
    username = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder':'username or email address'}))
    password = forms.CharField(required=True, widget=forms.PasswordInput(attrs={'placeholder':'password'}))
    # def clean(self):
    #     username = self.cleaned_data['username']
    #     email = (True if username.find('@')!=-1 else False)
    #     if email:
    #         username = User.objects.get(email=username).username
    #     user = User.objects.get(username__iexact=username)
    #     if not user:
    #         raise User.DoesNotExist("User credentials does not matched")
    #     password = self.cleaned_data['password']
    #     valid = user.check_password(password)
    #     if not valid:
    #         raise forms.ValidationError("User credentials does not matched")
    #     return


class UserRegistrationForm(forms.ModelForm):
    confirm_password = forms.CharField(label='Password', required=True, widget=forms.PasswordInput(attrs={'placeholder':'Confirm Password'}))
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password')
        help_texts = {'username': None}
        widgets = {
            'username': forms.TextInput(attrs={'placeholder':'Username'}),
            'first_name': forms.TextInput(attrs={'placeholder':'First name', 'required':'required'}),
            'last_name': forms.TextInput(attrs={'placeholder':'Last name'}),
            'email': forms.EmailInput(attrs={'placeholder':'Email', 'required':'required'}),
            'password': forms.PasswordInput(attrs={'placeholder':'Password'}),
        }
    def clean_confirm_password(self):
        password = self.cleaned_data['password']
        confirm_password = self.cleaned_data['confirm_password']
        if password != confirm_password:
            raise forms.ValidationError('Both Password must be Matched')
        else:
            return confirm_password

class PermanentAddressForm(forms.ModelForm):
    class Meta:
        model = PermanentAddress
        fields = ('street_address', 'city', 'state', 'pincode', 'country')
        widgets = {
            'street_address': forms.TextInput(attrs={'placeholder':'Street Address'}),
            'city': forms.TextInput(attrs={'placeholder':'City'}),
            'state': forms.TextInput(attrs={'placeholder':'State'}),
            'pincode': forms.NumberInput(attrs={'placeholder':'Pincode'}),
            'country': forms.TimeInput(attrs={'placeholder':'Country'}),
        }

class CorrespondenceAddressForm(forms.ModelForm):
    class Meta:
        model = CorrespondenceAddress
        fields = ('street_address', 'city', 'state', 'pincode', 'country')
        widgets = {
            'street_address': forms.TextInput(attrs={'placeholder':'Street Address'}),
            'city': forms.TextInput(attrs={'placeholder':'City'}),
            'state': forms.TextInput(attrs={'placeholder':'State'}),
            'pincode': forms.NumberInput(attrs={'placeholder':'Pincode'}),
            'country': forms.TimeInput(attrs={'placeholder':'Country'}),
        }

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('phone', 'gender', 'birth_date')
        widgets = {
            'phone': forms.NumberInput(attrs={'placeholder':'Phone Number'}),
            'gender': forms.RadioSelect(attrs={'default':'male'}),
        }
class ImageForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('profile_pic',)

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')
        help_texts = {'username': None}
        widgets = {
            'username': forms.TextInput(attrs={'placeholder':'Username'}),
            'first_name': forms.TextInput(attrs={'placeholder':'First name', 'required':'required'}),
            'last_name': forms.TextInput(attrs={'placeholder':'Last name'}),
            'email': forms.EmailInput(attrs={'placeholder':'Email', 'required':'required'}),
            'password': forms.PasswordInput(attrs={'placeholder':'Password'}),
        }
