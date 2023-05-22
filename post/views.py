from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Post
from .forms import PostForm

# Create your views here.
def index(request):
    #if the method is post
    if request.method == 'POST':
        form = PostForm(request.POST,request.FILES)
        #if the form is valid
        if form.is_valid():
            #it will save
            form.save()
            #and redirect to HOME page
            return HttpResponseRedirect('/')

        else:
            return HttpResponseRedirect(form.errors.as_json())

    posts = Post.objects.all().order_by('-created_at')[:20]
    return render(request, 'post.html',{'posts': posts})

def delete(request,post_id):
    post = Post.objects.get(id = post_id)
    post.delete()
    return HttpResponseRedirect('/')

def like(request,post_id):
    post= Post.objects.get(id=post_id)
    post.like +=1
    post.save()
    return HttpResponseRedirect('/')

def edit(request,post_id):
    post= Post.objects.get(id=post_id)
    if request.method == 'POST':
        form= PostForm(request.POST,request.FILES,instance=post)
        if form.is_valid():
            post.save()
            return HttpResponseRedirect('/')
        else :
            form=PostForm(PostForm)
    return render(request,'edit.html',{'post':post}) 