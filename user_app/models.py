from django.db import models
from datetime import date
from phonenumber_field.modelfields import PhoneNumberField
class User(models.Model):
    # Define gender choices
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
        ('N', 'Prefer not to say'),
    ]
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    DOB = models.DateField(default=date.today)
    mobile_number = PhoneNumberField(region=None, blank=False, null=False)
    email = models.EmailField(unique=True)
    gender = models.CharField(
        max_length=1,
        choices=GENDER_CHOICES,
        default='N',  # Set a default value if desired
    )
    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Anonymous(models.Model):
    celebrant = models.ForeignKey(User, on_delete= models.CASCADE, related_name='wishes')
    messages = models.CharField()
    created= models.TimeField(auto_now=True)
    update = models.TimeField(auto_now=True) 
    
    def __str__(self):
        return self.messages
    
    
    
    
    
    
    
    
    

# Create your models here.
