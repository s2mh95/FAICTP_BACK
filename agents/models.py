from django.db import models
from django.conf import settings

class Agent(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    personal_id = models.CharField(max_length=255)
    social_security_number = models.CharField(max_length=255)
    father_name = models.CharField(max_length=255)
    address = models.TextField(default="")
    city = models.TextField(default="")
    phone_number_1 = models.CharField(max_length=15)
    phone_number_2 = models.CharField(max_length=15, blank=True, null=True)
    phone_number_3 = models.CharField(max_length=15, blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', default='default_images/PL.jpg')
    birth_certificate_image = models.ImageField(upload_to='birth_certificates/', default='default_images/PL.jpg')
    social_security_card_image = models.ImageField(upload_to='ssn_cards/', default='default_images/PL.jpg')
    agent_level = models.CharField(max_length=20, choices=[('اول', 'اول'), ('دوم', 'دوم'), ('رزرو', 'رزرو')])
    mission_detail = models.TextField()
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"