def user_roles(request):
    if not request.user.is_authenticated:
        return {'check_admin': False}
    return {'check_admin': request.user.groups.filter(name='admin').exists()}
