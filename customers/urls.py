from django.urls import path
from .views import customers,customers2

urlpatterns = [
    path("customers/", customers),
    path("customers2/", customers2),
]