from django.contrib import admin
from .models import Menu, CustomerComment
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Menu)
class MenuAdmin(SummernoteModelAdmin):

    list_display = ('meal_title', 'slug', 'status',)
    search_fields = ['meal_title']
    list_filter = ('status',)
    prepopulated_fields = {'slug': ('meal_title',)}
    summernote_fields = ('content',)


admin.site.register(CustomerComment)