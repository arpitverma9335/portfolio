from django.contrib import admin
from .models import blog
from .models import project
from .models import achievement


# Register your models here.
admin.site.register(blog)
admin.site.register(project)
admin.site.register(achievement)