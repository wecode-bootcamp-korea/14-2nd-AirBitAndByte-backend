from django.urls import path

from .views      import PaymentView

urlpatterns = [
    path('/reservation', PaymentView.as_view()),
]
