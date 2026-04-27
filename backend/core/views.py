from django.shortcuts import render

menu = [
        {'title': 'Home', 'url': 'home'},
        {'title': 'Login', 'url': 'login'},
        {'title': 'Register', 'url': 'register'},
        ]

def home(request):
    context = {
            'menu': menu,
            'title': 'Home',
            }
    return render(request, 'core/home.html', context=context)
