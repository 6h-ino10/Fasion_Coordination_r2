from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.LoginView.as_view(), name = 'login'),
    path('signup/', views.SignupView.as_view(), name = 'signup'),
    path('signup_complete/', views.Signup_CompleteView.as_view(), name = 'signup_complete'),
]
