from django.db import models

# Create your models here.
class blog(models.Model):
	theme = models.CharField(max_length = 50)
	date = models.DateField(auto_now=True)
	title = models.TextField()
	content = models.TextField(default=None)

	def __str__(self):
		return self.title

class project(models.Model):
	about = models.CharField(max_length = 100)
	link = models.URLField(max_length = 100)
	desc = models.TextField(default = None)

	def __str__(self):
		return self.about

class achievement(models.Model):
	auth_url = models.CharField(max_length = 100 , default = 'None')
	field = models.CharField(max_length = 50 , default = None)
	platform = models.CharField(max_length = 50 , default = None)
	descn = models.TextField(default = None)

	def __str__(self):
		return self.platform

class skill(models.Model):
	area = models.CharField(max_length = 40)
	percent = models.IntegerField(default = 0)

	def __str__(self):
		return self.area

class sf_skill(models.Model):
	sf_area = models.CharField(max_length = 40)
	sf_percent = models.IntegerField(default = 0)

	def __str__(self):
		return self.sf_area

class user_ip(models.Model):
	ip = models.GenericIPAddressField(default = None)
	time = models.DateTimeField(auto_now=True)

	def __str__(self):
		return f"{self.time.date()} {self.ip}"

class contact(models.Model):
	add_line1 = models.CharField(max_length = 150 , default = None)
	add_line2 = models.CharField(max_length = 150 , default = None)
	number = models.CharField(max_length = 12 , default = None)
	email = models.EmailField(max_length = 254 , default = 'asme.arpitverma19@gmail.com')

class aim_about(models.Model):
	aim = models.TextField(default = "My aim is to be a successful Entrepreneur, by serving something to the society to meet its necessities and hence, upgrade its lifestyle.")
	myself = models.TextField(default =  "Hello! I'm Arpit, a web developer(django framework), a tech enthusiast, and a guy slighty obsessed for code quality. I’m currently studying mechanical engineering in NIT patna. If you have a project that you want to get started or think you need my help with something, then get in touch.")