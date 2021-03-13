
from django.contrib.auth.mixins import LoginRequiredMixin


class LoginMixin(LoginRequiredMixin):
    login_url = '/login'
    redirect_field_name = 'redirect_to'
