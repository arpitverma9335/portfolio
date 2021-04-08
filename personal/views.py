from django.shortcuts import render
from .models import blog
from .models import project
from .models import achievement
from .models import skill
from .models import user_ip
from .models import contact
from .models import aim_about

# Create your views here.
def index_func(request):
	x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
	if x_forwarded_for:
		ip = x_forwarded_for.split(',')[0]
	else:
		ip = request.META.get('REMOTE_ADDR')
	u = user_ip(ip = ip)
	if len(user_ip.objects.filter(ip = ip).values()) > 0:
		pass
	else:
		u.save()
	return render(request , 'index.html')

def about(request):
	skills = skill.objects.all().order_by('-percent')
	aim_obj = aim_about.objects.all()
	return render(request , 'about-us.html' , {'skills':skills , 'aim_about':aim_obj})

def services(request):
	return render(request , 'services.html')

def portfolio(request):
	proj = project.objects.all()
	ach = achievement.objects.all()
	return render(request , 'portfolio.html',{'projects':proj , 'achievements':ach})

def more(request):
	blog_id = request.GET['blogID']
	sp_blog = blog.objects.filter(id = blog_id)
	title =  blog.objects.filter(id = blog_id).values('title')[0]
	return render(request , 'single-blog.html' , {'blog':sp_blog , 'title':title['title']})

def blog_func(request):
	blg = blog.objects.all().order_by('-id')
	return render(request , 'blog.html',{'blog':blg})

def single_blog(request):
	return render(request , 'single-blog.html')

def contacts(request):
	contact_obj = contact.objects.all()
	return render(request , 'contact.html' , {'contacts':contact_obj})