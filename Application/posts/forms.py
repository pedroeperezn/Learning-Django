# Import forms and our data model for each post
from django import forms
from . import models
# Create class for posts
class CreatePost(forms.ModelForm):
    # Create a meta subclass which is the metadata
    class Meta:
        # We are going to be using the data from the data model we previously
        # declared and we are specifying which fields from the data model we are including
        model = models.Post
        fields = ['title','body','slug','banner']
        