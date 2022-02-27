from . import views
from django.urls import path

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('NewPost/', views.CreatePost.as_view(), name='post_create'),
    path('<slug>/edit/', views.UpdatePost.as_view(), name='post_edit'),
    path('<slug>/delete/', views.DeletePost.as_view(), name='post_delete'),
    path('about/', views.about_page, name='about'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    
]