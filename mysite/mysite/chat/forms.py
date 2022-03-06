from django import forms
from django.contrib.auth.models import User

class MessageForm(forms.Form):
    msg_title = forms.CharField(max_length=50)
    sender = forms.ForeignKey(User, related_name="sender", on_delete= forms.CASCADE,)
    reciever = forms.ForeignKey(User, related_name="receiver", on_delete= forms.CASCADE)
    msg_content = forms.TextField()
    created_at = forms.DateTimeField(auto_now_add=True)