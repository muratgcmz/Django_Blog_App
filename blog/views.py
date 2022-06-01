from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm
# Create your views here.
def post_list(request):
    posts = Post.objects.all()
    context = {
        'posts': posts 
    }

    return render(request, 'blog/post_list.html', context)

def post_create(request):
    form = PostForm(request.POST or None)
    if form.is_valid():
        postTemp = form.save()
        if 'image' in request.FILES:
            postTemp.image = request.FILES.get('image')
            postTemp.save()
        return redirect('home')
    context = {
        'form': form
    }
    
    return render(request, 'blog/post_create.html', context)

def post_update(request, id):
    post = Post.objects.get(id=id)
    form = PostForm(request.POST or None, request.FILES or None, instance=post)
    if form.is_valid():
        form.save()
        return redirect('home')
    context = {
        'form': form
    }
    
    return render(request, 'blog/post_update.html', context)

    