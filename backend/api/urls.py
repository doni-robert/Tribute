from django.urls import path
from .views import (
    CountyListAPIView,
    ConstituencyListAPIView,
    WardListAPIView,
    PollingStationListAPIView,
    EntryListCreateAPIView,
    CountyDetailAPIView,
    ConstituenciesByCountyAPIView,
    WardsByConstituencyAPIView,
    PollingStationsByWardAPIView
)

urlpatterns = [
    path('counties/', CountyListAPIView.as_view(), name='county-list'),
    path('counties/<int:county_id>/', CountyDetailAPIView.as_view(), name='county-detail'),
    path('counties/<int:county_id>/constituencies/', ConstituenciesByCountyAPIView.as_view(), name='constituencies-by-county'),
    path('counties/<int:county_id>/constituencies/<int:constituency_id>/wards/', WardListAPIView.as_view(), name='ward-list'),
    path('constituencies/<int:constituency_id>/wards/', WardsByConstituencyAPIView.as_view(), name='wards-by-constituency'),
    path('counties/<int:county_id>/constituencies/<int:constituency_id>/wards/<int:ward_id>/pollingstations/', PollingStationListAPIView.as_view(), name='pollingstation-list'),
    path('wards/<int:ward_id>/polling_stations/', PollingStationsByWardAPIView.as_view(), name='polling-stations-by-ward'),
    path('entries/', EntryListCreateAPIView.as_view(), name='entry-list-create'),
]