from django.contrib import admin

from .models import Question, Choice


# Register your models here.

class ChoiceInline(admin.TabularInline):
    """
    admin.StackedInline 多行
    admin.TabularInline 单行
    """
    model = Choice
    extra = 5


class QuestionAdmin(admin.ModelAdmin):
    # fields = ['pub_date', 'question_text']
    # list_display = ('question_text', 'pub_date')
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date']}),
    ]
    inlines = [ChoiceInline]
    list_filter = ['pub_date']
    search_fields = ['question_text']


class ChoiceAdmin(admin.ModelAdmin):
    list_display = ('choice_text', 'votes')
    search_fields = ['choice_text']


admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice, ChoiceAdmin)
