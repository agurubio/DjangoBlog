from django import forms
from django.contrib.auth.models import User
from django_summernote.fields import SummernoteTextFormField, SummernoteTextField

STATUS = ((0,"Draft"),(1,"Published"))

class PostForm(forms.Form):
    title = forms.CharField(max_length=200, unique=True)
    slug = forms.SlugField(max_length=200, unique=True)
    author = forms.ForeignKey(User, on_delete= forms.CASCADE,related_name='blog_posts')
    updated_on = forms.DateTimeField(auto_now= True)
    #content = forms.TextField()
    content = SummernoteTextFormField()
   # foo = SummernoteTextFormField()
    created_on = forms.DateTimeField(auto_now_add=True)
    status = forms.IntegerField(choices=STATUS, default=0)