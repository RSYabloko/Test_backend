from django.shortcuts import render

menu = [
        {'title': 'Home', 'url': 'home'},
        {'title': 'Login', 'url': 'login'},
        {'title': 'Register', 'url': 'register'},
        ]

def login(request):
    context = {
            'menu': menu,
            'title': 'Login',
            }
    return render(request, 'authorize/login.html', context=context)

def register(request):
    context = {
            'menu': menu,
            'title': 'Register',
            }
    return render(request, 'authorize/register.html', context=context)
