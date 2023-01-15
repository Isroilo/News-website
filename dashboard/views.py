from django.shortcuts import render,redirect
from .models import *

def create_blog(request):
    if request.method == 'POST':
        title = request.POST['title']
        text = request.POST['text']
        mini_text = request.POST['mini_text']
        category = request.POST.get("category")
        region = request.POST.get("region")
        img = request.FILES.getlist('img')
        new_blog = News.objects.create(
            title=title,
            text=text,
            mini_text=mini_text,
            category_id=category,
            user=request.user,
            region_id=region
        )
        try:
            for photo in img:
                img = Newsphoto.objects.create(
                    img=photo
                )
                new_blog.img.add(img)
                new_blog.save()
        except:
            pass
        return redirect('blog_detail_url', new_blog.pk)
    context = {
        'region' : Region.objects.all(),
        'category':Category.objects.all()
    }
    return render(request, 'dashboard/blog-create.html',context)


def update_blog(request,pk):
    blog = News.objects.get(pk=pk)
    if request.method == 'POST':
        blog = News.objects.get(pk=pk)
        title = request.POST['title']
        text = request.POST['text']
        mini_text = request.POST['mini_text']
        category_id = request.POST['category']
        img = request.FILES.get('img')
        category = Category.objects.get(id=category_id)
        blog.title = title
        blog.category = category
        blog.text = text
        blog.mini_text = mini_text
        blog.category = category
        if img is not None:
            try:
                for photo in img:
                    img = Newsphoto.objects.create(
                        img=photo
                    )
                    blog.img.add(img)
                    blog.save()
            except:
                blog.img.add(img)
        else:
            pass
        print(blog.img)
        return redirect('blog_detail_url', blog.pk)
    context = {
        'blog' : blog,
        'category': Category.objects.all()
    }
    return render(request,'dashboard/update-blog.html',context)


def delete_blog(request,pk):
    blog = News.objects.get(pk=pk)
    blog.delete()
    return redirect('user_detail_url',blog.pk)

def user_detail(request, pk):
    user = User.objects.get(pk=pk)
    blogs = News.objects.filter(user=user)
    context = {
        'user':user,
        'blogs':blogs
    }
    return render(request, 'dashboard/user-detail.html', context)


def user_update(request, pk):
    user = User.objects.get(pk=pk)
    if request.method == 'POST':
        user = User.objects.get(pk=pk)
        username = request.POST['username']
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        bio = request.POST['bio']
        staff = request.POST.get('staff')
        avatar = request.FILES.get('avatar')
        password = request.POST.get('password')
        password_confirm = request.POST.get('password_confirm')
        user.username = username
        user.first_name = first_name
        user.last_name = last_name
        user.email = email
        user.bio = bio
        print(staff)
        if staff is not None:
            user.is_staff = True
            user.save()
        else:
            user.is_staff = True
            user.save()
        if avatar is not None:
            user.avatar = avatar
        if password is not None:
            if password == password_confirm:
                user.set_password(password)
            else:
                pass
        user.save()
        return redirect('user_detail_url', user.pk)
    context = {
        'user':user
    }
    return render(request, 'dashboard/user-update.html', context)

def user_delete(request, pk):
    user = User.objects.get(pk=pk)
    user.delete()
    return render(request,'index.html')


def users_view(request):
    context = {
        'category': Category.objects.all(),
        'region': Region.objects.all(),
        'users': User.objects.all(),
    }
    return render(request,'dashboard/users.html',context)

def search_user_view(request):
    username = request.GET.get("username")
    print(username)
    users = User.objects.filter(username__icontains=username)
    context = {
        'users': users,
        'category': Category.objects.all(),
        'region': Region.objects.all(),
    }
    return render(request, 'dashboard/search-users.html', context)