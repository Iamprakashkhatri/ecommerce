from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User
from .models import Project,Member,Task,Company

from .models import Post
from guardian.admin import GuardedModelAdmin

admin.site.register(Project)
admin.site.register(Member)
admin.site.register(Task)
admin.site.register(Company)

class PostAdmin(GuardedModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ('title', 'slug', 'created_at')
    search_fields = ('title', 'content')
    ordering = ('-created_at',)
    date_hierarchy = 'created_at'

admin.site.register(Post, PostAdmin)