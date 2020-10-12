from django.contrib import admin
from .models import Car

admin.site.site_title = "Парковка"
admin.site.site_header = "Парковка"

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ("manufacturer", "model", "issuance", "transmission" , "color")
    list_display_links = ("manufacturer",)
