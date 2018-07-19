from django.shortcuts import render
from django.http import HttpResponse
from main import models
import random
# Create your views here.

def index(request):

    posts = models.Post.objects.order_by("-postid")[:5]
    context = {"posts":posts}
    userpost = models.Post()
    userpost.postcontent = request.POST.get("newpost", "")
    userpost.postid = random.randrange(0,100,1)
    if userpost.postcontent:
        userpost.save()
    return render(request, "index.html", context)
