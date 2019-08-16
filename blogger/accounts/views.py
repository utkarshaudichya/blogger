from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import Profile, PermanentAddress, CorrespondenceAddress
from .forms import UserLoginForm, UserRegistrationForm, UserForm, ProfileForm, PermanentAddressForm, CorrespondenceAddressForm, ImageForm
from django.contrib.auth import authenticate, login, logout
from django.forms import ValidationError

# Create your views here.
def userLogin(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            email = (True if username.find('@')!=-1 else False)
            if email:
                username = User.objects.get(email=username).username
            user = authenticate(username=username, password=password)
            if user:
                status = True
                if user.is_active:
                    login(request, user)
                    return redirect('blog:home')
                else:
                    return render(request, 'accounts/login.html', {'form':form})
            else:
                return render(request, 'accounts/login.html', {'form':form})
        else:
            return render(request, 'accounts/login.html', {'form':form})
    else:
        form = UserLoginForm()
        return render(request, 'accounts/login.html', {'form':form})

def userLogout(request):
    logout(request)
    return redirect('blog:home')

def userRegister(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.set_password(form.cleaned_data['password'])
            form.save()
            permanent_address = PermanentAddress.objects.create(user=new_user)
            correspondence_address = CorrespondenceAddress.objects.create(user=new_user)
            profile = Profile.objects.create(user=new_user,
                                            permanent_address = permanent_address,
                                            correspondence_address = correspondence_address)
            profile.save()
            return redirect('accounts:login')
    else:
        form = UserRegistrationForm()
    return render(request, 'accounts/signup.html', {'form':form})

def userProfileEdit(request):
    if request.method == 'POST':
        pic = request.user.profile.profile_pic
        user_form = UserForm(data=request.POST or None, instance=request.user)
        user_profile = ProfileForm(data=request.POST or None, instance=request.user.profile)
        image_porfile = ImageForm(data=request.POST or None , instance=request.user.porfile, files=request.FILES)
        user_perma_address = PermanentAddressForm(data=request.POST or None, instance=request.user.permanent_address)
        user_cores_address = CorrespondenceAddressForm(data=request.POST or None, instance=request.user.correspondence_address)
        if user_form.is_valid() and user_profile.is_valid() and user_perma_address.is_valid() and user_cores_address.is_valid():
            user_form.save()
            user_profile.save()
            user_perma_address.save()
            user_cores_address.save()
        return render(request, 'accounts/user_profile.html', {'user_form':user_form, 'user_profile':user_profile, 'user_perma_address':user_perma_address, 'user_cores_address':user_cores_address, 'pic':pic})
    else:
        pic = request.user.profile.profile_pic
        user_form = UserForm(instance=request.user)
        user_profile = ProfileForm(instance=request.user.profile)
        image_porfile = ImageForm(instance=request.user.profile)
        user_perma_address = PermanentAddressForm(instance=request.user.permanent_address)
        user_cores_address = CorrespondenceAddressForm(instance=request.user.correspondence_address)
        return render(request, 'accounts/edit_profile.html', {'user_form':user_form, 'user_profile':user_profile, 'user_perma_address':user_perma_address, 'user_cores_address':user_cores_address, 'pic':pic, 'image_profile':image_porfile})

def userProfile(request):
    pic = request.user.profile.profile_pic
    user_form = User.objects.get(username=request.user.username)
    user_profile = Profile.objects.get(user=request.user)
    user_perma_address = PermanentAddress.objects.get(user=request.user)
    user_cores_address = CorrespondenceAddress.objects.get(user=request.user)
    return render(request, 'accounts/user_profile.html', {'user_form':user_form, 'user_profile':user_profile, 'user_perma_address':user_perma_address, 'user_cores_address':user_cores_address, 'pic':pic})

def deleteUserAccount(request):
    user = User.objects.get(id=request.user.id)
    user.delete()
    return redirect('blog:home')
