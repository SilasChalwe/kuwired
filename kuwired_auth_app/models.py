from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
import uuid

class CustomUser(AbstractUser):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=100, unique=True)
    phone_number = models.CharField(max_length=15, unique=True)
    is_company = models.BooleanField(default=False)
    company_name = models.CharField(max_length=255, blank=True, null=True)
    company_role = models.CharField(max_length=100, blank=True, null=True)
    is_active = models.BooleanField(default=False)
    confirmation_token = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)

    # Override groups field to add related_name
    groups = models.ManyToManyField(
        Group,
        related_name='customuser_set',
        blank=True,
        help_text='The groups this user belongs to.',
        related_query_name='customuser'
    )

    # Override user_permissions field to add related_name
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='customuser_set',
        blank=True,
        help_text='Specific permissions for this user.',
        related_query_name='customuser'
    )

    def __str__(self):
        return self.username

class LoginAttempt(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    ip_address = models.GenericIPAddressField()
    timestamp = models.DateTimeField(auto_now_add=True)
    user_agent = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.user.username} logged in from {self.ip_address} on {self.timestamp}"

class LogLoginMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        if request.user.is_authenticated:
            ip_address = request.META.get('REMOTE_ADDR')
            user_agent = request.META.get('HTTP_USER_AGENT', '')

            LoginAttempt.objects.create(
                user=request.user,
                ip_address=ip_address,
                user_agent=user_agent
            )

        return response
