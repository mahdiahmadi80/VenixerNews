from django.shortcuts import redirect, render,get_object_or_404
from .models import Post,Comment
from django.db.models import Q
from .forms import CommentForm
from django.contrib import messages

def blog(request,**kwargs):

    posts=Post.objects.filter(active=1)
    if kwargs.get('cat'):
        posts=posts.filter(category__title=kwargs['cat'])

    if kwargs.get('author'):
        posts=posts.filter(author__username=kwargs['author'])

   
    if search :=request.GET.get('search'): 
        posts=posts.filter(Q(title__icontains=search)| Q(description__icontains=search))
        
       
    context = {'posts': posts}
    return render(request, 'blog/blog.html',context)

def blog_detail(request,num):

    post=get_object_or_404(Post,id=num,active=1)
    comments=Comment.objects.filter(post=post,active=1)
    if request.method == 'POST':
        form=CommentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'کامنت شما ثبت شد منتظر تایید کامنت خود باشید.')
            return redirect('/')
    form=CommentForm
    context={'post':post,'comments':comments,'forms':form}
    return render(request, 'blog/blog-detail.html',context)

 