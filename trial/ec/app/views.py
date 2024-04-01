from django.shortcuts import render
from .forms import CustomerRegistrationForm
from django.views import View
from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import HealthSubsidyForm

from .models import HealthSubsidy  # Import the updated model name
from django.contrib.auth.forms import PasswordResetForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from datetime import datetime
from django.http import HttpResponse
from django.db import IntegrityError
from .models import WasteManagementApplication
from .models import TemporarySupportApplication
from .models import LowIncomeSupportApplication
from .models import CrimeReport
from .models import ChildCareSupport
from .models import LocalityTaxPayment
from .models import PensionSupport
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required 
from django.contrib.auth.decorators import login_required
# Create your views here.

def home(request):
    return render(request, 'app/home.html')

def about(request):
    return render(request, 'app/about.html')

def contact(request):
    return render(request, 'app/contact.html')

def info(request):
    return render(request, 'app/a.html')

class CustomerRegistrationView(View):  # Update class name
    def get(self, request):
        form = CustomerRegistrationForm()
        return render(request, 'app/customerregistration.html', {'form': form})

    def post(self, request):
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Congratulations! User registered successfully.")
        else:
            messages.warning(request, "Invalid input data")
        return render(request, 'app/customerregistration.html', {'form': form})

class MyPasswordResetForm(PasswordResetForm):
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)

class SuccessView(View):
    def get(self, request):
        return render(request, 'app/success.html', context=locals())

    def post(self, request):
        return render(request, 'app/success.html', context=locals())
    
def health_subsidary_apply(request):
    # Logic for handling health subsidary application form submission, if needed
    return render(request, 'app/health_subsidary_apply.html')

def locality_tax_apply(request):
    # Logic for handling locality tax application form submission, if needed
    return render(request, 'app/locality_tax_apply.html')

class healthview(View):
    def get(self, request):
        form = HealthSubsidyForm()
        return render(request, 'app/health_subsidary_apply.html', {'form': form})

    def post(self, request):
        form = HealthSubsidyForm(request.POST)
        if form.is_valid():
            # Debug: Print form data
            print(form.cleaned_data)
            try:
                form.save()
                messages.success(request, "Congratulations! Data saved successfully.")
                return redirect('healthsuccess')  # Redirect to the success page
            except Exception as e:
                # Debug: Print exception
                print(f"An error occurred while saving data: {str(e)}")
                messages.error(request, "An error occurred while saving data.")
        else:
            # Debug: Print form errors
            print(form.errors)
            messages.warning(request, "Invalid input data")
        return render(request, 'app/health_subsidary_apply.html', {'form': form})
from django.shortcuts import render, redirect
from .models import HealthSubsidy
@login_required
def savehealth(request):
    if request.method == "POST":
        applicant_name = request.POST.get('applicant_name')
        email = request.POST.get('email')
        address = request.POST.get('address')
        city = request.POST.get('city')
        state = request.POST.get('state')
        zip_code = request.POST.get('zip_code')
        insurance_number = request.POST.get('insurance_number')
        policy_holder = request.POST.get('policy_holder')
        
        date_of_birth_str = request.POST.get('date_of_birth')
        if date_of_birth_str:
            date_of_birth = datetime.strptime(date_of_birth_str, '%Y-%m-%d').date()
        else:
            date_of_birth = None

        gender = request.POST.get('gender')
        medical_history = request.POST.get('medical_history')
        income_proof_file = request.FILES.get('income_proof')
        
        if address:  # Ensure address is provided
            try:
                # Create HealthSubsidy instance associated with the logged-in user
                HealthSubsidy.objects.create(
                    user=request.user,  # Associate with the logged-in user
                    applicant_name=applicant_name, 
                    email=email, 
                    address=address, 
                    city=city, 
                    state=state, 
                    zip_code=zip_code, 
                    insurance_number=insurance_number, 
                    policy_holder=policy_holder, 
                    date_of_birth=date_of_birth, 
                    gender=gender, 
                    medical_history=medical_history,
                    income_proof=income_proof_file
                )
                return render(request, "app/healthsuccess.html")
            except IntegrityError as e:
                return HttpResponse("An error occurred while saving the health record.")
        else:
            return HttpResponse("Address is required.")
    else:
        return render(request, "health_subsidary_apply.html")

def success_page(request):
    return render(request, 'app/healthsuccess.html')

def waste_management_apply(request):
    return render(request, 'app/waste_management_apply.html')
