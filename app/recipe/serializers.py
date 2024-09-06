"""
Serializers for recipe APIS
"""
from rest_framework import serializers

from core.models import Recipe


class RecipeSerializer(serializers.ModelSerializer):
    """Serializer for recipes"""

    class Meta:
        model = Recipe
        fields = ['id', 'title', 'time_minutes', 'price', 'link']
        read_only_fields = ['id']


class RecipeDetailSerializer(RecipeSerializer):
    """Serializer for recipe detail view"""

    class Meta(RecipeSerializer.Meta):
        # Inherits the fields from RecipeSerializer.Meta and adds
        # 'description'. This allows us to reuse the base fields
        # defined in RecipeSerializer and extend them with
        # additional fields specifically for the detailed view.
        fields = RecipeSerializer.Meta.fields + ['description']
