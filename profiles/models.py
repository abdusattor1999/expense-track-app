from django.db import models
from django.contrib.auth import get_user_model


PROFESSION_CHOICES=(
    ("Employee", "Employee"),
    ("Business", "Business"),
    ("Student", "Student"),
    ("Other", "Other"),
)

class Profile(models.Model):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
    profession = models.CharField(max_length=20, choices=PROFESSION_CHOICES)
    image = models.ImageField(upload_to='pofile_pictures/')
    savings = models.IntegerField(null=True, blank=True)
    income = models.BigIntegerField(null=True, blank=True)

    def __str__(self) -> str:
        return self.user.username
    
