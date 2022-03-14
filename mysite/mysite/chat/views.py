from django.shortcuts import render
from django.views import generic
from .models import Message
from login.models import Usuario
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.
class Inbox(generic.ListView, LoginRequiredMixin):
    Model = Message
    queryset =  Message.objects.all
    template_name = 'inbox.html'

class SentBox(generic.ListView, LoginRequiredMixin):
    queryset =  Message.objects.all
    template_name = 'sentbox.html'

class NewMessage(generic.CreateView, LoginRequiredMixin):
    model = Message
    template_name = 'msg_form.html'
    fields = ['msg_title', 'sender', 'reciever', 'msg_content']
    success_url = '/'