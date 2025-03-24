from django import forms


class ContactUsForm(forms.Form):
    title = forms.CharField(max_length=50, required=True)
    email = forms.EmailField(required=True)
    content = forms.CharField(widget=forms.Textarea())
