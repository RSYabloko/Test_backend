from django.contrib.auth import get_user_model

User = get_user_model()

def auth_user(email, password):
    try:
        user = User.objects.get(email = email)
    except User.DoesNotExist:
        return False, 'User not found'
    
    if not user.is_active:
        return False, 'User deactivate'

    if not user.check_password(password):
        return False, 'Incorrect password'
    
    return user, 'Success'
