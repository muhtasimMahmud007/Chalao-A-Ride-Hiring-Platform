#from django.contrib.auth.backends import BaseBackend
from employee.models import MyUserEmployee

class CustomUserModelBackend:
    def authenticate(self, request, username=None, password=None, **kwargs):

        # Try to authenticate the user as an Employee
        try:
            user = MyUserEmployee.objects.get(email=username)
            if user.check_password(password):
                return user
        except MyUserEmployee.DoesNotExist:
            pass

        return None
    def get_user(self, user_id):
        # Try to get the user by ID

        try:
            return MyUserEmployee.objects.get(pk=user_id)
        except MyUserEmployee.DoesNotExist:
            pass

        # If the user does not exist, return None
        return None
