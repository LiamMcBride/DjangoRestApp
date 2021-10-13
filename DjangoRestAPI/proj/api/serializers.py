from rest_framework import serializers
from proj.models import Proj, Country, State

class ProjSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proj
        fields = ["task", "completed", "timestamp", "updated", "user"]

class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ["id", "code", "name"]

class StateSerializer(serializers.ModelSerializer):
    class Meta:
        model = State
        fields = ["id", "code", "name", "countryId"]