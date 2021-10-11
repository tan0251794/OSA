from django.conf.urls.static import static  
from django.conf import settings 
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from rest_framework.authtoken.views import obtain_auth_token

import purchase_app.api.urls
import purchase_app.urls
import accounts.urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/', include(purchase_app.api.urls), name='purchase_api'),
    #ui
    path('', include(purchase_app.urls), name='cms'),
    #authentication
    path('user/', include(accounts.urls), name='user'),
    # path('', auth_views.LoginView.as_view(template_name='login.html')),
    # path('log-out', auth_views.LogoutView.as_view(next_page='/')),
    path('accounts/', include('allauth.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
