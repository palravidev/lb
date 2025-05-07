from django.db import models
from django.conf import settings
from django.db import models

class Profile(models.Model):
    ROLE_CHOICES = [
        ('student',    'Student'),
        ('instructor', 'Instructor'),
        ('guest',      'Guest'),
        ('coach',      'Coach'),
    ]
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE,
                                related_name='profile')
    role = models.CharField(max_length=20,
                            choices=ROLE_CHOICES,
                            default='student')

    def __str__(self):
        return f"{self.user.email} ({self.get_role_display()})"
