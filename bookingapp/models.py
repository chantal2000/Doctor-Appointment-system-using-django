from django.db import models

# Create your models here.
class Doctor(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField(unique=True)
    password=models.CharField(max_length=16)
    CHOICES=(
        ('F','Female'),
        ('M','Male')
    )
    gender=models.CharField(max_length=10,choices=CHOICES)
    phonenumber=models.CharField(max_length=10)
    address=models.CharField(max_length=100)
    birthdate=models.DateField()
    bloodgroup=models.CharField(max_length=5)
    specialisation=models.CharField(max_length=50)
    def __str__(self):
        return self.name
class Receptionist(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField(unique=True)
    password=models.CharField(max_length=16)
    CHOICES=(
        ('F','Female'),
        ('M','Male')
    )
    gender=models.CharField(max_length=10,choices=CHOICES)
    phonenumber=models.CharField(max_length=10)
    address=models.CharField(max_length=100)
    birthdate=models.DateField()
    bloodgroup=models.CharField(max_length=5)
    def __str__(self):
        return self.name
class Patient(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField(unique=True)
    password=models.CharField(max_length=16)
    CHOICES=(
        ('F','Female'),
        ('M','Male')
    )
    gender=models.CharField(max_length=10,choices=CHOICES)
    phonenumber=models.CharField(max_length=10)
    address=models.CharField(max_length=100)
    birthdate=models.DateField()
    bloodgroup=models.CharField(max_length=5)
    def __str__(self):
        return self.name
class Appointment(models.Model):
    doctorname=models.CharField(max_length=50)
    doctoremail=models.EmailField(unique=True)
    patientname=models.CharField(max_length=50)
    patientemail=models.EmailField(unique=True)
    appointmentdate=models.DateField(max_length=10)
    appointmenttime=models.TimeField()
    symptoms=models.CharField(max_length=100)
    status=models.BooleanField()
    prescriptions=models.CharField(max_length=200)
    
    def __str__(self):
        return self.patientname*"You have an appointment with" *self.doctorname * "on"*self.appointmentdate