from django.urls import path

from .views import PostListView, PostDetailView, PostCreateView, post_add, post_edit, PostUpdateView, PostDeleteView

urlpatterns = [
    path("", PostListView.as_view(), name ='post_list'),
    path('<int:pk>/', PostDetailView.as_view(), name = 'post_detail'),
    path('create/', PostCreateView.as_view(), name='post_create'),
    path('add/', post_add, name='post_add'),
    path('<int:pk>/edit/', post_edit, name='post_edit'),
    path('<int:pk>/update/', PostUpdateView.as_view(), name='post_update'),
    path('<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),



]