@login_required
def savewaste(request):
    if request.method == 'POST':
        applicant_name = request.POST.get('applicant_name')
        email = request.POST.get('email')
        address = request.POST.get('address')
        city = request.POST.get('city')
        state = request.POST.get('state')
        zip_code = request.POST.get('zip_code')
        waste_type = request.POST.get('waste_type')
        collection_day = request.POST.get('collection_day')
        additional_info = request.POST.get('additional_info')
        
        # Save data to the database
        WasteManagementApplication.objects.create(
            user=request.user,  # Associate with the logged-in user
            applicant_name=applicant_name,
            email=email,
            address=address,
            city=city,
            state=state,
            zip_code=zip_code,
            waste_type=waste_type,
            collection_day=collection_day,
            additional_info=additional_info
        )

        # Redirect to the success page
        return render(request, "app/healthsuccess.html")

    return render(request, 'app/waste_management_apply.html')

def temporary_support_apply(request):
    return render(request, 'app/temporary_support_apply.html')
@login_required
def savetemporarysupport(request):
    if request.method == 'POST':
        applicant_name = request.POST.get('applicant_name')
        email = request.POST.get('email')
        address = request.POST.get('address')
        city = request.POST.get('city')
        state = request.POST.get('state')
        zip_code = request.POST.get('zip_code')
        reason_for_support = request.POST.get('reason_for_support')
        
        # Get current date and time
        application_date = datetime.now()

        # Save data to the database
        TemporarySupportApplication.objects.create(
            user=request.user,  # Associate with the logged-in user
            applicant_name=applicant_name,
            email=email,
            address=address,
            city=city,
            state=state,
            zip_code=zip_code,
            reason_for_support=reason_for_support,
            application_date=application_date
        )

        # Redirect to the success page
        return render(request, "app/healthsuccess.html")

    return render(request, 'app/temporary_support_apply.html')
@login_required
def low_income_support_apply(request):
    if request.method == 'POST':
        applicant_name = request.POST.get('applicant_name')
        email = request.POST.get('email')
        address = request.POST.get('address')
        city = request.POST.get('city')
        state = request.POST.get('state')
        zip_code = request.POST.get('zip_code')
        monthly_income = request.POST.get('monthly_income')
        occupation = request.POST.get('occupation')
        expected_support = request.POST.get('expected_support')
        proof_document = request.FILES.get('proof_document')

        # Save data to the database
        LowIncomeSupportApplication.objects.create(
            user=request.user,  # Associate with the logged-in user
            applicant_name=applicant_name,
            email=email,
            address=address,
            city=city,
            state=state,
            zip_code=zip_code,
            monthly_income=monthly_income,
            occupation=occupation,
            expected_support=expected_support,
            proof_document=proof_document
        )

        # Redirect to the success page
        return render(request, "app/healthsuccess.html")

    return render(request, 'app/low_income_support_apply.html')
