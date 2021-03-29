from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'article'

urlpatterns = [
    path('dashboard/', views.dashboard,name = 'dashboard'),
    path('addarticle/', views.addArticle,name = 'addarticle'),
    path('article/<int:id>', views.detail,name = 'detail'),
    path('update/<int:id>', views.updateArticle, name = "update"),
    path('delete/<int:id>', views.deleteArticle,name = 'delete'),
    path('photo/', views.photo, name = 'photo'),
    path('addphoto/', views.addphoto, name = 'addphoto'),
    path('foto/<int:id>', views.detailF,name = 'detailF'),
    path('deletef/<int:id>', views.deletePhoto,name = 'deletef'),
    path('updatef/<int:id>', views.updatePhoto, name = "updatef"),
    path('', views.articles, name = 'articles'),
    path('photos/', views.photos, name = 'photos'),
    path('comment/<int:id>', views.addComment, name = 'comment'),
    path('addcomment/<int:id>', views.addComment2, name = 'addcomment'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)