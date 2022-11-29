from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
import os

class Post(models.Model):
	title = models.CharField(max_length=100) #name of post
	file = models.FileField(null=True,blank=True,upload_to='Files') #file
	content = models.TextField() #description
	date_posted = models.DateTimeField(default=timezone.now) #time function to display time
	author = models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		return self.title

	def extension(self):
		name, extension = os.path.splitext(self.file.name)
		return extension

	def get_absolute_url(self):
		return reverse('post-detail', kwargs={'pk': self.pk})

        
