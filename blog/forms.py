from .models import Comment
from django import forms

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)
        # exclude = ('post', 'author', 'created_at', 'modified_at')
        # 여러 개의 필드 중에 몇 개만 빼고 싶을 때