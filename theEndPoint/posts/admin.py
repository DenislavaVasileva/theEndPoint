from django.contrib import admin
from .models import Category, Post, Comment
from unfold.admin import ModelAdmin


@admin.register(Category)
class CategoryAdmin(ModelAdmin):
    list_display = ['name']


@admin.register(Post)
class PostAdmin(ModelAdmin):
    list_display = ['title', 'author', 'content', 'created_at', 'category']
    list_filter = ['category']
    ordering = ['-created_at']
    search_fields = ['title', 'author__user__username', 'content']


@admin.register(Comment)
class CommentAdmin(ModelAdmin):
    list_display = ['post', 'author', 'content', 'created_at']
    list_filter = ['post']
    ordering = ['-created_at']
