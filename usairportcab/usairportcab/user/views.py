from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login
from .forms import LoginForm, UserRegistrationForm, UserEditForms, ProfileEditForms, CarFareEditForm, SiteSettingsForm
from django.contrib.auth.decorators import login_required
from .models import Profile
from usapp.models import Sites_common_detail, Car_fare
from django.contrib import messages

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'],
                                password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect('/user/dashboard/')
                else:
                    messages.error(request, 'Disabled account')

            else:
                messages.error(request, "Don't have account with this username and password please signup")

    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})


@login_required
def dashboard(request):
    profile = Profile.objects.get(user=request.user)
    sitecommondetails = get_object_or_404(Sites_common_detail, company_name=profile.companyname)
    carfare = Car_fare.objects.filter(site_name__company_name__contains=profile.companyname)
    return render(request, 'dashboard.html', {'sitecommondetails':sitecommondetails, 'profile':profile, 'carfare':carfare})


def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            # create a new user
            new_user = user_form.save(commit=False)
            #set the chosen password
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            profile = Profile.objects.create(user=new_user)
            msg = 'sucess'

    else:
        user_form = UserRegistrationForm()
        msg = ''
    return render( request,
                   'register.html',{'user_form': user_form, 'msg': msg})


@login_required
def edit(request):
    if request.method == 'POST':
        user_form = UserEditForms(instance=request.user,
                                  data=request.POST)

        profile_form = ProfileEditForms(instance=request.user.profile,
                                        data=request.POST,
                                        files=request.FILES)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Profile updated ' \
                                      'successfully')
        else:
            messages.error(request, 'Error updating your profile')
    else:
        user_form = UserEditForms(instance=request.user)
        profile_form = ProfileEditForms(instance=request.user.profile)

    return render(request, 'edit-user-details.html',{'user_form': user_form, 'profile_form': profile_form})

@login_required
def editfare(request, id):
    carfare = get_object_or_404(Car_fare, id=id)
    editform = CarFareEditForm(request.POST or None, instance=carfare)
    profile = Profile.objects.get(user=request.user)
    if request.method == 'POST':
        if editform.is_valid():
            new_editform = editform.save(commit=False)
            new_editform.site_name = Sites_common_detail.objects.get(company_name=profile.companyname)
            new_editform.save()
            messages.success(request, 'Car Fare Edited ' \
                                      'successfully')
            return HttpResponseRedirect('/user/dashboard/')
        else:
            messages.error(request, 'Error updating your Car Fare')
    return render(request, 'edit-fare.html', {'form': editform, 'id':id})

@login_required
def addfare(request):
    editform = CarFareEditForm(request.POST or None, request.FILES or None)
    profile = Profile.objects.get(user=request.user)
    if request.method == 'POST':
        if editform.is_valid():
            new_editform = editform.save(commit=False)
            new_editform.site_name = Sites_common_detail.objects.get(company_name=profile.companyname)
            new_editform.save()
            messages.success(request, 'Car Fare Added ' \
                                      'successfully')
            return HttpResponseRedirect('/user/dashboard/')
        else:
            messages.error(request, 'Error updating your Car Fare')
    return render(request, 'add-fare.html', {'form': editform})

@login_required
def deletecarfare(request, id):
    try:
        carfare = get_object_or_404(Car_fare, id=id)
        messages.success(request, 'Car Fare Deleted ' \
                                  'successfully')
    except:
        messages.error(request, 'Error while deleting row')
    carfare.delete()
    return HttpResponseRedirect('/user/dashboard/')

@login_required
def sitesettings(request):
    profile = Profile.objects.get(user=request.user)
    sitecommondetails = get_object_or_404(Sites_common_detail, company_name=profile.companyname)
    siteform = SiteSettingsForm(request.POST or None, request.FILES or None, instance=sitecommondetails)
    if request.method == 'POST':
        if siteform.is_valid():
            siteform.save()
            messages.success(request, 'Site settings updated sucessfully')
            return HttpResponseRedirect('/user/dashboard/')
        else:
            messages.error(request, 'Error whole updateing data. please try again')
    return render(request, 'edit-site-settings.html', {'form':siteform})

def forgetpassword(request):
    return render(request, 'forget-password.html')