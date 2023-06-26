from django.contrib import admin
from metropark_02.fines.models import Fine, Payment


class FineAdmin(admin.ModelAdmin):
    # list_display = ['israeli_id', 'date_created', 'status', 'description', 'amount_in_pennies']
    list_display = ['date_created', 'status', 'description', 'amount_in_pennies']
    list_filter = ['status']
    search_fields = ['israeli_id']
    ordering = ['-date_created']

admin.site.register(Fine, FineAdmin)
admin.site.register(Payment)
