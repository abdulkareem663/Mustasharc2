from django.contrib import admin
from .models import *


class TaskProjectInline(admin.StackedInline):
    model = TaskProject
    extra = 1


class ProjectAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['project','spiecification'],'classes': "__all__"}),
    ]
    inlines = [TaskProjectInline]


admin.site.register(Degree)
admin.site.register(Subject)
admin.site.register(Spiecification)
admin.site.register(Service)
admin.site.register(TaskProject)
admin.site.register(Project,ProjectAdmin)
admin.site.register(Country)
admin.site.register(Bank)
admin.site.register(NumberAccount)
