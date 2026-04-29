def update_profile(user, data):
    user.first_name = data.get('first_name')
    user.middle_name = data.get('middle_name')
    user.last_name = data.get('last_name')
    user.email = data.get('email')
    user.save()
