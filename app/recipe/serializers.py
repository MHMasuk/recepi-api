from rest_framework import serializers

from .models import Tag


class TagSerializer(serializers.ModelSerializer):
    """Serializer for tag serializer"""

    class Meta:
        model = Tag
        fields = ('id', 'name')
        read_only_fields = ('id', )