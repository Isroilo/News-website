from django.shortcuts import render,redirect
from dashboard.models import *
from django.contrib.auth.decorators import login_required


def index_view(request):
    context ={
        'small_news' : News.objects.all().order_by('-id')[1:4],
        'last_news': News.objects.last(),
        'category' : Category.objects.all(),
        'region' : Region.objects.all(),
        'news' : News.objects.all().order_by('-id')[4:8],
        'blogs': News.objects.all().order_by('-id')[8:]
    }
    return render(request,'front/index.html',context)


def search_view(request):
    title = request.GET.get("title")
    blog = News.objects.filter(title__icontains=title)
    context = {
        'blogs': blog,
        'category': Category.objects.all(),
        'region': Region.objects.all(),
    }
    return render(request, 'front/search.html', context)

def blog_view(request, pk):
        category = Category.objects.get(pk=pk)
        context = {
            'category': Category.objects.all(),
            'region': Region.objects.all(),
            'news_banner': News.objects.filter(category=category).order_by('-id')[:1],
            'news_four': News.objects.filter(category=category).order_by('-id')[1:4],
            'news': News.objects.filter(category=category).order_by('-id')[4:],
            'blog': category,
        }
        return render(request, 'front/blog.html', context)


def region_view(request,pk):
    region = Region.objects.get(pk=pk)
    context = {
        'category': Category.objects.all(),
        'region': Region.objects.all(),
        'news_banner': News.objects.filter(region=region).order_by('-id')[:1],
        'news_four': News.objects.filter(region=region).order_by('-id')[1:4],
        'news': News.objects.filter(region=region).order_by('-id')[4:],
    }
    return render(request, 'front/region.html', context)


def blog_detail_view(request,pk):
    blog = News.objects.get(pk=pk)
    comments = BlogComment.objects.filter(blog=blog)
    context ={
        'comments' : comments,
        'blog' : blog,
        'category': Category.objects.all(),
        'region': Region.objects.all(),
        'news': News.objects.filter(category=blog.category).order_by('-id')[:2],
    }
    return render(request, 'front/blog-detail.html', context)

@login_required(login_url='login_url')
def create_comment(request,pk):
    blog = News.objects.get(pk=pk)
    if request.method == 'POST':
        izox = request.POST['izox']
        BlogComment.objects.create(
                    text=izox,
                    user=request.user,
                    blog=blog,
                )
        return redirect('blog_detail_url',blog.pk)
    blog = News.objects.filter(pk=pk)
    return render(request, 'front/blog-detail.html', blog.pk)


def reply_comment(request,pk):
    if request.method == 'POST':
            reply = request.POST['izox']
            reply_id = request.POST['reply_id']
            blog = News.objects.get(pk=pk)
            reply_comment=BlogComment.objects.get(pk=reply_id)
            BlogComment.objects.create(
                text=reply,
                user=request.user,
                blog=blog,
                reply_comment=reply_comment,
                )
            return redirect('blog_detail_url',blog.id)
    blog = News.objects.filter(pk=pk)
    return render(request,'front/blog-detail.html',blog.pk)
