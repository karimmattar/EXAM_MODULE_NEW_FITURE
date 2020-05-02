from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import post_save
from PIL import Image

ROLES = (
    ('headMaster', 'headMaster'),
    ('teacher', 'teacher'),
    ('student', 'student'),
    ('parent', 'parent'),
)

class CustomUser(AbstractUser):
    pass
    # add additional fields in here
    avatar = models.ImageField(default='unnamed.jpg', upload_to='images/')
    phone_number = models.CharField(max_length=15 ,null=True, blank=True)
    birth_date  = models.DateField(auto_now=True)
    role = models.CharField(max_length=15, choices=ROLES, null=False, blank=False)

    def __str__(self):
        return self.username