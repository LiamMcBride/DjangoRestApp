from django.conf.urls import url
from django.urls import path, include
from .views import (
    ProjListApiView,
    CountryListApiView,
)

urlpatterns = [
    path('', ProjListApiView.as_view()),
    path('country/', CountryListApiView.as_view()),
]