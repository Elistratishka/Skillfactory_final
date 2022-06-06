from django.forms import ModelForm
from .models import News


class PostForm(ModelForm):

    class Meta:
        model = News
        fields = ['character', 'header', 'content', 'author']
