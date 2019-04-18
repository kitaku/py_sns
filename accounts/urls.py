from django.urls import path
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView
# from .views import SignUp

from accounts import views as accounts_views

urlpatterns = [
    path('', TemplateView.as_view(template_name='accounts/top.html'), name='top'),
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/',accounts_views.signup, name = 'signup'),
]
