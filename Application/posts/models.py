from datetime import timezone
from django.db import models

# Create your models here.
class Post(models.Model):
    # Title of the model with a maximum length
    title = models.CharField(max_length=100)
    # A text field relates to a text area form
    body = models.TextField()
    slug = models.SlugField()
    # datetime stamp gets added every time that a user inputs information
    date = models.DateTimeField(auto_now_add=True)
    # Now, we are includding a banner image to each post. We are setting a default image and telling the page that it is 
    # ok for the image to be blank (null)
    banner = models.ImageField(default='fallback.jpg', blank=True)
    
    # Define str method that will return as a string the informaiton of our object
    def __str__(self):
        return self.title