from django.db import models

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
