from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Agent(models.Model):
    first_name = models.CharField(max_length=255, default=" ")
    last_name = models.CharField(max_length=255, default=" ")
    personal_id = models.CharField(max_length=255, default=" " )
    social_security_number = models.CharField(max_length=255 , default=" ")
    father_name = models.CharField(max_length=255 ,default=" ")
    address = models.TextField(default="")
    city = models.TextField(default="")
    phone_number_1 = models.CharField(max_length=15, default="")
    phone_number_2 = models.CharField(max_length=15, blank=True, null=True)
    phone_number_3 = models.CharField(max_length=15, blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', default='default_images/PL.jpg')
    birth_certificate_image = models.ImageField(upload_to='birth_certificates/', default='default_images/PL.jpg')
    social_security_card_image = models.ImageField(upload_to='ssn_cards/', default='default_images/PL.jpg')
    agent_level = models.CharField(max_length=20 , default=" ", choices=[('اول', 'اول'), ('دوم', 'دوم'), ('رزرو', 'رزرو')])

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

@receiver(post_save, sender=Agent)
def create_user_for_agent(sender, instance, created, **kwargs):
    if created:
        User.objects.create_user(
            username=instance.social_security_number,
            password=instance.phone_number_1,
            first_name=instance.first_name,
            last_name=instance.last_name
        )
        
class Mission(models.Model):
    state = models.TextField(default="")
    sender_address = models.TextField(default="")
    receiver_address = models.TextField(default="")
    description = models.CharField(max_length=40, choices=[('هوایی','هوایی'), ('پایانه اتوبوسرانی','پایانه اتوبوسرانی'), ('پایانه تاکسیرانی','پایانه تاکسیرانی'), ('خود شخص','خود شخص')])
    box_number= models.CharField(max_length=50)
    sender_phone_number = models.CharField(max_length=50)
    receiver_phone_number = models.CharField(max_length=50)
    assigned_agent = models.ForeignKey(Agent, on_delete=models.CASCADE, default=" ")
    mission_status = models.CharField(max_length=50 , default="انجام نشده", choices=[('انجام نشده','انجام نشده'), ('در حال ارسال','در حال ارسال'), ('انجام شد','انجام شد')])
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)
    receive_from = models.CharField(max_length=50, default="")
    receive_from_number = models.CharField(max_length=15, default="")
    receive_at = models.DateTimeField(auto_now=True)
    deliver_to = models.CharField(max_length=50, default="")
    deliver_to_number = models.CharField(max_length=15, default="")
    mission_date = models.DateField(null=True, blank=True) 

    def __str__(self):
        return self.box_number