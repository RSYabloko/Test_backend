from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import get_user_model, login, logout
from django.contrib.auth.models import Group

from authorize.services.auth import auth_user, register_user

User = get_user_model()

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
    if request.method == 'POST':
        email = request.POST.get('Email')
        first_name = request.POST.get('First name')
        middle_name = request.POST.get('Middle name')
        last_name = request.POST.get('Last name')
        password = request.POST.get('Password')
        confirm_password = request.POST.get('Confirm password')

        answer, message = register_user(email, password, confirm_password)

        if not answer:
            messages.error(request, message)
            return redirect('authorize:register')

        user = User.objects.create(
                email = email,
                first_name = first_name,
                middle_name = middle_name,
                last_name = last_name
            )
        user.set_password(password)
        user.save()

        group, _ = Group.objects.get_or_create(name='user')
        user.groups.add(group)
        messages.success(request, 'Register successful')

    return render(request, 'authorize/register.html')
