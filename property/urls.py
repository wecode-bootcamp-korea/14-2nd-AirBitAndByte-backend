from django.urls import path, include

from .views      import PropertyListView, PropertyDetailView

urlpatterns = [
    path('', PropertyListView.as_view()),
    path('/<int:property_id>', PropertyDetailView.as_view()),
    path('/<int:property_id>', include('reservation.urls')),
]
