from rest_framework import serializers
from .models import Meme


class MemeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meme
        fields = '__all__'

    def validate_title(self, value):
        if len(value) < 3:
            raise serializers.ValidationError("Title must be at least 3 characters long.")
        return value
