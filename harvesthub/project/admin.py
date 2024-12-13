from django.contrib import admin
from .models import Contact, Crop

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'message', 'submitted_at')
    list_filter = ('submitted_at',)
    search_fields = ('name', 'email')

@admin.register(Crop)
class CropAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'location')
    search_fields = ('name', 'location')
