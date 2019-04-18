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
    # path('user_create/', view.UserCreate.as_view(), name = 'user_create'),
    # path('user_create/done',view.UserCreateDone.as_view(), name = 'user_create_done'),
    # path('user_create/complete/<token>/', views.UserCreateComplete.as_view(), name = 'user_create_complete'),
]
