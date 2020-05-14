from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
# Create your views here.


def hello(request):
	#return HttpResponse("hello world");
	context ={"name":"israr",
			  "posts":Post.objects.all()
			  }
	return render(request,'posts/home.html',context)