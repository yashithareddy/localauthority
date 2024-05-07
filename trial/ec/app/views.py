from django.shortcuts import render
from .forms import CustomerRegistrationForm
from django.views import View
from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import HealthSubsidyForm

from .models import HealthSubsidy  
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
from django.db import models
from .models import News
from django import forms
# Create your views here.
from django.contrib.auth import authenticate, login

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



class SuccessView(View):
    def get(self, request):
        return render(request, 'app/success.html', context=locals())

    def post(self, request):
        return render(request, 'app/success.html', context=locals())
    
def health_subsidary_apply(request):
    
    return render(request, 'app/health_subsidary_apply.html')

def locality_tax_apply(request):
    
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
        return render(request, "app/health_subsidary_apply.html")

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
        return render(request, "app/healthsuccess.html")  

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
        #evidence_proof = request.FILES.get('evidence_proof')
        # Save data to the database
        ChildCareSupport.objects.create(
            user=request.user,  # Associate with the logged-in user
            full_name=full_name,
            email=email,
            phone_number=phone_number,
            family_income=family_income,
            reason_for_support=reason_for_support,
            income_proof=income_proof,
            #evidence_proof=evidence_proof
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

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from .models import HealthSubsidy, WasteManagementApplication, TemporarySupportApplication, LowIncomeSupportApplication, CrimeReport, LocalityTaxPayment, ChildCareSupport, PensionSupport
from .forms import newsupdate
from .forms import EventUpdate
@login_required(login_url='/admin/login/')
@staff_member_required
def admin_dashboard(request):
    if request.method == 'POST':
        fm = newsupdate(request.POST)
        fms = EventUpdate(request.POST)
        if fm.is_valid():
            fm.save()
            return redirect('admin_dashboard')
        if fms.is_valid():
            fms.save()
            return redirect('admin_dashboard')  # Redirect to the admin dashboard page after successful update
    else:
        fm = newsupdate()
        fms = EventUpdate()

    # Retrieve data for other models as before
    health_subsidies = HealthSubsidy.objects.all()
    waste_applications = WasteManagementApplication.objects.all()
    temporary_support_applications = TemporarySupportApplication.objects.all()
    low_income_support_applications = LowIncomeSupportApplication.objects.all()
    crime_reports = CrimeReport.objects.all()
    locality_tax_payments = LocalityTaxPayment.objects.all()
    child_care_support_applications = ChildCareSupport.objects.all()
    pension_support_applications = PensionSupport.objects.all()
    news_articles = News.objects.all()
    stud = News.objects.all()
    studs = Event.objects.all()  # Retrieve all events

    return render(request, 'app/admin_dasboard.html', {
        'health_subsidies': health_subsidies,
        'waste_applications': waste_applications,
        'temporary_support_applications': temporary_support_applications,
        'low_income_support_applications': low_income_support_applications,
        'crime_reports': crime_reports,
        'locality_tax_payments': locality_tax_payments,
        'child_care_support_applications': child_care_support_applications,
        'pension_support_applications': pension_support_applications,
        'news_articles': news_articles,  # Pass news articles to the template
        'form_news': fm,
        'form_event': fms,  # Pass the form instance to the template
        'stu': stud,
        'studs': studs
    })
from django.shortcuts import redirect, get_object_or_404
from django.views.decorators.http import require_POST
from .models import HealthSubsidy, WasteManagementApplication, TemporarySupportApplication, LowIncomeSupportApplication, CrimeReport, LocalityTaxPayment, ChildCareSupport, PensionSupport  # Import all application models

@login_required
@staff_member_required
@require_POST
def change_status(request, model_name, app_id):
    # Map model names to their corresponding Django model classes
    model_mapping = {
        'health_subsidy': HealthSubsidy,
        'waste_management_application': WasteManagementApplication,
        'temporary_support_application': TemporarySupportApplication,
        'low_income_support_application': LowIncomeSupportApplication,
        'crime_report': CrimeReport,
        'locality_tax_payment': LocalityTaxPayment,
        'child_care_support': ChildCareSupport,
        'pension_support': PensionSupport,
        # Add mappings for other models as needed
    }

    # Get the model class based on the model name from the mapping
    model = model_mapping.get(model_name)

    if model:
        if request.method == 'POST':
            new_status = request.POST.get('new_status')
            application = get_object_or_404(model, pk=app_id)
            application.status = new_status
            application.save()
        return redirect('admin_dashboard')
    else:
        # Redirect to admin dashboard if the model name is not valid
        return redirect('admin_dashboard')

#def admin_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None and user.is_staff:
            login(request, user)
            return redirect('admin_dashboard')
        else:
            messages.error(request, "Invalid username or password.")
    return render(request, 'admin/login.html')

#def adminlogin(request):
    return render(request, 'admin/login.html')

def news_list(request):
    news_articles = News.objects.all().order_by('-publication_date')
    return render(request, 'app/news_list.html', {'news_articles': news_articles})

def news_detail(request, news_id):
    news_article = News.objects.get(pk=news_id)
    return render(request, 'app/news_detail.html', {'news_article': news_article})

def update_news_status(request, news_id):
    if request.method == 'POST':
        new_status = request.POST.get('new_status')
        try:
            news_article = News.objects.get(pk=news_id)
            news_article.status = new_status
            news_article.save()
            # Redirect back to the news list page after updating the status
            return redirect('news_list')
        except News.DoesNotExist:
            # Handle the case where the news article does not exist
            pass
    # If the request method is not POST or news article doesn't exist, redirect to the news list page
    return redirect('news_list')

def add_news(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        # Assuming publication_date is auto-generated
        news_article = News.objects.create(title=title, content=content)
        # Redirect to the news list page after adding the news article
        return redirect('news_list')
    return render(request, 'app/add_news.html')

def financial_assisstance(request):
    return render(request, 'app/financial_assisstance.html')

def childcare_support(request):
    return render(request, 'app/childcare_support.html')

def localitytaxinfo(request):
    return render(request,'app/localitytaxinfo.html')

def pensionplanninginfo(request):
    return render(request,'app/pensionplanninginfo.html')

def wastemanagementinfo(request):
    return render(request,'app/wastemanagementinfo.html')

def healthsubsidieinfo(request):
    return render(request,'app/healthsubsidieinfo.html')

from .models import Event

def event_list(request):
    events = Event.objects.all()
    return render(request, 'app/events.html', {'events': events})
