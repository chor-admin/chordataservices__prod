from django.contrib import admin
from .models import BlogStartPost, BlogStartTag, BlogRunPost, BlogRunTag, BlogExitPost, BlogExitTag

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


class RunPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_on', 'updated_on')
    list_fileter = ('tags', 'created_on', 'updated_on')
    search_fields = ('title',)
    prepopulated_fields = {'slug': ('title',)}
    autocomplete_fields = ('tags',)

admin.site.register(BlogRunPost, RunPostAdmin)

class TagRunAdmin(admin.ModelAdmin):
    search_fields = ('name',)

admin.site.register(BlogRunTag, TagRunAdmin)


class ExitPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_on', 'updated_on')
    list_fileter = ('tags', 'created_on', 'updated_on')
    search_fields = ('title',)
    prepopulated_fields = {'slug': ('title',)}
    autocomplete_fields = ('tags',)

admin.site.register(BlogExitPost, ExitPostAdmin)

class TagExitAdmin(admin.ModelAdmin):
    search_fields = ('name',)

admin.site.register(BlogExitTag, TagExitAdmin)