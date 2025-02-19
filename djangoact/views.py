from django.shortcuts import render
from .models import Post


def post_list(request):
    posts = Post.objects.all()
    return render(request, 'book/post_list.html', {'posts': posts})

def bookview(request):
    return render(request,'First.html')

