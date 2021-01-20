from django.shortcuts import render
from .models import blog
from .models import project
from .models import achievement
from .models import skill

# Create your views here.
def index_func(request):
	return render(request , 'index.html')

def about(request):
	skills = skill.objects.all().order_by('-percent')
	return render(request , 'about-us.html' , {'skills':skills})

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

def contact(request):
	return render(request , 'contact.html')