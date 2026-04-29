from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import get_user_model, login

User = get_user_model()

menu = [
        {'title': 'Home', 'url': 'home'},
        {'title': 'Login', 'url': 'login'},
        {'title': 'Register', 'url': 'register'},
        ]

def login_user(request):
    context = {
            'menu': menu,
            'title': 'Login',
            }

    if request.method == 'POST':
        email = request.POST.get('Email')
        password = request.POST.get('Password')

        try:
            user = User.objects.get(email = email)
        except User.DoesNotExist:
            messages.error(request, 'User not found')
            return redirect('login')

        if not user.check_password(password):
            messages.error(request, 'Password not correct')
            return redirect('login')

        login(request, user)

        messages.success(request, 'Loggin success')
        return redirect('home')

    return render(request, 'authorize/login.html', context = context)

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
