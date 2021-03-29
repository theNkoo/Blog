from django.shortcuts import render,HttpResponse,redirect,get_object_or_404,reverse
from .froms import ArticleForms,FotoForms
from django.contrib import messages
from .models import Article,Foto,Comment
from django.contrib.auth.decorators import login_required
# Create your views here.

def articles(request):

    #keyword = request.Get.get('keyword')
    #if keyword:
    #    articles = Article.objects.all(title__contains = keyword)
    #    return render(request,'articles.html',{'articles':articles})
   
    articles = Article.objects.all()
    

    return render(request,'articles.html',{'articles':articles})



def index(request):
    
    return render(request,'index.html')
    
    

def article(request):
    return render(request,('index'))

@login_required(login_url = 'user:loginUser')
def dashboard(request):
    articles = Article.objects.filter(author = request.user)
    context = {
        'articles':articles
    }
    
    return render(request,'dashboard.html',context)

@login_required(login_url= 'user:loginUser')
def addArticle(request):
    form = ArticleForms(request.POST or None,request.FILES or None)
    if form.is_valid():
        article = form.save(commit=False)
        article.author = request.user
        article.save()

        messages.success(request,'Yazmış Oldugunuz Yazı Başarıyla Kaydedildi')
        return redirect('index')

    return render(request,('addarticle.html'),{'form':form})

def detail(request,id):
    #article = Article.objects.filter(id = id).first()
    article = get_object_or_404(Article,id = id)
    comments = article.comments.all()
    return render(request,'detail.html',{'article':article,'comments':comments})


@login_required(login_url= 'user:loginUser')
def updateArticle(request,id):
    
    article = get_object_or_404(Article,id = id)
    form = ArticleForms(request.POST or None,request.FILES or None,instance= article)
    if form.is_valid():

        article = form.save(commit=False)
        article.author = request.user
        article.save()
        messages.success(request,'Makale Başarıyla Güncellendi')
        return redirect('index')

    return render(request,'update.html',{'form':form})



@login_required(login_url= 'user:loginUser')
def deleteArticle(request,id):
    article = get_object_or_404(Article,id = id)
    article.delete()
    messages.warning(request,'Dosya Başarıyla Silindi')

    return redirect('article:dashboard')



@login_required(login_url= 'user:loginUser')
def photo(request):
    articles = Foto.objects.filter(owner = request.user)
   
    context = {
        'articles':articles
    }
    
    return render(request,('photo.html'),context)



@login_required(login_url= 'user:loginUser')
def addphoto(request):
    form = FotoForms(request.POST or None,request.FILES or None)
    if form.is_valid():
        foto = form.save(commit=False)
        foto.owner = request.user
        foto.save()

        messages.success(request,'Yazmış Oldugunuz Yazı Başarıyla Kaydedildi')
        return redirect('article:photo')
    return render(request,('addphoto.html'),{'form':form})




@login_required(login_url= 'user:loginUser')
def detailF(request,id):
    #article = Article.objects.filter(id = id).first()
    article = get_object_or_404(Foto,id = id)
    return render(request,'detailF.html',{'article':article})


@login_required(login_url= 'user:loginUser')
def deletePhoto(request,id):
    shot = get_object_or_404(Foto,id=id)

    shot.delete()
    messages.warning(request,'Fotograf Başarıyla Silindi')

    return redirect('article:photo')


@login_required(login_url= 'user:loginUser')
def updatePhoto(request,id):
    article = get_object_or_404(Foto,id = id)
    form = FotoForms(request.POST or None,request.FILES or None,instance= article)
    if form.is_valid():

        article = form.save(commit=False)
        article.owner = request.user
        article.save()
        messages.success(request,'Makale Başarıyla Güncellendi')
        return redirect('index')

    return render(request,'update.html',{'form':form})

def photos(reqeust):

    articles = Foto.objects.all()
    

    return render(reqeust,'photos.html',{'articles':articles})


def addComment(request,id):

    article = get_object_or_404(Article,id=id)
    if request.method == 'POST':
        comment_author = request.POST.get('comment_author')
        comment_content = request.POST.get('comment_content')
        newComment = Comment(comment_author = comment_author,comment_content=comment_content)
        newComment.article = article
        newComment.save()
    
    return redirect(reverse('article:detail',kwargs={'id':id}))


def addComment2(request,id):
    article = get_object_or_404(Article,id=id)
    if request.method == 'POST':
        comment_author = request.POST.get('comment_author')
        comment_content = request.POST.get('comment_content')
        newComment = Comment(comment_author = comment_author,comment_content=comment_content)
        newComment.article = article
        newComment.save()
    
    #return redirect(reverse('article:detail',kwargs={'id':id}))
        pass


