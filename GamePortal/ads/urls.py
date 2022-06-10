from django.urls import path
from .views import PostList, PostView, UserView, PostAdd, PostEdit, PostDelete, comment_add


urlpatterns = [
    path('', PostList.as_view(), name='list'),
    path('news/<int:pk>/', PostView.as_view(), name='detail'),
    path('news/<int:pk>/edit', PostEdit.as_view(), name='edit'),
    path('news/<int:pk>/delete', PostDelete.as_view(), name='delete'),
    path('<int:pk>/user_lk/', UserView.as_view(), name='user'),
    path('add/', PostAdd.as_view(), name='add'),
    path('news/<int:pk>/comment', comment_add, name='add_comment')
    ]

