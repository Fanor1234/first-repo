#define Serializer class for User model
from .models import MenuTable,BookingTable
from rest_framework import serializers

class MenuSerializer(serializers.ModelSerializer):

    class Meta:
        model = MenuTable
        fields = ['Title', 'Price', 'Inventory']

class BookingSerializer(serializers.ModelSerializer):

    class Meta:
        model = BookingTable
        fields = ['Name', 'No_of_guest', 'Booking_date']      