from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import get_user_model, login, logout

from authorize.services.auth import auth_user

User = get_user_model()

menu = [
        {'title': 'Home', 'url': 'home'},
        {'title': 'Login', 'url': 'login'},
        {'title': 'Register', 'url': 'register'},
        ]

def login_user(request):
    if request.method == 'POST':
        email = request.POST.get('Email')
        password = request.POST.get('Password')

        user, message = auth_user(email, password)

        if not user:
            messages.error(request, message)
            return redirect('authorize:login')

        login(request, user)

        messages.success(request, 'Loggin success')
        return redirect('home')

    return render(request, 'authorize/login.html')

def logout_user(request):
    logout(request)
    return redirect('home')

def register(request):
    context = {
            'menu': menu,
            'title': 'Register',
            }
    if request.method == 'POST':
        email = request.POST.get('Email')
        first_name = request.POST.get('First name')
        middle_name = request.POST.get('Middle name')
        last_name = request.POST.get('Last name')
        password = request.POST.get('Password')
        confirm_password = request.POST.get('Confirm password')

        if len(password) < 8:
            return render(request, 'authorize/register.html', {'menu': menu, 'title': 'Register', 'error': 'Password must be least 8 simbols'})

        if password != confirm_password:
            return render(request, 'authorize/register.html', {'menu': menu, 'title': 'Register', 'error': 'Password error'})

        if User.objects.filter(email=email).exists():
            return render(request, 'authorize/register.html', {'menu': menu, 'title': 'Register', 'error': 'User exists'})

        user = User.objects.create(
                email = email,
                first_name = first_name,
                middle_name = middle_name,
                last_name = last_name
            )
        user.set_password(password)
        user.save()

        messages.success(request, 'Register successful')

    return render(request, 'authorize/register.html', context = context)
