from django.contrib import admin
from work.models import Work

# Register your models here.


class WorkAdmin(admin.ModelAdmin):
    list_display = ('title', 'excerpt', 'date')
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Work, WorkAdmin)
