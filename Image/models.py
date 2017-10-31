from __future__ import unicode_literals
from datetime import datetime

from django.db import models

# Create your models here.



# Design database fields

class Image(models.Model):
	image = models.ImageField(max_length=100,verbose_name='image',default='',upload_to='images/%Y')
	add_time = models.DateTimeField(default=datetime.now,verbose_name='add_time')
	class Meta:
		ordering = ('add_time',)
	def __unicode__(self):
		return self.image