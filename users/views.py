from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from .forms import LoginForm, SignupForm
from django.views.generic.edit import CreateView
from django.views.generic.base import TemplateView

# Create your views here.
class LoginView(LoginView, LoginForm):
    template_name = 'Login.html'

    def form_valid(self, form):
        response = super().form_valid(form)

        if not form.cleaned_data.get('remember_me'):
            self.request.session.set_expiry(0)
        else:
            self.request.session.set_expiry(1209600)
        return response
    
class SignupView(CreateView, SignupForm):
    template_name = 'signup.html'

    def form_valid(self, form):
        return super().form_valid(form)
    
    redirect('signup_complete')

class Signup_CompleteView(TemplateView):
    template_name = 'signup_complete.html'
