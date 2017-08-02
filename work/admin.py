from django.contrib import admin
from work.models import WorkPost

# Register your models here.


class WorkPostAdmin(admin.ModelAdmin):
    list_display = ('post_title', 'post_excerpt', 'post_author', 'post_publish', 'post_status')
    list_filter = ('post_status', 'post_created', 'post_publish', 'post_author')
    search_fields = ('post_title', 'post_body')
    prepopulated_fields = {'post_slug': ('post_title', )}
    raw_id_fields = ('post_author',)
    date_hierarchy = 'post_publish'
    ordering = ['post_status', 'post_publish']

admin.site.register(WorkPost, WorkPostAdmin)

