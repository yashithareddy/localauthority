from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class HealthSubsidy(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    applicant_name = models.CharField(max_length=100, default="", null=True)
    email = models.EmailField(default="")
    address = models.CharField(max_length=200, default="")
    city = models.CharField(max_length=100, default="")
    state = models.CharField(max_length=100, default="")
    zip_code = models.CharField(max_length=10, default="")
    insurance_number = models.CharField(max_length=50, default="")
    policy_holder = models.CharField(max_length=100, default="")
    date_of_birth = models.DateField(default="2000-01-01")
    
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other')
    ]
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, default="Male")
    medical_history = models.TextField(default="No medical history provided")
    income_proof = models.FileField(upload_to='income_proof/', null=True, blank=True)
    STATUS_CHOICES = [
        ('Accepted', 'Accepted'),
        ('Rejected', 'Rejected'),
        ('On Hold', 'On Hold'),
    ]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='On Hold')

    def __str__(self):
        return self.applicant_name

    class Meta:
        verbose_name_plural = "Health Subsidies"
    def clean(self):
        if not self.applicant_name or not self.email or not self.address or not self.city or not self.state or not self.zip_code or not self.insurance_number or not self.policy_holder or not self.date_of_birth:
            raise ValidationError('All fields are required.')

class WasteManagementApplication(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    WASTE_TYPES = (
        ('general', 'General Waste'),
        ('recyclable', 'Recyclable Waste'),
        ('organic', 'Organic Waste'),
        # Add more waste types if needed
    )

    applicant_name = models.CharField(max_length=100)
    email = models.EmailField()
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=10)
    waste_type = models.CharField(max_length=20, choices=WASTE_TYPES)
    collection_day = models.CharField(max_length=50)
    additional_info = models.TextField(blank=True, null=True)
    application_date = models.DateTimeField(auto_now_add=True)
    STATUS_CHOICES = [
        ('Accepted', 'Accepted'),
        ('Rejected', 'Rejected'),
        ('On Hold', 'On Hold'),
    ]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='On Hold')

    def __str__(self):
        return f"Waste Management Application by {self.applicant_name}"
    def clean(self):
        if not self.applicant_name or not self.email or not self.address or not self.city or not self.state or not self.zip_code or not self.waste_type or not self.collection_day:
            raise ValidationError('All fields are required.')
    
class TemporarySupportApplication(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    applicant_name = models.CharField(max_length=100)
    email = models.EmailField()
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=10)
    reason_for_support = models.TextField()
    application_date = models.DateTimeField(auto_now_add=True)
    STATUS_CHOICES = [
        ('Accepted', 'Accepted'),
        ('Rejected', 'Rejected'),
        ('On Hold', 'On Hold'),
    ]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='On Hold')

    def __str__(self):
        return f"Temporary Support Application by {self.applicant_name}"
    
class LowIncomeSupportApplication(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    applicant_name = models.CharField(max_length=100)
    email = models.EmailField()
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=10)
    monthly_income = models.DecimalField(max_digits=10, decimal_places=2)
    occupation = models.CharField(max_length=100)
    expected_support = models.DecimalField(max_digits=10, decimal_places=2)
    application_date = models.DateTimeField(auto_now_add=True)
    proof_document = models.FileField(upload_to='proof_documents/', null=True, blank=True)
    STATUS_CHOICES = [
        ('Accepted', 'Accepted'),
        ('Rejected', 'Rejected'),
        ('On Hold', 'On Hold'),
    ]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='On Hold') # New field for uploading documents

    def __str__(self):
        return f"Low Income Support Application by {self.applicant_name}"
    
class CrimeReport(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    title = models.CharField(max_length=100)
    description = models.TextField()
    location = models.CharField(max_length=200)
    reporter_name = models.CharField(max_length=100)
    evidence_proof = models.FileField(upload_to='crime_reports/', null=True, blank=True)
    STATUS_CHOICES = [
        ('Accepted', 'Accepted'),
        ('Rejected', 'Rejected'),
        ('On Hold', 'On Hold'),
    ]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='On Hold')
    

    def __str__(self):
        return self.title
    
class LocalityTaxPayment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=10)
    credit_card_number = models.CharField(max_length=16)  # Assuming credit card numbers are 16 digits
    name_on_card = models.CharField(max_length=100)
    exp_month = models.CharField(max_length=20)  # Assuming month name like "January"
    exp_year = models.CharField(max_length=4)  # Assuming year in YYYY format
    cvv = models.CharField(max_length=3)
    STATUS_CHOICES = [
        ('Accepted', 'Accepted'),
        ('Rejected', 'Rejected'),
        ('On Hold', 'On Hold'),
    ]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='On Hold')

    def __str__(self):
        return f"Locality Tax Payment by {self.full_name}"
    
class ChildCareSupport(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,default=1)
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    family_income = models.DecimalField(max_digits=10, decimal_places=2)
    reason_for_support = models.TextField()
    applied_at = models.DateTimeField(auto_now_add=True)
    income_proof = models.FileField(upload_to='income_proof/', null=True, blank=True)
    STATUS_CHOICES = [
        ('Accepted', 'Accepted'),
        ('Rejected', 'Rejected'),
        ('On Hold', 'On Hold'),
    ]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='On Hold')

    def __str__(self):
        return self.full_name
    
class PensionSupport(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    date_of_birth = models.DateField()
    reason_for_support = models.TextField()
    applied_at = models.DateTimeField(auto_now_add=True)
    birth_certificate = models.FileField(upload_to='birth_certificates/', null=True, blank=True)
    STATUS_CHOICES = [
        ('Accepted', 'Accepted'),
        ('Rejected', 'Rejected'),
        ('On Hold', 'On Hold'),
    ]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='On Hold')

    def __str__(self):
        return self.full_name
    
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    residency_proof = models.FileField()
    length_of_residency = models.CharField(max_length=50)


class News(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    publication_date = models.DateTimeField(auto_now_add=True)


class Event(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateField()
    time = models.TimeField()

    def __str__(self):
        return self.name