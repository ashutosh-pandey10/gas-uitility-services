from django.contrib.auth.models import User
from django.db import models


class ServiceRequest(models.Model):
    REQUEST_TYPE_CHOICES = [
        ("gas_leak", "Gas Leak"),
        ("meter_installation", "Meter Installation"),
        ("connection_issue", "Connection Issue"),
        # Add more request types as needed
    ]

    STATUS_CHOICES = [
        ("pending", "Pending"),
        ("in_progress", "In Progress"),
        ("completed", "Completed"),
    ]

    request_type = models.CharField(max_length=100, choices=REQUEST_TYPE_CHOICES)
    details = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="pending")
    submitted_at = models.DateTimeField(auto_now_add=True)
    resolved_at = models.DateTimeField(null=True, blank=True)
    attached_files = models.FileField(upload_to="attachments/", blank=True, null=True)
    customer = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_request_type_display()} - {self.get_status_display()}"


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=20)
    address = models.TextField()

    def __str__(self):
        return self.user.username
