from django.shortcuts import redirect
from django.contrib.auth.views import LoginView, LogoutView
from .forms import LoginForm, SignupForm
from django.views.generic.edit import CreateView
from django.views.generic.base import TemplateView
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.http import HttpResponse

# Create your views here.
class LoginView(LoginView):
    template_name = 'login.html'
    form_class = LoginForm

    def form_valid(self, form):
        response = super().form_valid(form)

        if not form.cleaned_data.get('remember_me'):
            self.request.session.set_expiry(0)
        else:
            self.request.session.set_expiry(1209600)

        return response
    
class SignupView(CreateView):
    model = User
    template_name = 'signup.html'
    form_class = SignupForm
    success_url = reverse_lazy('signup_complete')

    def form_valid(self, form):
        response = super().form_valid(form)
        return redirect(self.success_url)


class Signup_CompleteView(TemplateView):
    template_name = 'signup_complete.html'

class LogoutView(LogoutView):
    template_name = 'logout.html'
