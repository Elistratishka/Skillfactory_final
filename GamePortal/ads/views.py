from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from .models import News
from django.contrib.auth.models import User
from .forms import PostForm
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
import logging


logger = logging.getLogger(__name__)


class PostList(ListView):
    model = News
    context_object_name = 'posts'
    form_class = PostForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = PostForm()
        return context

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
        return super().get(request, *args, **kwargs)


class PostView(DetailView):
    model = News
    context_object_name = 'post'


class UserView(DetailView):
    model = User
    template_name = 'News/User.html'
    context_object_name = 'User'


class PostAdd(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    permission_required = ('news.add_post',)
    model = News
    form_class = PostForm
    template_name = 'News/Post_new.html'


class PostEdit(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    permission_required = ('news.change_post',)
    model = News
    form_class = PostForm

    def get_object(self, **kwargs):
        pk = self.kwargs.get('pk')
        return News.objects.get(pk=pk)


class PostDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    permission_required = ('news.delete_post',)
    model = News
    queryset = News.objects.all()
    success_url = '/news/'
