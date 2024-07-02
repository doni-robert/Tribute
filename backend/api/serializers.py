from rest_framework import serializers
from .models import County, Constituency, Ward, PollingStation, Entry

class CountySerializer(serializers.ModelSerializer):
    """Serializer for the County model.

    This serializer converts County model instances to and from JSON format.

    Attributes:
        Meta (class): Meta class to specify model and fields to include.
    """

    class Meta:
        """Meta class to specify the model and fields to include."""
        model = County
        fields = '__all__'


class ConstituencySerializer(serializers.ModelSerializer):
    """Serializer for the Constituency model.

    This serializer converts Constituency model instances to and from JSON format.

    Attributes:
        Meta (class): Meta class to specify model and fields to include.
    """

    class Meta:
        """Meta class to specify the model and fields to include."""
        model = Constituency
        fields = '__all__'


class WardSerializer(serializers.ModelSerializer):
    """Serializer for the Ward model.

    This serializer converts Ward model instances to and from JSON format.

    Attributes:
        Meta (class): Meta class to specify model and fields to include.
    """

    class Meta:
        """Meta class to specify the model and fields to include."""
        model = Ward
        fields = '__all__'


class PollingStationSerializer(serializers.ModelSerializer):
    """Serializer for the PollingStation model.

    This serializer converts PollingStation model instances to and from JSON format.

    Attributes:
        Meta (class): Meta class to specify model and fields to include.
    """

    class Meta:
        """Meta class to specify the model and fields to include."""
        model = PollingStation
        fields = '__all__'

class EntrySerializer(serializers.ModelSerializer):
    """Serializer for the Entry model.

    This serializer converts Entry model instances to and from JSON format,
    including all fields and relationships.

    Attributes:
        Meta (class): Meta class to specify the model and fields to include.
    """

    class Meta:
        """Meta class to specify the model and fields to include."""
        model = Entry
        fields = '__all__'