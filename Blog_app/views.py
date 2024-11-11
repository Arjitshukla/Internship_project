from django.shortcuts import render
from Blog_app.models import BlogPost

# Create your views here.
def blog(request):
    allPosts = BlogPost.objects.all()
    context ={'allposts':allPosts}
    return render (request,"blogs/blogs_card.html",context)
    # return render (request,"blogs/blog_detail.html")



 
def blog_detail(request,slug):
    post = BlogPost.objects.filter(slug =slug)[0]
    context ={"post":post}
    return render (request,"blogs/blog_detail.html",context)
    # return render (request,"blogs/blog_detail.html")

