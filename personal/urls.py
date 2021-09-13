from django.contrib import admin
from django.urls import path
from . import views
from django.conf.urls import handler404

urlpatterns = [
    path('' , views.index_func),
    path('about',views.about),
    path('services',views.services),
    path('view_more',views.more),
    path('blog',views.blog_func),
    path('single-blog',views.single_blog),
    path('contact',views.contacts),
    path('offline',views.offline),
]

handler404 = 'personal.views.handler404'