def check_admin(user):
    return user.groups.filter(name='admin').exists()
