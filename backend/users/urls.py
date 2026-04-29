from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
        path('settings/', views.settings_user, name='settings'),
        path('change_password/', views.change_password_view, name='change_password'),
        path('deactivate_account/', views.deactivate_account_view, name='deactivate_account'),
        ]
