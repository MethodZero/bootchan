from django.db import models
from main import views
import datetime
# Create your models here.
class Post(models.Model):
    postid = models.PositiveIntegerField()
    postcontent = models.CharField(max_length=1024)
    postimg = models.URLField(blank=True)
    postauthor = models.CharField(max_length=16, default="Anonymous")
    posttitle = models.CharField(max_length=32, blank=True)
    posttime = models.DateField(default=datetime.date.today, blank=True)
    postboard = models.CharField(default="r", max_length=32)
    postparent = models.PositiveIntegerField(default=0)
class Board(models.Model):
    boardtopic = models.CharField(max_length=32)
    boardposts = models.PositiveIntegerField()
    boardname = models.CharField(max_length=8)
