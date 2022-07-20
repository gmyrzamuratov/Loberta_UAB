from django.contrib import admin

# Register your models here.
from links.models import Links


class LinksAdmin(admin.ModelAdmin):
    list_display = ('id', 'url', 'user', )

admin.site.register(Links, LinksAdmin)
