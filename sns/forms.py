from django import forms
from .models import Message,Friend,Good
from django .contrib.auth.models import User

#Messageフォーム
class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['owner','content']

#Friendフォーム
class FriendForm(forms.ModelForm):
    class Meta:
        model = Friend
        fields = ['owner','user']

#Goodフォーム
class GoodForm(forms.ModelForm):
    class Meta:
        model = Good
        fields = ['owner', 'message']

#検索フォーム
class SearchForm(forms.Form):
    serch = forms.CharField(max_length=100)

#投稿フォーム
class PostForm(forms.Form):
    content = forms.CharField(max_length=100, widget=forms.Textarea(attrs={'placeholder' : 'いまどうしてる？' , 'cols': 40, 'rows' : 5}))
