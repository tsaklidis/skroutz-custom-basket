from django.contrib import admin

from skroutzbasket.list.models import List


@admin.register(List)
class ListAdmin(admin.ModelAdmin):
    model = List
    list_display = ('name',)
