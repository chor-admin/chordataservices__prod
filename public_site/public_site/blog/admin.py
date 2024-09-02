from django.contrib import admin
from .models import BlogStartPost, BlogStartTag

class StartPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_on', 'updated_on')
    list_fileter = ('tags', 'created_on', 'updated_on')
    search_fields = ('title',)
    prepopulated_fields = {'slug': ('title',)}
    autocomplete_fields = ('tags',)

admin.site.register(BlogStartPost, StartPostAdmin)

class TagStartAdmin(admin.ModelAdmin):
    search_fields = ('name',)

admin.site.register(BlogStartTag, TagStartAdmin)