from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from .forms import LoginForm, MyPasswordResetForm  # Import MyPasswordResetForm here

from .views import healthview

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('a/',views.info, name='info'),
    
    path('registration/', views.CustomerRegistrationView.as_view(), name='customerregistration'),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='app/login.html', authentication_form=LoginForm), name='login'),
    path('success/', views.SuccessView.as_view(), name='success'),
    path('health_subsidary_apply/', views.health_subsidary_apply, name='health_subsidary_apply'),
    path('password-reset/', auth_views.PasswordResetView.as_view(template_name='app/password_reset.html', form_class=MyPasswordResetForm), name='password_reset'),
    path('locality_tax_apply/', views.locality_tax_apply, name='locality_tax_apply'),
    path('healthsuccess/', views.success_page, name='healthsuccess'), 
    path('healthsuccess/', healthview.as_view(), name='healthsuccess'),
    path('savehealth/', views.savehealth, name='savehealth'),
    path('waste-management-apply/', views.waste_management_apply, name='waste_management_apply'), # Class-based view pattern
    path('savewaste/',views.savewaste,name='savewaste'),
    path('temporary-support-apply/', views.savetemporarysupport, name='savetemporarysupport'),
    path('low_income_support_apply/', views.low_income_support_apply, name='low_income_support_apply'),
    path('reportingcrimes/', views.savecrimes, name='reportingcrimes'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('save_locality_tax/', views.save_locality_tax_payment, name='save_locality_tax'),
    path('save_child_support_application/', views.save_child_support_application, name='save_child_support_application'),
    path('save_pension_support/', views.save_pension_support_application, name='save_pension_support'),

    
    


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
