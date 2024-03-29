from django.db import models
import jsonfield
from django.utils import timezone

# Create your models here.

class reports(models.Model):
    patient_id = models.CharField(max_length=10, blank=True)
    name = models.CharField(max_length=100,blank=True)
    gender = models.CharField(max_length=10, blank=True)
    age = models.CharField (max_length=3, blank=True)
    date = models.CharField(max_length=20, blank=True) 
    normal = jsonfield.JSONField( null=True)
    abnormal = jsonfield.JSONField( null=True)
    # notes = jsonfield.JSONField( null=True)
    file_path = models.CharField(max_length=100)
    uploaded_at = models.DateTimeField(auto_now=True)

    class meta:
        db_table = "reports"


class scraped_data (models.Model):
    headline = models.CharField (max_length=500) 
    summary = models.CharField (max_length=500)
    links = models.CharField (max_length=500)
    class meta:
        db_table = "scraped_data"


class patient(models.Model):
    name = models.CharField(max_length=100,blank=True)
    gender = models.CharField(max_length=10, blank=True)
    age = models.CharField (max_length=3, blank=True)
    birthday = models.CharField (max_length=10, blank=True)
    email = models.CharField (max_length=50, blank=True)
    phone = models.CharField (max_length=20,blank=True)
    address = models.CharField (max_length=500, blank=True)
    pincode = models.CharField (max_length=10, blank=True)
    imgpath = models.CharField (max_length=100, blank=True)

    class meta:
        db_table = "patient_data"


class user(models.Model):
    name = models.CharField(max_length=100,blank=True)
    gender = models.CharField(max_length=10, blank=True)
    age = models.CharField (max_length=3, blank=True)
    email = models.CharField (max_length=50, blank=True)
    phone = models.CharField (max_length=20,blank=True)
    password = models.CharField (max_length=200,blank=True)
    user_role = models.CharField (max_length=20,blank=True)
    verification = models.CharField (max_length=30,blank=True)


class appointment(models.Model):
    patient_id = models.ForeignKey('patient',on_delete=models.CASCADE,)
    date =  models.DateTimeField(auto_now=False, auto_now_add=False)
    mobile = models.CharField (max_length=20,blank=True)
    status = models.CharField(max_length=10, blank=True)

    def datepublished(self):
        return self.date.strftime('%B %d ,  %Y')

    def timepublished(self):
        return self.date.strftime('%H : %M : %S')


class patient_history (models.Model):
    patient_id = models.ForeignKey('patient',on_delete=models.CASCADE,)
    appointment_id = models.ForeignKey('appointment',on_delete=models.CASCADE,)
    symptom = models.CharField(max_length=1000, blank=True)
    prescription = models.CharField(max_length=1000, blank=True)
