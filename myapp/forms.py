from django import forms
from django.db.models import fields
from .models import Post


class PostForm(forms.ModelForm):


    class Meta:
        model = Post
        fields = [
            'title', 'content', 'Industry', 'occupation', 'job_description', 'qualifications', 
            'time', 'thumbnail', 'img', 'work_style', 'salary', 'tag', 'vacation', 'benefit',
            'prefecture', 'city',
            ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'