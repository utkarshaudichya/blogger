from django.contrib import admin
from .models import Blog, Comments

# Register your models here.
class BlogAdmin(admin.ModelAdmin):
    list_display = ('author', 'status', 'title', 'slug', 'publish', 'created', 'updated')
    list_filter = ('status', 'created', 'publish')
    search_fields = ('title', 'body', 'author')
    prepopulated_fields = {'slug':('title',)}
    raw_id_fields = ('author',)
    date_hierarchy = 'publish'
    ordering = ['status', 'publish']

admin.site.register(Blog, BlogAdmin)
admin.site.register(Comments)
