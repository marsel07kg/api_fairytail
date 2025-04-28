from django.contrib import admin
from . import models

from django.utils.html import format_html


@admin.register(models.Character)
class BannerAdmin(admin.ModelAdmin):


    def image_tag(self, obj):
        return format_html('<img src="{}" style="max-width:200px; max-height:200px"/>'.format(obj.image.url))
    image_tag.short_description = 'Image'

    readonly_fields = ('image_tag',)

    list_display = ('name','description','image', 'image_tag',)