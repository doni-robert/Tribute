from django.urls import path
from .views import (
    CountyListAPIView,
    ConstituencyListAPIView,
    WardListAPIView,
    PollingStationListAPIView,
    EntryListCreateAPIView
)

urlpatterns = [
    path('counties/', CountyListAPIView.as_view(), name='county-list'),
    path('constituencies/', ConstituencyListAPIView.as_view(), name='constituency-list'),
    path('wards/', WardListAPIView.as_view(), name='ward-list'),
    path('polling-stations/', PollingStationListAPIView.as_view(), name='pollingstation-list'),
    path('entries/', EntryListCreateAPIView.as_view(), name='entry-list-create'),
]