from django.contrib import admin
from .models import Article,Foto,Comment

# Register your models here.

@admin.register(Article)

class ArticalAdmin(admin.ModelAdmin):
    list_display = ['title','author','created_date']
    
    list_display_links = ['title','created_date']
    
    search_fields = ['title','created_date']

    list_filter=['created_date']

    class Meta:
        model = Article 

@admin.register(Foto)

class FotoAdmin(admin.ModelAdmin):
    list_display = ['title','owner','created_date']
    
    list_display_links = ['title','created_date']
    
    search_fields = ['title','created_date']

    list_filter=['created_date']

    class Meta:
        model = Foto

admin.site.register(Comment)


