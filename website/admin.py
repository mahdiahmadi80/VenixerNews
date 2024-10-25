from django.contrib import admin
from .models import Contact

class ContactAdmin(admin.ModelAdmin):
    list_display = ['name','email']
    search_fields = ['massage','description']
admin.site.register(Contact,ContactAdmin)
# Register your models here.
