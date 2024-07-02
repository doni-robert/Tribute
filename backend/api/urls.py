from django.urls import path
from .views import (
    CountyListAPIView,
    ConstituencyListAPIView,
    WardListAPIView,
    PollingStationListAPIView,
    EntryListCreateAPIView
)

urlpatterns = [
    path('api/counties/', CountyListAPIView.as_view(), name='county-list'),
    path('api/constituencies/', ConstituencyListAPIView.as_view(), name='constituency-list'),
    path('api/wards/', WardListAPIView.as_view(), name='ward-list'),
    path('api/polling-stations/', PollingStationListAPIView.as_view(), name='pollingstation-list'),
    path('api/entries/', EntryListCreateAPIView.as_view(), name='entry-list-create'),
]