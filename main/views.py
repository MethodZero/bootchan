from django.shortcuts import render
from django.http import HttpResponse
from main import models
import random
# Create your views here.

def boards(request, board="r"):
    posts = models.Post.objects.filter(postboard=board).order_by("-postid")[:5]
    boardscontext = {"posts":posts, "board":board, "boardtopic":models.Board.objects.get(boardname=board).boardtopic}
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
    replycontext = {"parent":parent, "form":form}
    if request.method == "POST":
        form = ReplyForm(request.POST)
        post = form.save(commit=False)
        post.postid = (models.Post.objects.filter(postboard=board).order_by("-postid")[0] + 1)
    else:
        form = ReplyForm()
    return render(request, "reply.html", replycontext)
