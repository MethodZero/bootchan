from django import forms

from models import Post

class ReplyForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ("postcontent")
