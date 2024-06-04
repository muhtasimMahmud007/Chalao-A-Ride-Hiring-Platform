#from django.contrib.auth.backends import BaseBackend
from owner.models import MyUser



class CustomUserModelBackend:
    def authenticate(self, request, username=None, password=None, **kwargs):
        # Try to authenticate the user as an Owner
        try:
            user = MyUser.objects.get(email=username)
            if user.check_password(password):
                return user
        except MyUser.DoesNotExist:
            pass
        return None
    def get_user(self, user_id):
        # Try to get the user by ID
        try:
            return MyUser.objects.get(pk=user_id)
        except MyUser.DoesNotExist:
            pass
        return None
