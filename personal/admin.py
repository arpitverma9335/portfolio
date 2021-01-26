from django.contrib import admin
from .models import blog
from .models import project
from .models import achievement
from .models import skill
from .models import user_ip


# Register your models here.
admin.site.register(blog)
admin.site.register(project)
admin.site.register(achievement)
admin.site.register(skill)
admin.site.register(user_ip)