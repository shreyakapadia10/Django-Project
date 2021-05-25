from django.shortcuts import render
from .models import Blogpost

# Create your views here.


def index(request):
    posts = Blogpost.objects.all()
    return render(request=request, template_name="blog/index.html", context={'allPosts': posts})


def blogpost(request, pid):
    posts = Blogpost.objects.filter(post_id=pid)[0]
    return render(request=request, template_name="blog/blogpost.html", context={"post": posts})