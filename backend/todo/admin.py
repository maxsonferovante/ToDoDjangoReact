from django.contrib import admin
from .models import Todo
# Register your models here.
class TodoAdmin(admin.ModelAdmin):
    readonly_fields = ('created',)
    list_display = ('title','id', 'description', 'completed')

admin.site.register(Todo, TodoAdmin)