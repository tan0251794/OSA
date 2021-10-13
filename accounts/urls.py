#from accounts.views import account, home_view
from django.urls import path
from django.contrib.auth import views as auth_views
from rest_framework.authtoken.views import obtain_auth_token

from accounts.views import social_login

urlpatterns = [
    #path('create/', account , name='user form'),
    #path('log-in/', auth_views.LoginView.as_view(template_name='login.html')),
    #path('log-out/', auth_views.LogoutView.as_view(next_page='/accounts/')),
    #path('', home_view , name='home'),
    path('login/', obtain_auth_token, name='login'),
    # path('social-login/', social_login, name='social-login'),
]

