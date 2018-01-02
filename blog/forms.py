from django import forms
from .models import Post


class PostForm(forms.ModelForm):  # forms.ModelForm: 이 폼이 ModelForm이라는 것을 장고에 알려줌
    class Meta:  # 이 폼을 만들기 위해 어떤 model(Post)이 쓰여야 하는지 장고에 알려줌
        model = Post
        fields = ('title', 'text',)