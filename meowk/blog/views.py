from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.forms import inlineformset_factory
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required


from .models import Post, Blogger
from .forms import PostForm, CreateUserForm, BloggerForm
from .decorators import unauthenticated_user, allowed_users


@unauthenticated_user
def register_user(request):

    form = CreateUserForm()

    if request.method == "POST":
        form = CreateUserForm(request.POST)

        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('usernmae')

            # group = Group.objects.get(name="blogger")
            # user.groups.add(group)
            # Blogger.objects.create(user=user, name=user.username)

            messages.success(request, "Account was successfully created")
            return redirect('login-user')

    context = {
        'form': form
    }
    return render(request, 'blog/register.html', context)


@unauthenticated_user
def login_user(request):

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, "Username or password is incorrect")

    context = {}
    return render(request, 'blog/login.html', context)


@login_required(login_url='login-user')
def logout_user(request):
    logout(request)
    return redirect('login-user')


@login_required(login_url='login-user')
def manage_post(request, pk):
    blogger = Blogger.objects.get(id=pk)
    posts = blogger.post_set.all()
    context = {
        'posts': posts
    }
    return render(request, 'blog/manage-post.html', context)


@login_required(login_url='login-user')
def account_settings(request):

    blogger = request.user.blogger

    form = BloggerForm(instance=blogger)

    if request.method == "POST":
        form = BloggerForm(request.POST, instance=blogger)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {
        'form': form
    }
    return render(request, 'blog/account-settings.html', context)


def home(request):
    posts = Post.objects.all().order_by('date_created',)[::-1]
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)


def post(request, pk):
    post = Post.objects.get(id=pk)
    context = {
        'post': post
    }
    return render(request, 'blog/post.html', context)


@login_required(login_url='login-user')
def create_post(request, pk):
    PostFormSet = inlineformset_factory(
        Blogger, Post, fields=('title', 'body', 'category', 'tags'), extra=1)
    blogger = Blogger.objects.get(id=pk)
    formset = PostFormSet(queryset=Post.objects.none(), instance=blogger)
    # form = PostForm(initial={'blogger': blogger})
    if request. method == 'POST':
        formset = PostFormSet(request.POST, instance=blogger)
        if formset.is_valid():
            formset.save()
            return redirect('home')
    context = {
        'formset': formset
    }
    return render(request, 'blog/create-post.html', context)


@login_required(login_url='login-user')
def update_post(request, pk):
    post = Post.objects.get(id=pk)
    form = PostForm(instance=post)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {
        'form': form
    }
    return render(request, 'blog/update-post.html', context)


@login_required(login_url='login-user')
def delete_post(request, pk):
    post = Post.objects.get(id=pk)
    if request.method == "POST":
        post.delete()
        return redirect('home')

    return render(request, 'blog/delete-post.html')
# def blogger(request, pk):
#     blogger = Blogger.objects.get(id=pk)
#     context = {
#         'blogger': blogger
#     }
#     return render(request, 'blog/blog.html', context)
