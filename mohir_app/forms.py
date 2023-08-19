from django import forms
from .models import Contact, Commentsx

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = "__all__"

class SubscriptionForm(forms.Form):
    subject = forms.CharField(max_length=100, label="Subject")
    message = forms.CharField(widget=forms.Textarea, label="Message")
    email = forms.EmailField(label="Email", required=True)

class CommentForm(forms.ModelForm):
    class Meta:
        model = Commentsx
        fields = ['user', 'body']
