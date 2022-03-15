
from pickle import TRUE
from tkinter import CASCADE
import uuid
from django.db import models
from django.urls import reverse

# Create your models here.
class users(models.Model):
    user_id = models.AutoField(primary_key=True)
    full_names = models.CharField(max_length=100)
    contacts = models.CharField(max_length=13)
    email = models.EmailField()
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    gender = models.CharField(max_length=10)

    def __str__(self):
        return self.email


class company(models.Model):
    company_name = models.CharField(primary_key=True, max_length=200)

class buses(models.Model):
    bus_id = models.AutoField(primary_key=True)
    bus_name = models.CharField(max_length=30)
    plate_number = models.CharField(max_length=7)
    numberofseats = models.IntegerField(default=0)
    brand = models.CharField(max_length=100)

    def __str__(self):
        return str(self.plate_number)

    def get_absolute_url(self):
        """Returns the url to access a detail record for this book."""
        return reverse('bus-detail', args=[str(self.bus_id)])  

    

class drivers(models.Model):
    driver_id = models.AutoField(primary_key=True)
    driver_names = models.CharField(max_length=50)
    contact = models.CharField(max_length=13)
    gender = models.CharField(max_length=10)
    email = models.EmailField()

    def __str__(self):
        return self.driver_names

    def get_absolute_url(self):
        """Returns the url to access a detail record for this book."""
        return reverse('driver-detail', args=[str(self.driver_id)])  

class schedules(models.Model):
    schedule_id = models.AutoField(primary_key=True)
    starting_point = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    departing_time = models.TimeField()
    estimated_arrival_time = models.TimeField()
    schedule_date = models.DateField()
    bus = models.ForeignKey(buses,on_delete = models.CASCADE)
    driver = models.ForeignKey(drivers,on_delete=models.CASCADE)
    price= models.CharField(max_length=200)
    availableseats = models.IntegerField(default=0)

    def __str__(self):
        return str(self.starting_point + self.destination)
  
    def get_absolute_url(self):
        """Returns the url to access a detail record for this book."""
        return reverse('schedule-detail', args=[str(self.schedule_id)])  


class customers(models.Model):
    customer_id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    contacts = models.CharField(max_length=13)
    gender = models.CharField(max_length=10)
    email = models.EmailField()
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=30,default=12345)

    def __str__(self):
        return self.customer_id
    
    def get_absolute_url(self):
        """Returns the url to access a detail record for this book."""
        return reverse('customer-detail', args=[str(self.customer_id )])  

class bookings(models.Model):
    BOOKED = 'Booked'
    CANCELLED = 'Cancel'

    ticket_statuses= ((BOOKED,'BOOKED'),
                    (CANCELLED,'CANCELLED'),)

    booking_id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    customer_email = models.EmailField()
    schedule = models.ForeignKey(schedules, on_delete=models.CASCADE)
    tickets = models.IntegerField(default=1)
    total_amount_to_pay = models.CharField(max_length=30)
    status = models.CharField(choices=ticket_statuses, default=BOOKED, max_length=14)

    def __str__(self):
        return self.booking_id

    def get_absolute_url(self):
        """Returns the url to access a detail record for this book."""
        return reverse('booking-detail', args=[str(self.booking_id)])  



class payements(models.Model):
    payement_id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    booking = models.ForeignKey(bookings, on_delete=models.CASCADE)
    amount_paid = models.IntegerField()
    payement_date = models.DateTimeField() 
    payement_type = models.CharField(max_length=50)

    def __str__(self):
        return self.payement_id
    




