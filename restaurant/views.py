from django.shortcuts import render

from rest_framework import generics,serializers
from .serializers import BookingSerializer,MenuSerializer
from .models import *
from rest_framework.permissions import IsAuthenticated
class BookingView(generics.ListCreateAPIView):
	queryset = Booking.objects.all()
	# for i in queryset:
	# 	print(i.name)

	serializer_class = BookingSerializer
	permission_classes = [IsAuthenticated]

class MenuView(generics.ListCreateAPIView):
	queryset = Menu.objects.all()
	serializer_class = MenuSerializer
	