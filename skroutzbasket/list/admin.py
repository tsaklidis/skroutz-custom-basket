from django.contrib import admin

from skroutzbasket.list.models import List, Item


@admin.register(List)
class ListAdmin(admin.ModelAdmin):
    model = List
    list_display = ('name', 'count_items', 'total_sum')

    def count_items(self, obj):
        return obj.items.count()
    count_items.short_description = 'Items in list:'

    def total_sum(self, obj):
        total_sum = 0
        for item in obj.items.all():
            total_sum = total_sum + item.price

        return '{0} euro'.format(total_sum)

    total_sum.short_description = 'List total price:'


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    model = Item
    list_display = ('title',)
