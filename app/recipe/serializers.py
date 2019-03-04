from rest_framework import serializers

from .models import Tag, Ingredient


class TagSerializer(serializers.ModelSerializer):
    """Serializer for tag serializer"""

    class Meta:
        model = Tag
        fields = ('id', 'name')
        read_only_fields = ('id', )


class IngredientSerializer(serializers.ModelSerializer):
    """serializers for the ingredient objects"""

    class Meta:
        model = Ingredient
        fields = ('id', 'name', )
        read_only_fields = ('id', )
