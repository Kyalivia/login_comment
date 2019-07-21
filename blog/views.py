from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone

from .models import Blog
from .forms import Create

from .models import Comment
from .forms import CommentForm

from django.contrib.auth.decorators import login_required

@login_required
def read(request):
    blogs = Blog.objects.order_by('-id')
    return render(request, 'blog/read.html', {'blogs': blogs})

@login_required
def create(request):
    if request.method == 'POST':
        form = Create(request.POST)
        if form.is_valid:
            post = form.save(commit=False)
            post.pub_date = timezone.now()
            post.save()
            return redirect('read') 
    else:
        form = Create()
        return render(request, 'blog/create.html', {'form':form})
       
@login_required
def update(request, pk):
        blog = get_object_or_404(Blog, pk=pk)

        if request.method == "POST":
                form = Create(request.POST, instance=blog) 

                if form.is_valid(): 
                        blog = form.save(commit=False) 
                        blog.update_date=timezone.now() 
                        blog.save()
                        return redirect('read') 

        else:
                form = Create(instance=blog) 
                return render(request, 'blog/update.html',{'form' : form})

@login_required
def delete(request, pk):
        blog = Blog.objects.get(id=pk)
        blog.delete()
        return redirect('read')

@login_required
def detail(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    
    if request.method == "POST":
        comment_form = CommentForm(request.POST)
        comment_form.instance.blog_id = blog_id
        if comment_form.is_valid():
            comment = comment_form.save()



    comment_form = CommentForm()
    comments = blog.comments.all()

    return render(request, 'blog/detail.html', {'blog':blog, 'comments':comments, 'comment_form':comment_form})

