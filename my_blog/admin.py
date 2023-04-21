from django.contrib import admin
from .models import Post, Category, Tag, Comment, Author, Subscriber


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'date_posted')
    list_filter = ('date_posted', 'categories', 'tags')
    search_fields = ('title', 'content')
    prepopulated_fields = {'slug': ('title',)}
    # Dodanie prepopulated_fields wykorzystuje mechanizm slugowania, który bazuje na polu 'title'


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_by', 'date_created')
    search_fields = ('name', 'created_by__username')
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('content', 'post', 'date_posted')
    list_filter = ('date_posted',)
    search_fields = ('content', 'email', 'body')


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('user', 'bio', 'website')
    search_fields = ('user__username', 'bio', 'website')


@admin.register(Subscriber)
class SubscriberAdmin(admin.ModelAdmin):
    list_display = ('email', 'is_active', 'date_subscribed')
    list_filter = ('is_active', 'date_subscribed')
    search_fields = ('email',)
