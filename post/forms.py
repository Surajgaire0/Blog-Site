from django import forms
from django_summernote.widgets import SummernoteWidget
from .models import Posts
from django.core.exceptions import ValidationError

class PostsForm(forms.ModelForm):
    description=forms.CharField(widget=SummernoteWidget(),help_text='Should be at least 200 words.')

    def clean_description(self):
        description=self.cleaned_data['description']
        if len(description.split())<200:
            raise ValidationError('Content should be at least 200 words.')
        return description

    class Meta:
        model=Posts
        fields=('title','description')