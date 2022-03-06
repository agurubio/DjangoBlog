from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Message(models.Model):
    msg_title = models.CharField(max_length=50, default="")
    sender = models.ForeignKey(User, related_name="sender", on_delete= models.CASCADE)
    reciever = models.ForeignKey(User, related_name="receiver", on_delete= models.CASCADE)
    msg_content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.msg_title
