from django.conf.urls import url
from django.urls import path, include
from .views import (
    ProjListApiView,
)

urlpatterns = [
    path('', ProjListApiView.as_view()),
]