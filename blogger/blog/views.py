from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from .models import Blog, Comments
from .forms import CreateEditBlogForm, CommentsForm, ShareBlogForm
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.db.models import Q
from taggit.models import Tag
from django.core.mail import send_mail
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


# Create your views here.
def blogListView(request, tag_slug=None):
    blogs = Blog.objects.filter(status='published')
    query = request.GET.get('q')
    if query:
        blogs = Blog.objects.filter(Q(title__icontains=query) | Q(author__username=query)| Q(body__icontains=query))
    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        blogs = Blog.objects.filter(tags__in=[tag])
    paginator = Paginator(blogs, 5)
    page_number = request.GET.get('page')
    try:
        blog_list = paginator.page(page_number)
    except PageNotAnInteger:
        blog_list = paginator.page(1)
    except EmptyPage:
        blog_list = paginator.page(paginator.num_pages)
    return render(request, 'blog/blog_list.html', {'blog_list':blog_list})

@login_required(login_url='accounts:login')
def createBlogView(request):
    if request.method == 'POST':
        form = CreateEditBlogForm(request.POST)
        if form.is_valid():
            new_blog = form.save(commit=False)
            title = form.cleaned_data['title']
            slug = '-'.join(title.lower().split())
            new_blog.slug = slug
            new_blog.author = request.user
            new_blog.save()
            return redirect('blog:home')
    else:
        form = CreateEditBlogForm()
        return render(request, 'blog/create_blog.html', {'form':form})

def blogDetailView(request, id, year, month, day, post):
    blog = get_object_or_404(Blog, id=id, slug=post, status='published')
    comments = Comments.objects.filter(blog=blog).order_by('-id')
    is_liked = False
    if blog.likes.filter(id=request.user.id).exists():
        is_liked = True
    if request.method == 'POST':
        comment_form = CommentsForm(request.POST or None)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.user = request.user
            new_comment.blog = blog
            new_comment.save()
    else:
        comment_form = CommentsForm()
    return render(request, 'blog/blog_detail.html', {'blog':blog, 'comments':comments, 'comment_form':comment_form, 'is_liked':is_liked})

def likeBlogView(request):
    blog = get_object_or_404(Blog, id=request.POST.get('blog_id'))
    is_liked = False
    if blog.likes.filter(id=request.user.id).exists():
        blog.likes.remove(request.user)
        is_liked = False
    else:
        blog.likes.add(request.user)
        is_liked = True
    return HttpResponseRedirect(blog.get_absolute_url())

def shareBlogView(request, id):
    blog = get_object_or_404(Blog, id=id, status='published')
    if request.method == 'POST':
        form = ShareBlogForm(request.POST)
        if form.is_valid():
            subject = '{} ({}) recommends you to read "{}"'.format((request.user.first_name+' '+request.user.last_name), request.user.email, blog.title)
            blog_url = request.build_absolute_uri(blog.get_absolute_url())
            message = 'Read Blog at:\n{}\n\n{}\'s comments: \n{}'.format(blog_url, (request.user.first_name+' '+request.user.last_name), form.cleaned_data['comment'])
            send_mail(subject, message, 'djangoblogproject@gmail.com', [form.cleaned_data['email']])
            return HttpResponseRedirect(blog.get_absolute_url())
    else:
        form = ShareBlogForm()
        return render(request, 'blog/share_blog.html', {'form':form, 'blog':blog})

def myBlogsView(request):
    blogs = Blog.objects.filter(author=request.user)
    print(blogs)
    return render(request, 'blog/my_blogs.html', {'blogs':blogs})

def myBlogEditView(request, id):
    blog = Blog.objects.get(id=id)
    if request.method == 'POST':
        form = CreateEditBlogForm(data=request.POST or None, instance=blog)
        if form.is_valid():
            form.save()
            return redirect('blog:my_blogs')
    else:
        form = CreateEditBlogForm(instance=blog)
        return render(request, 'blog/create_blog.html', {'form':form})

def myBlogDeleteView(request, id):
    blog = Blog.objects.get(id=id)
    blog.delete()
    return redirect('blog:my_blogs')
