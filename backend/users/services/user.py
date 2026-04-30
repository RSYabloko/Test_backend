from django.contrib.auth.decorators import login_required

@login_required
def change_password(user, old_password, new_password, new_password_repeat):
    if len(new_password) < 8:
        return False, 'Password must be least 8 symbols'

    if new_password != new_password_repeat:
        return False, 'Repeat password incorrect'

    user.set_password(new_password)
    user.save()

    return True, 'Password updated'

@login_required
def deactivate_account(user, password):
    if not user.check_password(password):
        return False, 'Incorrect password'
    
    user.is_active = False
    user.save(update_fields=['is_active'])
    return True, 'Account deactivated'
