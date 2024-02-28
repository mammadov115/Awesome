from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Post)


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ["name", "order"]
    list_editable = ["order"]