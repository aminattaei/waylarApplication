from django import forms
from comments.models import Comment


class ContactForm(forms.Form):
    message_title = forms.CharField(
        max_length=50, required=True, empty_value="enter title message"
    )
    user_email = forms.EmailField(required=True)
    message_content = forms.CharField(required=True, widget=forms.Textarea)


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
