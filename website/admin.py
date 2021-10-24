from django.contrib import admin
from .models import Items

class ItemsAdmin(admin.ModelAdmin):
    list_display = ['name', 'amount', 'solutions']
    # whatever you want in your admin panel like filter, search and ...

admin.site.register(Items, ItemsAdmin)