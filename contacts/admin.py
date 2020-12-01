from django.contrib import admin
from .models import Contact


class ContactAdmin(admin.ModelAdmin):
    """Displays a table of items in the admin page """
    list_display = ( 'id','listing', 'name', 'email','phone', 'contact_date')
    list_display_links = ('id','listing', 'name')
    search_fields= ('listing', 'name')
    list_per_page = 10


admin.site.register(Contact, ContactAdmin)
