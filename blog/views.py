
from django.shortcuts import render
from django.urls import reverse

from blog.models import Post

def index(request):
    user = request.user
    admin_link = reverse('admin:index')
    posts = Post.objects.filter(published=True).order_by('-created_at')
    return render(request, 'index.html', {'posts': posts,'admin_link': admin_link, 'user': user})



