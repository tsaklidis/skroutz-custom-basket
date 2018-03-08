from django.contrib import admin

from skroutzbasket.list.models import List, Item


@admin.register(List)
class ListAdmin(admin.ModelAdmin):
    model = List
    list_display = ('name', 'count_items')

    def count_items(self, obj):
        return obj.items.count()
    count_items.short_description = 'Items in list:'


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    model = Item
    list_display = ('title',)
