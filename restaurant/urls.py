from django.contrib import admin
from django.urls import path
from restaurant import views

urlpatterns = [
		path("book/",views.BookingView.as_view()),
		path("menu/",views.MenuView.as_view(),name='menu-view'),
		
]