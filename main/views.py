from django.shortcuts import render
from django.http import HttpResponse
from main import models
import random
import datetime
# Create your views here.

def index(request):
    indexcontext = {}
    return render(request, "index.html", indexcontext)

def boards(request, board="r"):
    posts = models.Post.objects.filter(postboard=board).order_by("-postid")[:5]
    replies = []
    for o in posts:
        replies.append(models.Post.objects.filter(postparent=o.postid))
    boardscontext = {"posts":posts, "board":board, "boardtopic":models.Board.objects.get(boardname=board).boardtopic, "replies":replies}
    models.Board.objects.get(boardname=board).boardposts = len(models.Board.objects.filter(boardname=board))
    models.Board.objects.get(boardname=board).save()
    # userpost = models.Post()
    # userpost.postcontent = request.POST.get("newpost", "")
    # userpost.postid = random.randrange(0,100,1)
    # if userpost.postcontent:
    #     userpost.save()
    return render(request, "board.html", boardscontext)

def reply(request, board="r", postid="0"):
    parent = models.Post.objects.get(postid=postid)
    replies = models.Post.objects.filter(postparent=postid)
    replycontext = {"parent":parent, "replies":replies}
    if "submit-post" in request.POST:
        userpost = models.Post()
        userpost.postid = int(models.Post.objects.filter().order_by("-postid")[0].postid + 1)
        userpost.postimg = request.POST.get("userimg", "")
        userpost.postcontent = request.POST.get("usertext", "")
        userpost.postauthor = request.POST.get("username", "")
        userpost.postboard = board
        userpost.postparent = parent.postid
        userpost.save()
    return render(request, "reply.html", replycontext)
