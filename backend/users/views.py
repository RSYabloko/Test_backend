from users.services.profile import update_profile
from users.services.user import change_password, deactivate_account
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import logout
from django.shortcuts import render, redirect

@login_required
def settings_user(request):
    if request.method == 'POST':
        update_profile(request.user, request.POST)

        messages.success(request, 'Profile update')
        return redirect('users:settings')

    return render(request, 'users/settings.html')

@login_required
def change_password_view(request):
    if request.method == 'POST':
        old_password = request.POST.get('old_password')
        new_password = request.POST.get('new_password')
        new_password_repeat = request.POST.get('new_password_repeat')

        success, message = change_password(
                request.user,
                old_password,
                new_password,
                new_password_repeat
                )
        if not success:
            messages.error(request, message)
            return redirect('users:change_password')

        messages.success(request, message)
        return redirect('authorize:login')

    return render(request, 'users/edit_password.html')

@login_required
def deactivate_account_view(request):
    if request.method == 'POST':
        password = request.POST.get('password')
        success, message = deactivate_account(request.user, password)
        if not success:
            messages.error(request, message)
            return redirect('users/deactivate_account.html')

        logout(request)
        messages.success(request, message)
        return redirect('home')

    return render(request, 'users/deactivate_account.html')
