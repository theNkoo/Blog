from django import forms
from .models import Article,Foto


class ArticleForms(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title','content','article_image']

class FotoForms(forms.ModelForm):
    class Meta:
        model = Foto
        fields = ['title','article_image']
