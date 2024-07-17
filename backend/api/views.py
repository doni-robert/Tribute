from rest_framework import generics
from .models import County, Constituency, Ward, PollingStation, Entry
from .serializers import CountySerializer, ConstituencySerializer, WardSerializer, PollingStationSerializer, EntrySerializer

class CountyListAPIView(generics.ListAPIView):
    """API view to retrieve list of counties."""
    queryset = County.objects.all()
    serializer_class = CountySerializer

class CountyDetailAPIView(generics.RetrieveAPIView):
    """API view to retrieve a county by ID."""
    queryset = County.objects.all()
    serializer_class = CountySerializer
    lookup_field = 'pk'

class ConstituencyListAPIView(generics.ListAPIView):
    """API view to retrieve list of constituencies."""
    queryset = Constituency.objects.all()
    serializer_class = ConstituencySerializer

class ConstituenciesByCountyAPIView(generics.ListAPIView):
    """API view to retrieve all constituencies for a specific county."""
    serializer_class = ConstituencySerializer

    def get_queryset(self):
        county_id = self.kwargs['county_id']
        return Constituency.objects.filter(county_id=county_id)

class WardListAPIView(generics.ListAPIView):
    """API view to retrieve list of wards."""
    queryset = Ward.objects.all()
    serializer_class = WardSerializer

class WardsByConstituencyAPIView(generics.ListAPIView):
    """API view to retrieve all wards for a specific constituency."""
    serializer_class = WardSerializer

    def get_queryset(self):
        constituency_id = self.kwargs['constituency_id']
        return Ward.objects.filter(constituency_id=constituency_id)

class PollingStationListAPIView(generics.ListAPIView):
    """API view to retrieve list of polling stations."""
    queryset = PollingStation.objects.all()
    serializer_class = PollingStationSerializer

class PollingStationsByWardAPIView(generics.ListAPIView):
    """API view to retrieve all polling stations for a specific ward."""
    serializer_class = PollingStationSerializer

    def get_queryset(self):
        ward_id = self.kwargs['ward_id']
        return PollingStation.objects.filter(ward_id=ward_id)

class EntryListCreateAPIView(generics.ListCreateAPIView):
    """API view to retrieve list of entries or create new."""
    queryset = Entry.objects.all()
    serializer_class = EntrySerializer
