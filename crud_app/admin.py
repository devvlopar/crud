from django.contrib import admin

from crud_app.models import Task, User

# Register your models here.
admin.site.register(Task)
admin.site.register(User)
