from rest_framework import serializers

from .models import Tag, Ingredient, Recipe


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


class RecipeSerializer(serializers.ModelSerializer):
    """Serializers for recipe"""
    ingredients = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Ingredient.objects.all()
    )
    tags = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Tag.objects.all()
    )

    class Meta:
        model = Recipe
        fields = ('id', 'title', 'time_minutes', 'price', 'ingredients', 'tags', 'link', )
        read_only_fields = ('id', )


class RecipeDetailSerializer(serializers.ModelSerializer):
    """Recipe detail serializer"""
    ingredients = IngredientSerializer(many=True, read_only=True)
    tags = TagSerializer(many=True, read_only=True)

    class Meta:
        model = Recipe
        fields = ('id', 'title', 'time_minutes', 'price', 'ingredients', 'tags', 'link',)
        read_only_fields = ('id',)
