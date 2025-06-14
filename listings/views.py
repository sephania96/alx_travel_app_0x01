from django.shortcuts import render
from rest_framework import viewsets
from .models import Listing, Booking
from .serializers import ListingSerializer, BookingSerializer
# Create your views here.

class ListingViewSet(viewsets.ModelViewSet):
    """Handles CRUD for listings."""
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer

class BookingViewSet(viewsets.ModelViewSet):
    """Handles CRUD for bookings."""
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer