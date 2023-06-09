from django.contrib import admin
from .models import MedicalRequest

class MedicalRequestAdmin(admin.ModelAdmin):
    list_display = ["id", 'User', 'seat', 'requested_at', 'is_resolved']
    exclude = ['id']
    readonly_fields = ['User', 'requested_at']
    
admin.site.register(MedicalRequest, MedicalRequestAdmin)