from django.contrib import admin
from .models import system_stewart_platform, stewart_platform, law_for_platform

class system_stewart_platformAdmin(admin.ModelAdmin):
    list_display = ('id', 'title_system', 'law_type_system', 'time_create')
    list_display_links = ('id', 'title_system')
    search_fields = ('title_system', 'law_type_system', 'author')
    list_filter = ('time_create','title_system')

class law_for_platformAdmin(admin.ModelAdmin):
    list_display = ('id', 'law_type_plat', 'time_create')
    list_display_links = ('id', 'law_type_plat')
    search_fields = ('law_type_plat', 'author')
    list_filter = ('time_create','law_type_plat')

class stewart_platformAdmin(admin.ModelAdmin):
    list_display = ('id', 'title_platform', 'system_stewart_platform', 'time_create')
    list_display_links = ('id', 'title_platform')
    search_fields = ('title_platform', ' system_stewart_platform', 'author')
    list_filter = ('time_create','title_platform')


admin.site.register(system_stewart_platform, system_stewart_platformAdmin)
admin.site.register(stewart_platform, stewart_platformAdmin)
admin.site.register(law_for_platform, law_for_platformAdmin)