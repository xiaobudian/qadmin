from django.contrib import admin
from .models import Question, Tag

# Register your models here.

# class TagInline(admin.StackedInline):
#     model = Tag

# class QuestionAdmin(admin.ModelAdmin):  
#     inlines = [TagInline]

admin.site.register(Question)
admin.site.register(Tag)