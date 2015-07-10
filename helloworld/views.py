from django.shortcuts import render_to_response
from django.shortcuts import render
from django.http import HttpResponse
from helloworld.models import Blogs
# Create your views here.
def home(request):

    context={}
    return render(request,"helloworld/index.html",context)

def blog(request, blog_id):
    blog=Blogs.objects.get(id=blog_id)
    context={'blog':blog}
    return render(request,"helloworld/singleblog.html", context)

def bloghome(request):
    allblogs=Blogs.objects.all()
    context={'allblogs':allblogs}
    return render(request,"helloworld/blog.html", context)

def recursiveBayes(request):
    context={}
    return render(request, "helloworld/rbfblogpost.html", context)
