from django.contrib import admin
from .models import Item

@admin.register(Item)
class ItemSerializer(admin.ModelAdmin):
  list_display=['title', 'description', 'owner']