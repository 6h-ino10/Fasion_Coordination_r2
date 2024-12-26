from django.contrib import admin
from django.urls import path,include
from users import views

urlpatterns = [
    path('', views.LoginView.as_view(), name = 'login'),
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    #path('coordination_app/', include('coordination_app.urls')),
]
