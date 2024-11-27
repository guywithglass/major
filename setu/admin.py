from django.contrib import admin
from .models import Contract


class ContractAdmin(admin.ModelAdmin):
    # Fields to display in the list view
    list_display = ('username', 'email', 'phone', 'crop',
                    'payment', 'message', 'accepted', 'accepted_by')
    # Add search functionality for username and email
    search_fields = ('username', 'email', 'accepted')
    list_filter = ('crop', 'payment')


# Register your models here.
admin.site.register(Contract, ContractAdmin)
