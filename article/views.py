from django.shortcuts import render,redirect,get_object_or_404
from .models import Article
from .forms import ArticleForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
def home_view(request):
    return render(request, "index.html")

def about_view(request):
    return render(request, "about.html")

def contact_view(request):
    return render(request, "contact.html")

@login_required(login_url = "account:login")
def articles_view(request):
    articles = Article.objects.all()
    return render(request, "articles.html", {'articles':articles})

@login_required(login_url = "account:login")
def article_details_view(request,id):
    # article = Article.objects.filter(id = id).first()
    article = get_object_or_404(Article,id = id)
    context =  {"article":article}
    return render(request, "article-details.html",context)

@login_required(login_url = "account:login")
def dashboard_view(request):
    articles = Article.objects.filter(author = request.user)
    return render(request, "dashboard.html", {'articles':articles})

@login_required(login_url = "account:login")
def add_articles_view(request):
    form = ArticleForm(request.POST or None ,request.FILES or None)

    if form.is_valid():
        article = form.save(commit=False)
        article.author = request.user
        article.save()

        messages.success(request,"Məqaləniz uğurla əlavə olundu...")
        return redirect("dashboard")

    context = {"form":form}
    return render(request, "addarticles.html",context)