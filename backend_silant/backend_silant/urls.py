from django.contrib import admin
from django.urls import path, include
from dj_rest_auth.views import LoginView, LogoutView
from silant.views import CustomUserDetailsView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('api/', include('silant.urls')),
    path('api/v1/login/', LoginView.as_view(), name='rest_login'),
    path('api/v1/logout/', LogoutView.as_view(), name='rest_logout'),
    path('api/v1/user/', CustomUserDetailsView.as_view(), name='user_details'),
]
