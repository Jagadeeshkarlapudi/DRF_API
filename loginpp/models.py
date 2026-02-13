from django.db import models
from django.core.exceptions import ValidationError

class Enquiry(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    passed_year = models.CharField(max_length=10)
    qualification = models.CharField(max_length=100)
    college_name = models.CharField(max_length=150)
    address = models.TextField()
    course_interested = models.CharField(max_length=100)

    timings = models.JSONField()          # Morning, Afternoon, Evening
    training_method = models.JSONField()  # Regular, Fast Track
    training_mode = models.JSONField()    # Online, Offline

    source = models.CharField(max_length=100)
    demo_given_by = models.CharField(max_length=100)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class OnlineEnquiry(models.Model):
 
    STATUS_CHOICES = [
        ('demo_pending', 'Demo Pending'),
        ('demo_completed', 'Demo Completed'),
        ('interested', 'Interested'),
        ('not_interested', 'Not Interested'),
    ]

    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=10)
    course = models.CharField(max_length=100, blank=True, null=True)

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='demo_pending'
    )

    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name

class ContactEnquiry(models.Model):
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=10)
    email = models.EmailField()
    course = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name



def validate_image_size(image):
    max_size_kb = 300  # change if needed
    if image.size > max_size_kb * 1024:
        raise ValidationError(f"Image size should be less than {max_size_kb} KB")


class Admission(models.Model):

    # 🔹 Choices
    GENDER_CHOICES = [
        ("male", "Male"),
        ("female", "Female"),
        ("other", "Other"),
    ]

    OCCUPATION_CHOICES = [
        ("student", "Student"),
        ("employee", "Employee"),
        ("housewife", "Housewife"),
    ]

    TRAINING_MODE_CHOICES = [
        ("regular", "Regular"),
        ("fasttrack", "Fast Track"),
    ]

    TRAINING_METHOD_CHOICES = [
        ("online", "Online"),
        ("offline", "Offline"),
    ]

    TIMINGS_CHOICES = [
        ("morning", "Morning"),
        ("afternoon", "Afternoon"),
        ("evening", "Evening"),
    ]

    

    # 🔹 Basic Details
    name = models.CharField(max_length=100)
    email = models.EmailField()
    contact_number = models.CharField(max_length=10)
    alternate_number = models.CharField(max_length=10, blank=True, null=True)
    date_of_birth = models.DateField()
    qualification = models.CharField(max_length=100)
    passed_out_year = models.PositiveIntegerField()
    address = models.TextField()

    # 🔹 Radio Fields
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    occupation = models.CharField(max_length=20, choices=OCCUPATION_CHOICES)

    # 🔹 Checkbox Fields (Multiple Selection)
    training_mode = models.JSONField()      # regular, fasttrack
    training_method = models.JSONField()    # online, offline
    timings = models.JSONField()            # morning, afternoon, evening

    # 🔹 Dates
    date_of_joining = models.DateField()

    # 🔹 Dropdown Fields
    demo_given_by = models.CharField(max_length=100)
    allocated_to = models.CharField(max_length=100)
    admission_by = models.CharField(max_length=100)

    # 🔹 Image Upload
    image = models.URLField(blank=True, null=True)


    # 🔹 Checkbox (Agreement)
    fee_once_paid_not_refundable = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

