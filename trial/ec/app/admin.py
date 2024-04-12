from django.contrib import admin
from .models import HealthSubsidy , WasteManagementApplication, TemporarySupportApplication,LowIncomeSupportApplication,CrimeReport, LocalityTaxPayment,ChildCareSupport,PensionSupport# Update the import statement
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import UserProfile
from .models import News
admin.site.register(HealthSubsidy)
admin.site.register(WasteManagementApplication)
admin.site.register(TemporarySupportApplication)
admin.site.register(LowIncomeSupportApplication)
admin.site.register(CrimeReport)
admin.site.register( LocalityTaxPayment)
#admin.site.register(ChildCareSupport)
admin.site.register(PensionSupport)
@admin.register(ChildCareSupport)
class ChildCareSupportAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'phone_number', 'family_income', 'income_proof')

class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ('username', 'email', 'get_residency_proof', 'get_length_of_residency')  

    def get_residency_proof(self, obj):
        try:
            return obj.userprofile.residency_proof
        except UserProfile.DoesNotExist:
            return None

    get_residency_proof.short_description = 'Residency Proof'

    def get_length_of_residency(self, obj):
        try:
            return obj.userprofile.length_of_residency
        except UserProfile.DoesNotExist:
            return None

    get_length_of_residency.short_description = 'Length of Residency'
admin.site.register(UserProfile)
# Re-register the UserAdmin class with the custom settings
admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
admin.site.register(News)