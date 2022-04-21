
from django.contrib import admin

from .models import Category, Tag, Blog, Comment


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulater_fields = {'slug': ('name',)}


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulater_fields = {'slug': ('name',)}


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['blog', 'user']
    prepopulater_fields = {'user': ('created', 'text')}


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'created']
    prepopulater_fields = {'slug': ('title', 'category')}
    list_filter = ['category', 'tags']
    search_fields = ['title']

















# from django.contrib import admin
#
# from .models import Category, Comment,Blog,Tag
#
# @admin.register(Category)
# class CategoryAdmin(admin.ModelAdmin):
#     list_display = ['name','slug']
#     prepopulated_fields = {'slug',('name',)}
#
# @admin.register(Blog)
# class BlogAdmin(admin.ModelAdmin):
#     list_display = ['title', 'category','user','created','views']
#     prepopulated_fields = {'slug',('title',)}
#     list_filter = ['category','tags']
#
# @admin.site.register(Comment)
# class CommentAdmin(admin.ModelAdmin):
#     list_display = ['name', 'slug']
#     prepopulated_fields = {'slug', ('name',)}
#
# @admin.register(Tag)
# class
