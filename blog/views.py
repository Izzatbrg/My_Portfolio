from django.shortcuts import render,get_object_or_404
from .models import Blog

def all_blogs(request):
    blogs = Blog.objects.order_by('-date')
    return render(request, 'blogs/all_blogs.html',{'blogs':blogs})
def blog(request, blog_id):
    bloG = get_object_or_404(Blog, pk=blog_id)
    return render(request,'blogs/blog.html',{'blog': bloG})
