from django.urls import path
from .views import PostList, PostView, UserView, PostAdd, PostEdit, PostDelete


urlpatterns = [
    path('', PostList.as_view(), name='list'),
    path('<int:pk>/', PostView.as_view(), name='detail'),
    path('<int:pk>/edit', PostEdit.as_view(), name='edit'),
    path('<int:pk>/delete', PostDelete.as_view(), name='delete'),
    path('search/', UserView.as_view(), name='user'),
    path('add/', PostAdd.as_view(), name='add'),
    ]
