from django.shortcuts import render

from rest_framework import generics

from .models import User, Item, ItemSection, ItemCategory
from .serializers import *


class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ItemList(generics.ListCreateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer


class ItemDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer


class ItemCategoryList(generics.ListCreateAPIView):
    queryset = ItemCategory.objects.all()
    serializer_class = ItemCategorySerializer


class ItemCategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ItemCategory.objects.all()
    serializer_class = ItemCategorySerializer


class ItemSectionList(generics.ListCreateAPIView):
    queryset = ItemSection.objects.all()
    serializer_class = ItemSectionSerializer


class ItemSectionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ItemSection.objects.all()
    serializer_class = ItemSectionSerializer
