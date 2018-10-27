from django.contrib import admin
from .models import *
# Register your models here.


# class CategoryAdmin(admin.ModelAdmin):
#     list_display = ('name',)


# class TagAdmin(admin.ModelAdmin):
#     list_display = ('name',)


# class BlogAdmin(admin.ModelAdmin):
#     list_display = ('title', 'category', 'content', 'pub')


# class CommentAdmin(admin.ModelAdmin):
#     list_display = ('blog', 'name', 'content', 'pub')

admin.site.register(User)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Blog)
admin.site.register(Comment)
