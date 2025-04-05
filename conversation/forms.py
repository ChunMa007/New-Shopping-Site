from django import forms
from .models import ConversationMessages

class ConversationMessageForm(forms.ModelForm):
    class Meta:
        model = ConversationMessages
        fields = ('content', )
        widgets = {
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': '1'})
        }
        labels = {'content': ''}