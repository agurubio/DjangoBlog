from . import views
from django.urls import path


urlpatterns = [
    path('<user>/inbox', views.Inbox.as_view(), name='inbox'),
    path('<user>/sentbox', views.SentBox.as_view(), name='sentbox'),
    path('<user>/NewMessage', views.NewMessage.as_view(), name='new_message'),
]