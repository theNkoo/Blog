from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'user'

urlpatterns = [
    path('register/', views.register,name = 'register'),
    path('login/', views.loginUser,name = 'loginUser'),
    path('logout/', views.logoutUser,name = 'logoutUser'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)