from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect

import choices_functions as c_and_f
from members.forms import RegisterUserForm

HOME = 'streaming:home'


def register_user(request):
    states = c_and_f.STATES
    regions = c_and_f.CONTINENTS
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            messages.success(request, 'Registration was Successful')
            login(request, user)
            messages.success(request, 'Registration was Successful, Thank you for Joining Us!')
            return redirect(HOME)
    else:
        form = RegisterUserForm()
    return render(request, 'members/register_user.html',
                  {'states': states, 'regions': regions, 'form': form})


def login_user(request):
    if request.method == 'POST':
        username = request.POST['Username']
        password = request.POST['Password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Successful Login!')
            return redirect(HOME)  # Redirect to the home page
        else:
            messages.error(request, 'ERROR: No username or password, please try again..')
            return render(request, 'members/login_user.html')  # Correct path to your login template
    else:
        return render(request, 'members/login_user.html')  # Correct path to your login template


def logout_view(request):
    logout(request)
    # Redirect to a success page.
    # print('Logout was Successful. Thanks for being a member of Django-Stream!')
    messages.success(request, 'Logout was Successful !')
    return redirect('streaming:home')
