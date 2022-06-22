from django import forms


class AddPostForm(forms.Form):

    title = forms.CharField(label='Title', max_length=100)
    content = forms.CharField(label='Content', max_length=4000)
