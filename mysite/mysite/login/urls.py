from . import views
from django.urls import path


urlpatterns = [
    path('register/', views.register, name='register'),
    path('update/', views.UpdateProfile, name='update'),
    path('profile/', views.UserDetail.as_view(), name='profile'),
    path('agregarAvatar/', views.agregarAvatar, name='add_avatar'),
    ]