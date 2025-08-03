from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import listing_list_create, listing_detail, booking_list_create, booking_detail, ListingViewSet, BookingViewSet

# Create a router and register viewsets
router = DefaultRouter()
router.register(r'listings', ListingViewSet, basename='listing')
router.register(r'bookings', BookingViewSet, basename='booking')

urlpatterns = [
    # Listings API
    path('listings/', listing_list_create, name='listing-list-create'),
    path('listings/<int:pk>/', listing_detail, name='listing-detail'),

    # Bookings API
    path('bookings/', booking_list_create, name='booking-list-create'),
    path('bookings/<int:pk>/', booking_detail, name='booking-detail'),

    path('', include(router.urls)),
]
