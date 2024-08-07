from rest_framework import serializers

from .models import Team



class TeamsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = (
            'id',
            'name',
            'description',
            'image_url',
        )