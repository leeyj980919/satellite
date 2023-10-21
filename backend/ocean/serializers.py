from rest_framework import serializers


class ObservationSerializer(serializers.Serializer):
    ObsCode = serializers.CharField()
    Date = serializers.DateField()
