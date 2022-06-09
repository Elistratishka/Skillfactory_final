from django import forms
from .models import News, Comment
from ckeditor_uploader.widgets import CKEditorUploadingWidget


class PostForm(forms.ModelForm):
    content = forms.CharField(label='Текст', widget=CKEditorUploadingWidget())

    class Meta:
        model = News
        fields = ['author', 'header', 'content', 'character']


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ['text']
