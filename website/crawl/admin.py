from django.contrib import admin

from .models import *


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'keywords', 'date')
    list_filter = ['date']
    search_fields = ['title', 'keywords']


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'major', 'sum_publish', 'sum_download')
    search_fields = ['name', 'major']


class SourceAdmin(admin.ModelAdmin):
    list_display = ('name', 'basic_info')
    search_fields = ['name']


class OrganizationAdmin(admin.ModelAdmin):
    list_display = ['name', 'used_name', 'region', 'website']
    search_fields = ['name', 'region']


class ASAdmin(admin.ModelAdmin):
    list_display = ['getArticle', 'getSource']
    search_fields = ['url_article', 'url_source']


class AAAdmin(admin.ModelAdmin):
    list_display = ['getArticle', 'getAuthor']
    search_fields = ['url_article', 'url_author']


class AOAdmin(admin.ModelAdmin):
    list_display = ['getAuthor', 'getOrganization']
    search_fields = ['url_organization', 'url_author']


class TSAdmin(admin.ModelAdmin):
    list_display = ['getTeacher', 'getStudent']
    search_fields = ['url_teacher', 'url_student']


# Register your models here.
admin.site.register(Article, ArticleAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Source, SourceAdmin)
admin.site.register(Organization, OrganizationAdmin)
admin.site.register(ReArticleSource, ASAdmin)
admin.site.register(ReArticleAuthor, AAAdmin)
admin.site.register(ReAuthorOrganization, AOAdmin)
admin.site.register(ReTeacherStudent, TSAdmin)
