from django.contrib import admin
from django.db import models
from django import forms
from .models import Comment, Article, Column, NewUser,Author

class CommentAdmin(admin.ModelAdmin):
	list_display = ('user_id','article_id','pub_date', 'content','poll_num')  

class ArticleAdmin(admin.ModelAdmin):
	formfield_overrides = {
        models.TextField: {'widget': forms.Textarea(
                           attrs={'rows': 41,
                                  'cols': 100
                                  })}, 
    }
	list_display = ('title','pub_date', 'poll_num') 

class NewUserAdmin(admin.ModelAdmin):
	list_display = ('username','date_joined', 'profile') 

class ColumnAdmin(admin.ModelAdmin):
	list_display = ('name', 'intro') 

class AuthorAdmin(admin.ModelAdmin):
	list_display = ('name', 'profile') 

admin.site.register(Comment, CommentAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Column, ColumnAdmin)
admin.site.register(NewUser, NewUserAdmin)
admin.site.register(Author, AuthorAdmin)