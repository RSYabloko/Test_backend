def user_roles(request):
    if not request.user.is_authenticated:
        return {'is_admin': False}
    return {'is_admin': request.user.groups.filter(name='admin').exists()}
