from django import forms

from .models import User


class CommentManagement(forms.ModelForm):
    class Meta:
        model = User
        fields = ['Comment']
        widgets = {
            'Comment': forms.TextInput(attrs={'class': 'form-control', }),
            

        }
