from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views
from core.views import home, SignupView, login_view, logout, HomeView
from rest_framework.authtoken import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView



   



urlpatterns = [
    path('admin/', admin.site.urls),
  
    # 3rd party apps
    path('api-auth/', include('rest_framework.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls')),
    path('api-token-auth/', views.obtain_auth_token),
    path('accounts/', include('allauth.urls')),

    #Custom URLS
    path('', home, name='home'),
    path('json/', HomeView.as_view(), name='home-json'),
    path('signup', SignupView.as_view(), name='signup'),
    path('login', login_view, name='login'),
    path('logout', logout, name='logout'),
    #Built in Django Auth
    #path('accounts/', include('django.contrib.auth.urls')),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
