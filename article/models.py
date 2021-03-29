from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

class Article(models.Model):
    author = models.ForeignKey('auth.User',on_delete=models.CASCADE,verbose_name='Yazar')
    title = models.CharField(max_length= 55,verbose_name='Başlık')
    content = RichTextField(verbose_name='İçerik')
    created_date = models.DateTimeField(auto_now_add=True,verbose_name='Oluşturulma Tarihi')
    article_image = models.FileField(blank=True,null=True,verbose_name='Makleye Fotograf ekle')
    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_date']


#class adPhoto(models.Model):
 #   owner = models.ForeignKey('auth.User', on_delete=models.CASCADE,verbose_name='Fotograf Sahibi')
  #  title = models.CharField(max_length= 55,verbose_name='Başlık')
   # created_date = models.DateTimeField(auto_now_add=True,verbose_name='Oluşturulma Tarihi')
    #article_image = models.FileField(blank=True,null=True,verbose_name='Fotograf Ekle')


class Foto(models.Model):
    owner = models.ForeignKey('auth.User',on_delete=models.CASCADE,verbose_name='Yazar')
    title = models.CharField(max_length= 55,verbose_name='Başlık')
    created_date = models.DateTimeField(auto_now_add=True,verbose_name='Oluşturulma Tarihi')
    article_image = models.FileField(blank=True,null=True,verbose_name='Makleye Fotograf ekle')
    


class Comment(models.Model):
    article = models.ForeignKey(Article,on_delete = models.CASCADE,verbose_name='Yorum',related_name='comments')
    comment_author = models.CharField(max_length=50,verbose_name='Yorumcu')
    comment_content = models.CharField(max_length=500,verbose_name='Yorum İçeriği')
    comment_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comment_content

    class Meta:
        ordering = ['-comment_date']
