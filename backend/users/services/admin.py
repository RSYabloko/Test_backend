from django.shortcuts import render
from django.contrib.auth.decorators import login_required, user_passes_test
from users.services.permissions import check_admin

@login_required
@user_passes_test(check_admin)
def admin_panel(request):
    return render(request, 'users/admin_panel.html')
