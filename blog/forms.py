from django import forms
from blog.models import comment, post

# class NewComment(forms.Form):
#     name = forms.CharField()
#     email = forms.EmailField()
#     body = forms.Textarea()

class NewComment(forms.ModelForm):
    class Meta:
        model = comment
        fields = ('name', 'email', 'body')


class CreatePost(forms.ModelForm):
    title = forms.CharField(label = 'الاسم')
    content = forms.CharField(label = 'البريد الالكتروني', widget = forms.Textarea)
    class Meta:
        model = post
        fields = ('title', 'content')
