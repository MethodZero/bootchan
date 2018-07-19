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
    postboard = models.CharField(default="alt.random", max_length=32)
