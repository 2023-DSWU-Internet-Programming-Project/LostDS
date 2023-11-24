from .models import Comment
from django import forms

class CommentForm(forms.ModelForm):
    content = forms.CharField(
        label='',
        widget=forms.Textarea(attrs={'placeholder': ' 댓글을 입력해주세요 . . .','style': 'width: 100%; height: 100px; border-radius: 10px; resize: none;'})
    )

    class Meta:
        model = Comment
        fields = ('content',)
