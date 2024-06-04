#from django.contrib.auth.backends import BaseBackend
from customer.models import MyUserCustomer

class CustomUserModelBackend:
    def authenticate(self, request, username=None, password=None, **kwargs):

        # Try to authenticate the user as a Customer
        try:
            user = MyUserCustomer.objects.get(email=username)
            if user.check_password(password):
                return user
        except MyUserCustomer.DoesNotExist:
            pass
    def get_user(self, user_id):
        # Try to get the user by ID


        try:
            return MyUserCustomer.objects.get(pk=user_id)
        except MyUserCustomer.DoesNotExist:
            pass

        # If the user does not exist, return None
        return None