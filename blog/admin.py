from django.contrib import admin
from posts.models import Post, Category, Tag
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    model = Post
    list_display = ('title', 'subtitle',)
    prepopulated_fields = {'slug': ('title',)}
    
admin.site.register(Post, PostAdmin)
admin.site.register(Category)
admin.site.register(Tag)