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

def register_user(email, password, confirm_password):
    if len(password) < 8:
        return False, 'Password must be least 8 simbols'

    if password != confirm_password:
        return False, 'Error password repeat'

    if User.objects.filter(email=email).exists():
        return False, 'User exists'

    return True, 'Success'

