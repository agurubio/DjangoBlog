from urllib import request
from django.shortcuts import render
from django.views import generic
from .models import Message
from django.contrib.auth.models import User


# Create your views here.

#@login_required
class Inbox(generic.ListView):
    queryset = Message.objects.all
    template_name = 'inbox.html'

class SentBox(generic.ListView):
    queryset =  Message.objects.all
    template_name = 'sentbox.html'

class NewMessage(generic.CreateView):
    model = Message
    template_name = 'msg_form.html'
    fields = ['msg_title', 'sender', 'reciever', 'msg_content']
    success_url = '/'