@login_required
def savecrimes(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        location = request.POST.get('location')
        reporter_name = request.POST.get('reporter_name')

        # Save data to the database
        CrimeReport.objects.create(
            user=request.user,  # Associate with the logged-in user
            title=title, 
            description=description, 
            location=location, 
            reporter_name=reporter_name
        )

        # Redirect to the success page
        return render(request, "app/healthsuccess.html")  # assuming you have a named URL for healthsuccess view

    return render(request, 'app/reportingcrimes.html')

def healthsuccess(request):
    return render(request, "app/healthsuccess.html")

def logout_view(request):
  logout(request)  # Log out the user
  message = "You have been successfully logged out."  # Set the message
  return render(request, 'app/logout.html', {'message': message}) 
@login_required
def dashboard(request):
    user = request.user
    # Retrieve data for the logged-in user from newly added models
    health_subsidies = HealthSubsidy.objects.filter(user=user)
    waste_applications = WasteManagementApplication.objects.filter(user=user)
    temporary_support_applications = TemporarySupportApplication.objects.filter(user=user)
    low_income_support_applications = LowIncomeSupportApplication.objects.filter(user=user)
    crime_reports = CrimeReport.objects.filter(user=user)
    locality_tax_payments = LocalityTaxPayment.objects.filter(user=user)
    child_care_support_applications = ChildCareSupport.objects.filter(user=user)
    pension_support_applications = PensionSupport.objects.filter(user=user)
    # Calculate the counts for each application status
    accepted_count = health_subsidies.filter(status='Accepted').count()
    rejected_count = health_subsidies.filter(status='Rejected').count()
    on_hold_count = health_subsidies.filter(status='On Hold').count()
    # Calculate the counts for each application status
    accepted_count = {
        'Health Subsidies': health_subsidies.filter(status='Accepted').count(),
        'Waste Management Applications': waste_applications.filter(status='Accepted').count(),
        'Temporary Support Applications': temporary_support_applications.filter(status='Accepted').count(),
        'Low Income Support Applications': low_income_support_applications.filter(status='Accepted').count(),
        'Child Care Support Applications': child_care_support_applications.filter(status='Accepted').count(),
        'Pension Support Applications': pension_support_applications.filter(status='Accepted').count()
    }

    rejected_count = {
        'Health Subsidies': health_subsidies.filter(status='Rejected').count(),
        'Waste Management Applications': waste_applications.filter(status='Rejected').count(),
        'Temporary Support Applications': temporary_support_applications.filter(status='Rejected').count(),
        'Low Income Support Applications': low_income_support_applications.filter(status='Rejected').count(),
        'Child Care Support Applications': child_care_support_applications.filter(status='Rejected').count(),
        'Pension Support Applications': pension_support_applications.filter(status='Rejected').count()
    }

    on_hold_count = {
        'Health Subsidies': health_subsidies.filter(status='On Hold').count(),
        'Waste Management Applications': waste_applications.filter(status='On Hold').count(),
        'Temporary Support Applications': temporary_support_applications.filter(status='On Hold').count(),
        'Low Income Support Applications': low_income_support_applications.filter(status='On Hold').count(),
        'Child Care Support Applications': child_care_support_applications.filter(status='On Hold').count(),
        'Pension Support Applications': pension_support_applications.filter(status='On Hold').count()
    }
    # Prepare data for the chart
    services = list(accepted_count.keys())
    accepted_counts = list(accepted_count.values())
    rejected_counts = list(rejected_count.values())
    on_hold_counts = list(on_hold_count.values())


    return render(request, 'app/dashboard.html', {
        'health_subsidies': health_subsidies,
        'waste_applications': waste_applications,
        'temporary_support_applications': temporary_support_applications,
        'low_income_support_applications': low_income_support_applications,
        'crime_reports': crime_reports,
        'locality_tax_payments': locality_tax_payments,
        'child_care_support_applications': child_care_support_applications,
        'pension_support_applications': pension_support_applications,
        'accepted_count': accepted_count,
        'rejected_count': rejected_count,
        'on_hold_count': on_hold_count,
        'services': services,
        'accepted_counts': accepted_counts,
        'rejected_counts': rejected_counts,
        'on_hold_counts': on_hold_counts,
    })

@login_required
def save_locality_tax_payment(request):
    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        address = request.POST.get('address')
        city = request.POST.get('city')
        state = request.POST.get('state')
        zip_code = request.POST.get('zip_code')
        credit_card_number = request.POST.get('credit_card_number')
        name_on_card = request.POST.get('name_on_card')
        exp_month = request.POST.get('exp_month')
        exp_year = request.POST.get('exp_year')
        cvv = request.POST.get('cvv')
        
        # Save data to the database
        LocalityTaxPayment.objects.create(
            user=request.user,  # Associate with the logged-in user
            full_name=full_name,
            email=email,
            address=address,
            city=city,
            state=state,
            zip_code=zip_code,
            credit_card_number=credit_card_number,
            name_on_card=name_on_card,
            exp_month=exp_month,
            exp_year=exp_year,
            cvv=cvv
        )

        # Redirect to the success page
        return render(request, "app/healthsuccess.html")

    return render(request, 'app/locality_tax_apply.html')

@login_required
def save_child_support_application(request):
    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone_number')
        family_income = request.POST.get('family_income')
        reason_for_support = request.POST.get('reason_for_support')
        income_proof = request.FILES.get('income_proof')
        evidence_proof = request.FILES.get('evidence_proof')
        # Save data to the database
        ChildCareSupport.objects.create(
            user=request.user,  # Associate with the logged-in user
            full_name=full_name,
            email=email,
            phone_number=phone_number,
            family_income=family_income,
            reason_for_support=reason_for_support,
            income_proof=income_proof,
            evidence_proof=evidence_proof
        )

        # Redirect to the success page
        return render(request, "app/healthsuccess.html")

    return render(request, 'app/child_care_support_application.html')

@login_required
def save_pension_support_application(request):
    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone_number')
        date_of_birth = request.POST.get('date_of_birth')
        reason_for_support = request.POST.get('reason_for_support')
        birth_certificate = request.FILES.get('birth_certificate')
        
        # Save data to the database
        PensionSupport.objects.create(
            user=request.user,  # Associate with the logged-in user
            full_name=full_name,
            email=email,
            phone_number=phone_number,
            date_of_birth=date_of_birth,
            reason_for_support=reason_for_support,
            birth_certificate=birth_certificate
        )

        # Redirect to the success page
        return render(request, "app/healthsuccess.html")

    return render(request, 'app/pensionsupport.html')