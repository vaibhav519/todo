from django.urls import path
from .views import PostListView, PostCreateView, PostDeleteView, PostUpdateView
from . import views


urlpatterns = [
    path('', PostListView.as_view(), name='todo-home'),
    path('todo/new/', PostCreateView.as_view(), name='todo-create'),
    path('todo/<int:pk>/update/', PostUpdateView.as_view(), name='todo-update'),
    path('todo/<int:pk>/delete/', PostDeleteView.as_view(), name='todo-delete'),
]