from django.urls import path

from .views import PostListView, PostCreateView, PostUpdateView


urlpatterns = [
    path('', PostListView.as_view(), name='post'),
    path('post/create', PostCreateView.as_view(), name='create-post'),
    path('post/<int:pk>/update', PostUpdateView.as_view(), name='update-post'),

]
