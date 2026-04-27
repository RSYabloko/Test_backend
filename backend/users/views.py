from django.shortcuts import render

menu = [
        {'title': 'Home', 'url': 'home'},
        {'title': 'Login', 'url': 'login'},
        {'title': 'Register', 'url': 'register'},
        ]

def index(request):
    context = {
            'menu': menu,
            }
    return render(request, 'core/home.html', context=context)
