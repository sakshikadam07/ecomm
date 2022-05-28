from django.contrib import admin
from .models import Men

# Register your models here.

class MenAdmin(admin.ModelAdmin):
    prepopulated_fields = { 'mens_slug': ('mens_category_name',)}
    list_display_men    = ('mens_category_name', 'mens_slug')
admin.site.register(Men, MenAdmin)
