from django.shortcuts import render
from django.http import HttpResponse
from main import models
import random
# Create your views here.

def boards(request, board="r"):
    posts = models.Post.objects.filter(postboard=board).order_by("-postid")[:5]
    context = {"posts":posts, "board":board, "boardtopic":models.Board.objects.get(boardname=board).boardtopic}
    models.Board.objects.get(boardname=board).boardposts = len(models.Board.objects.filter(boardname=board))
    models.Board.objects.get(boardname=board).save()
    # userpost = models.Post()
    # userpost.postcontent = request.POST.get("newpost", "")
    # userpost.postid = random.randrange(0,100,1)
    # if userpost.postcontent:
    #     userpost.save()
    return render(request, "board.html", context)

def reply(request, board="r", postid="0"):
    pass
