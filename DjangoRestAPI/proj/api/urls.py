from django.conf.urls import url
from django.urls import path, include
from .views import (
    ProjListApiView,
    CountryListApiView,
    StateListApiView,
    statesByCountry,
)

urlpatterns = [
    path('', ProjListApiView.as_view()),
    path('country/', CountryListApiView.as_view()),
    path('state/', StateListApiView.as_view()),
    path('country/<int:countryId>/', CountryListApiView.statesById),
]