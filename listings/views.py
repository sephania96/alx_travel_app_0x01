from django.shortcuts import render
from rest_framework import viewsets
from .models import Listing, Booking
from .serializers import ListingSerializer, BookingSerializer
# Create your views here.

class ListingviewSet(viewsets.ModelViewset):
    """Handles CRUD for listings."""
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer

class BookingviewSet(viewsets.ModelViewset):
    """Handles CRUD for bookings."""
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer