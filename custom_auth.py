from django.contrib.auth.backends import BaseBackend
from owner.models import MyUser
from customer.models import MyUserCustomer
from employee.models import MyUserEmployee

class CustomUserModelBackend(BaseBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        # Try to authenticate the user as an Owner
        try:
            user = MyUser.objects.get(username=username)
            if user.check_password(password):
                return user
        except MyUser.DoesNotExist:
            pass

        # Try to authenticate the user as a Customer
        try:
            user = MyUserCustomer.objects.get(username=username)
            if user.check_password(password):
                return user
        except MyUserCustomer.DoesNotExist:
            pass

        # Try to authenticate the user as an Employee
        try:
            user = MyUserEmployee.objects.get(username=username)
            if user.check_password(password):
                return user
        except MyUserEmployee.DoesNotExist:
            pass

        # If authentication has not succeeded, return None
        return None

    def get_user(self, user_id):
        # Try to get the user by ID
        try:
            return MyUser.objects.get(pk=user_id)
        except MyUser.DoesNotExist:
            pass

        try:
            return MyUserCustomer.objects.get(pk=user_id)
        except MyUserCustomer.DoesNotExist:
            pass

        try:
            return MyUserEmployee.objects.get(pk=user_id)
        except MyUserEmployee.DoesNotExist:
            pass

        # If the user does not exist, return None
        return None
