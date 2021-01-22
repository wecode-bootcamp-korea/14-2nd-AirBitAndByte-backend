from django.urls import path, include

from .views import ReservationView

urlpatterns = [
    path('', include('user.urls')),
    path('property', include('property.urls')),
    path('reservation', ReservationView.as_view()),
]
