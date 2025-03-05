from rest_framework import serializers
from .models import SharewishEntry

class SharewishEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = SharewishEntry
        fields = '__all__'