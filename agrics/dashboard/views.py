from django.shortcuts import render
from django.contrib.auth import authenticate, login
from .forms import UserLogin, UserRegistrationForm
from django.http import HttpResponse
from django.contrib import messages

# Create your views here.
def user_login(request):
    if request.method == 'POST':
        form = UserLogin(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request,
                                username=cd['username'],
                                password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Authenticated '\
                                        'successfully')
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
    else:
        form = UserLogin()
    return render(request, 'account/login.html', {'form': form})


def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
    # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
    # Set the chosen password
            new_user.set_password(
                user_form.cleaned_data['password'])
    # Save the User object
            new_user.save()
            messages.success(request, 'Account created successfully')
            return render(request,'account/register_done.html',{'new_user': new_user})
        else:
            messages.error(request, 'Error updating your profile')
    else:
        user_form = UserRegistrationForm()
    return render(request,'account/register.html',{'user_form': user_form})