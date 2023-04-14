from django.shortcuts import render
from django.http import HttpResponse

# serializers
from rest_framework.decorators import api_view
from rest_framework import generics
from .models import MenuTable,BookingTable
from .serializers import MenuSerializer,BookingSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated


def sayHello(request):
    return HttpResponse('<h2>Hello World</h2>')

 # Create your views here.
def index(request):
    return render(request, 'index.html', {})



# Create your views here.
class MenuItemView(generics.ListCreateAPIView):
    queryset = MenuTable.objects.all()
    serializer_class = MenuSerializer

class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = MenuTable.objects.all()
    serializer_class = MenuSerializer

class BookingViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]

    queryset = BookingTable.objects.all()
    serializer_class = BookingSerializer  