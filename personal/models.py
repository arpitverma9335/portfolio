from django.db import models

# Create your models here.
class blog(models.Model):
	theme = models.CharField(max_length = 50)
	date = models.DateField(auto_now=True)
	title = models.TextField()
	content = models.TextField(default=None)

class project(models.Model):
	about = models.CharField(max_length = 100)
	link = models.URLField(max_length = 100)
	desc = models.TextField(default = None)

class achievement(models.Model):
	field = models.CharField(max_length = 50 , default = None)
	platform = models.CharField(max_length = 50 , default = None)
	descn = models.TextField(default = None)

class skill(models.Model):
	area = models.CharField(max_length = 40)
	percent = models.IntegerField(default = 0)

class user_ip(models.Model):
	ip = models.GenericIPAddressField(default = None)
	time = models.DateTimeField(auto_now=True)