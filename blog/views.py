from blog.models import Post
from django.shortcuts import render
from datetime import date


# Helper files

def get_date(post):
    return post.get('date')

# Create your views here.

def starting_page(request):

    latest_posts = Post.objects.all().order_by("-date")[:3]   #Django will automatically convert this into long sql query so no performance issue...
    # sorted_posts = sorted(all_posts,key=get_date) #Sorted the List all_posts...
    # latest_posts = sorted_posts[-3:]
    return render(request,"blog/index.html",{
        "posts":latest_posts
    })

def posts(request):
    all_posts = Post.objects.all()
    return render(request,"blog/all-posts.html",{
        "all_posts":all_posts
    })

def post_detail(request,slug):
    identified_post = Post.objects.get(slug=slug)
    # identified_post = next(post for post in all_posts if post['slug'] == slug)
    return render(request,"blog/post-detail.html",{
        "identified_post": identified_post,
        "post_tags":identified_post.tags.all()
    })
