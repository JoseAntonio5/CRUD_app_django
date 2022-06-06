from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# MODELS
from .models import PostModel
from django.contrib.auth.models import User

# FORMS
from .forms import PostForm, registerUserForm

def loginUser(request):
    if request.method == 'POST':
        
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            request.session['user_id'] = user.id
            login(request, user)
            return redirect('posts')
        else:
            messages.error(request, "Incorrect username or password")
            return redirect('login')

    return render(request, 'login.html')

def registerUser(request):

    form = registerUserForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, "User has been created!")
            return redirect('login')

    return render(request, 'register.html', {'form': form})

def userPage(request, id):

    try:
        user = User.objects.get(id=id)
        posts = PostModel.objects.filter(author=user)
    except Exception or ObjectDoesNotExist:
        messages.error(request, "Error! User not found.")
        return redirect('error')

    return render(request, 'userPage.html', {'user': user, 'posts': posts})

def index(request):

    try:
        posts = PostModel.objects.all()
        user = User.objects.get(id=request.session.get('user_id'))
    except Exception or ObjectDoesNotExist:
        return render(request, 'index.html', {'posts': posts})

    return render(request, 'index.html', {'posts': posts, 'user': user})

@login_required
def createPost(request):
    
    form = PostForm(request.POST or None)
    user = User.objects.get(id=request.session.get('user_id'))

    if request.method == 'POST':

        if form.is_valid():
            post = form.save(commit=False)
            post.author = user
            post.save()
            messages.success(request, "New post has been created!")
            return redirect('posts')

    return render(request, 'newPost.html', {'form': form})

def viewPostDetails(request, id):

    try:
        post = PostModel.objects.get(id=id)
        user = User.objects.get(id=request.session.get('user_id'))
    except Exception or ObjectDoesNotExist:
        return render(request, 'details.html', {'post': post})

    return render(request, 'details.html', {'post': post, 'user': user})

@login_required
def updatePost(request, id):

    try:
        post = PostModel.objects.get(id=id)
        user = User.objects.get(id=request.session.get('user_id'))
    except ObjectDoesNotExist:
        messages.error(request, "Error, post not found")
        return redirect('error')

    if user != post.author:
        # TODO: RETURN TO ERROR PAGE
        return redirect('posts')

    if request.method == 'POST':
        try:
            post.title = request.POST['title']
            post.description = request.POST['description']
            post.save()
            messages.success(request, "Your post has been succesfully updated!")
            return redirect('/posts/' + id)
        except Exception:
            messages.error(request, "Error, post not found")
            return redirect('error')

    return render(request, 'update.html', {'post': post})

@login_required
def deletePost(request, id):

    try:
        post = PostModel.objects.get(id=id)
        user = User.objects.get(id=request.session.get('user_id'))
    except ObjectDoesNotExist:
        messages.error(request, "Error, post not found")
        return redirect('error')

    if user != post.author:
        # TODO: RETURN TO ERROR PAGE
        return redirect('posts')

    if request.method == 'POST':
        try:
            post.delete()
            messages.success(request, "Your post has been succesfully deleted!")
            return redirect('/posts')
        except Exception:
            messages.error(request, "Error, post not found")
            return redirect('error')

    return render(request, 'delete.html')

def errorPage(request):
    return render(request, 'error.html')

def logoutUser(request):
    try:
        logout(request)
        return redirect('login')
    except:
        messages.error(request, "Error.")
        return redirect('posts')