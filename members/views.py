from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.sites import requests
from django.shortcuts import render, redirect
import requests
import ssl


import choices_functions as c_and_f
from members.forms import RegisterUserForm
from private.hidden import SERVER_URL_HIDDEN
from streaming import templates as temps

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
        url = f'https://{SERVER_URL_HIDDEN}/api/token-auth/'

        # Create a session
        session = requests.Session()
        session.mount('https://', requests.adapters.HTTPAdapter(max_retries=3))
        session.verify = False  # Warning: Disabling SSL verification has security implications

        username = request.POST.get('username')
        password = request.POST.get('password')

        data = {
            'username': username,
            'password': password
        }

        try:
            response = session.post(url, json=data, timeout=5)
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                # Redirect to a success page.
                messages.success(request, 'Successful Login ! ')
                if response.status_code == 200:
                    token = response.json().get('token')
                    print(f"Login successful. Token: {token}")
                return render(request, HOME, {})
            else:
                messages.error(request, 'ERROR: No username or password, please try again..')
                print(f"Login failed with status code: {response.status_code}")
                return render(request, 'authenticate/login_user.html', {})
        except requests.exceptions.RequestException as e:
            print(f"Request exception: {e}")
        finally:
            session.close()

    return render(request, 'members/login_user.html', {})

    # return render(request, 'authenticate/login_user.html', {})


def logout_view(request):
    logout(request)
    # Redirect to a success page.
    # print('Logout was Successful. Thanks for being a member of Django-Stream!')
    messages.success(request, 'Logout was Successful !')
    return redirect('streaming:home')
