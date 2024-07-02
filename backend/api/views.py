from rest_framework import generics
from .models import County, Constituency, Ward, PollingStation, Entry
from .serializers import CountySerializer, ConstituencySerializer, WardSerializer, PollingStationSerializer, EntrySerializer

class CountyListAPIView(generics.ListAPIView):
    """API view to retrieve list of counties."""
    queryset = County.objects.all()
    serializer_class = CountySerializer

class ConstituencyListAPIView(generics.ListAPIView):
    """API view to retrieve list of constituencies."""
    queryset = Constituency.objects.all()
    serializer_class = ConstituencySerializer

class WardListAPIView(generics.ListAPIView):
    """API view to retrieve list of wards."""
    queryset = Ward.objects.all()
    serializer_class = WardSerializer

class PollingStationListAPIView(generics.ListAPIView):
    """API view to retrieve list of polling stations."""
    queryset = PollingStation.objects.all()
    serializer_class = PollingStationSerializer

class EntryListCreateAPIView(generics.ListCreateAPIView):
    """API view to retrieve list of entries or create new."""
    queryset = Entry.objects.all()
    serializer_class = EntrySerializer
