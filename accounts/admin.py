from django.contrib import admin
from .models import Profile, ToDo, Diary

# Register your models here.
from django.contrib import admin
from .models import Profile, ToDo, Diary

@admin.register(ToDo)
class ToDoAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'completed', 'created_at')
    list_filter = ('completed', 'created_at')
    search_fields = ('title', 'description')

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'birthday')
    search_fields = ('user__username', 'user__first_name', 'user__last_name')

@admin.register(Diary)
class DiaryAdmin(admin.ModelAdmin):
    list_display = ('title', 'user')
    search_fields = ('title', 'description')
