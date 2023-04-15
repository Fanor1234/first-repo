from django.db import models

#from django.contrib.auth.models import User

# Create your models here.
class BookingTable(models.Model):
    Name = models.CharField(max_length=255)
    No_of_guest = models.IntegerField()
    Booking_date = models.DateTimeField()


#    def __str__(self):
#    return self.name
    
    
class MenuTable(models.Model):
    Title = models.CharField(max_length=255)
    Price = models.DecimalField(max_digits=10, decimal_places=2)
    Inventory = models.IntegerField()

    def __str__(self):
        return f'{self.Title} : {str(self.Price)}'

#    def __str__(self):
#        return self.name