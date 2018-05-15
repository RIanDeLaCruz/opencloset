from django.contrib import admin
from .models import ItemCategory, ItemSection, Item


class CategoryAdmin(admin.ModelAdmin):
    pass


class SectionAdmin(admin.ModelAdmin):
    pass


class ItemAdmin(admin.ModelAdmin):
    pass

admin.site.register(ItemCategory, CategoryAdmin)
admin.site.register(ItemSection, SectionAdmin)
admin.site.register(Item, ItemAdmin)
