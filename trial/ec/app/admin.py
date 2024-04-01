from django.contrib import admin
from .models import HealthSubsidy , WasteManagementApplication, TemporarySupportApplication,LowIncomeSupportApplication,CrimeReport, LocalityTaxPayment,ChildCareSupport,PensionSupport# Update the import statement

admin.site.register(HealthSubsidy)
admin.site.register(WasteManagementApplication)
admin.site.register(TemporarySupportApplication)
admin.site.register(LowIncomeSupportApplication)
admin.site.register(CrimeReport)
admin.site.register( LocalityTaxPayment)
admin.site.register(ChildCareSupport)
admin.site.register(PensionSupport)
