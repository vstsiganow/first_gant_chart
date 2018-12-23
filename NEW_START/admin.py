from django.contrib import admin
from .models import Project
from .models import CalendarPlan
from .models import Task

admin.site.register(Task)
admin.site.register(Project)
admin.site.register(CalendarPlan)
