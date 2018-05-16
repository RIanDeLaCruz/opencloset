from .models import User, Item, ItemSection, ItemCategory

from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = (
            'username', 'email', 'password',
            'first_name', 'last_name', 'id', 'url'
        )


class ItemSerializer(serializers.HyperlinkedModelSerializer):
    section = serializers.SlugRelatedField(
        slug_field='name',
        queryset=ItemSection.objects.all()
    )
    category = serializers.SlugRelatedField(
        slug_field='name',
        queryset=ItemCategory.objects.all()
    )

    class Meta:
        model = Item
        fields = (
            'name', 'price', 'size',
            'brand', 'description', 'condition',
            'picture', 'section', 'category',
            'tag', 'lent_by', 'rented_by', 'url'
        )

class ItemSectionSerializer(serializers.HyperlinkedModelSerializer):
    items = ItemSerializer(many=True, read_only=True)


    class Meta:
        model = ItemSection
        fields = '__all__'

class ItemCategorySerializer(serializers.HyperlinkedModelSerializer):
    items = ItemSerializer(many=True, read_only=True)


    class Meta:
        model = ItemCategory
        fields = '__all__'
